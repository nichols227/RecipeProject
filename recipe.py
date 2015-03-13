import urllib2
from bs4 import BeautifulSoup
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
import pprint
import collections
import re
import heapq
import time
import json

prim_methods = ['saute', 'bake', 'grill', 'roast', 'barbeque', 'broil', 'boil', 'poach', 'freeze', 'fry', 'steam', 'smoke', 'simmer', 'blanch']
other_methods = ['sprinkle', 'melt', 'garnish', 'chop', 'grate', 'stir', 'shake', 'mince', 'crush', 'squeeze', 'mix', 'julienne', 'dice', 'peel', 'shave', 'knead', 'blend', 'brush', 'grease', 'season', 'pour', 'grind', 'whisk', 'chill', 'drain', 'combine', 'heat', 'refrigerate']
non_descripts = ['flakes', 'powder', 'salt', 'oil', 'filets', 'sauce', 'jam', 'pepper', 'cheese', 'juice', 'leaves', 'noodles', 'wine', 'sugar', 'fillets']
all_tools = ['thermometer', 'aluminum foil', 'saucepan', 'oven', 'pan', 'pot', 'wok', 'grater', 'whisk', 'ladle', 'grill', 'bowl', 'knife', 'colander', 'cutting board', 'spatula', 'funnel', 'peeler', 'strainer', 'rolling pin', 'baking dish', 'skillet', 'mortar and pestle', 'plastic wrap', 'deep-fryer', 'baking sheet', 'can opener', 'slow cooker', 'blender']

def representRecipe(url):
	soup = BeautifulSoup(urllib2.urlopen(url).read())
	recipeDict = {}
	ingreds = getIngreds(soup)
	ingred_names =[]
	for ing in ingreds:
		ingred_names.append(ing['name'])
	finalDict = getSteps(soup, ingred_names)
	finalDict['ingredients'] = ingreds
	return finalDict

def getIngreds(soup):
	ingredients = []
	ingreds = soup.find_all('p', 'fl-ing')
	for ing in ingreds:
		labels = ing.find_all('span')
		newDict = {'name': 'none', 'quantity': 'none', 'size': 'none', 'measurement': 'none', 'descriptor': 'none', 'preparation': 'none', 'prep-description': 'none'}
		if(len(labels) > 1):
			commas = labels[1].string.split(',')
			if commas[0] == 'skinless' or commas[0] == 'boneless':
				chicken_name = commas[1][1:].split(' ')
				newDict['name'] = ' '.join(chicken_name[1:3])
				newDict['descriptor'] = commas[0] + ' and ' + chicken_name[0]
				newDict['quantity'] = labels[0].string
				newDict['measurement'] = chicken_name[-1]
				ingredients.append(newDict)
				continue

			name = commas[0].split(' ')
			preps = []
			prep_descripts = []
			if len(name) > 1:
				count = 0
				while count < len(name):
					pre = name[count]
					if pre.endswith('ed'):
						preps.append(pre)
						name.pop(count)
					elif pre.endswith('ly'):
						prep_descripts.append(pre)
						name.pop(count)
					else:
						count += 1
			if len(name) > 1:
				if (name[-1] in non_descripts):
					if (len(name) == 2):
						newDict['name'] = ' '.join(name)
					else:
						newDict['name'] = ' '.join(name[-2:])
						newDict['descriptor'] = ' '.join(name[:-2])
				else:
					newDict['name'] = name[-1]
					newDict['descriptor'] = ' '.join(name[:-1])
			else:
				newDict['name'] = name[0].lower()

			meas = labels[0].string
			paran = meas.find('(')
			if paran != -1:
				r_par = meas.index(')')
				newDict['size'] = meas[paran+1:r_par]
				meas = meas[:paran-1] + meas[r_par+1:]
			amts = meas.split(' ')		
			decimal = False
			for i in xrange(len(amts)):
				if '/' in amts[i]:
					decimal = True
					dec = round(float(amts[i][0])/float(amts[i][2]), 3)
					amts[i] = str(dec)[1:]
					break
			if len(amts) == 1:
				newDict['quantity'] = amts[0]
			else:
				if decimal:
					newDict['quantity'] = ''.join(amts[:-1])
				else:
					newDict['quantity'] = ' '.join(amts[:-1])
				newDict['measurement'] = amts[-1]
			
			if len(commas) > 1:
				prep = commas[1][1:].split(' ')
				if len(prep) > 1:
					for i, pre in enumerate(prep):
						if pre.endswith('ly'):
							newDict['prep-description'] = pre
							prep.pop(i)
							break
					if 'until' in prep:
						prep.pop(prep.index('until'))
					newDict['preparation'] = ' '.join(prep)
				else:
					newDict['preparation'] = prep[0]
			elif preps:
				if len(preps) == 1:
					newDict['preparation'] = preps[0]
				else:
					prep_array = []
					for pre in preps:
						prep_array.append(pre)
						prep_array.append('and')
					del prep_array[-1]
					newDict['preparation'] = ' '.join(prep_array)
			if prep_descripts:
				if len(preps) == 1:
					newDict['prep-description'] = prep_descripts[0]
				else:
					prep_array = []
					for pre in prep_descripts:
						prep_array.append(pre)
						prep_array.append('and')
					del prep_array[-1]
					newDict['prep-description'] = ' '.join(prep_array)
		else:
			taste = labels[0].string.split(' ')
			for i in xrange(len(taste)):
				if taste[i] == 'to':
					newDict['name'] = ' '.join(taste[0:i])
					newDict['descriptor'] = ' '.join(taste[i:])
					break
			else:
				newDict['name'] = ' '.join(taste)

		ingredients.append(newDict)

	return ingredients

def getSteps(soup, names):
	finalDict = {}
	primary = []
	tools =[]
	methods = []
	total_steps = []
	direcs = soup.find_all('span', 'plaincharacterwrap break')
	for direc in direcs:
		steps = re.split('\. |; ', direc.string)
		for step in steps:
			ings_used = []
			tools_used =[]
			methods_used = []
			stepDict = {}


			stepDict['step'] = step
			step = step.lower()
			split_string = re.split(',? |\.', step)
			and_p = False

			for i, j in enumerate(split_string):
				if i == 0 or and_p:
					and_p = False
					if j in prim_methods:
						check_tup = [item for item in primary if item[1] == j]
						if check_tup:
							tup = primary.pop(primary.index(check_tup[0]))
							primary.append((tup[0] - 1, j))
						else:
							primary.append((-1, j))
						if j not in methods:
							methods.append(j)
						methods_used.append(j)
					elif j in other_methods:
						if j not in methods:
							methods.append(j)
						methods_used.append(j)
				elif j == 'and':
					and_p = True
				elif (j == 'minutes') or (j == 'seconds') or (j == 'hours') or (j == 'minute') or (j == 'second') or (j == 'hour'):
					if 'time' in stepDict.keys():
						stepDict['time'] += ' or '
						if split_string[i-2] == 'to' and is_number(split_string[i-1]) and is_number(split_string[i-3]):
							stepDict['time'] += split_string[i-3] + '-' + split_string[i-1] + ' ' + j
						else:
							stepDict['time'] += ' '.join(split_string[i-1:i+1])
					elif split_string[i-2] == 'to' and is_number(split_string[i-1]) and is_number(split_string[i-3]):
						stepDict['time'] = split_string[i-3] + '-' + split_string[i-1] + ' ' + j
					else:
						stepDict['time'] = ' '.join(split_string[i-1:i+1])

			for name in names:
				if name in step:
					ings_used.append(name)
				else:
					split_name = name.split(' ')
					if len(split_name) > 1:
						for one_name in split_name:
							if one_name in step and name not in ings_used and one_name != 'and':
								ings_used.append(name)
								continue

			for tool in all_tools:
				if tool in step:
					tools_used.append(tool)
					if tool not in tools:
						tools.append(tool)
			stepDict['ingredients used'] = ings_used
			stepDict['tools_used'] = tools_used
			stepDict['methods_used'] = methods_used
			total_steps.append(stepDict)
	heapq.heapify(primary)
	finalDict['cooking methods'] = methods
	finalDict['cooking tools'] = tools
	finalDict['steps'] = total_steps
	if primary:
		finalDict['primary cooking method'] = heapq.heappop(primary)[1]
	else:
		finalDict['primary cooking method'] = 'none'
	return finalDict

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

			
with open('recipe_representation4.json', 'w') as outfile:
	json.dump(representRecipe('http://allrecipes.com/Recipe/Steak-Soup/Detail.aspx?event8=1&prop24=SR_Thumb&e11=steak&e8=Quick%20Search&event10=1&e7=Home%20Page&soid=sr_results_p1i2'), outfile)
#pprint.pprint(representRecipe('http://allrecipes.com/Recipe/Chef-Johns-Chicken-Kiev/?prop31=10'))
#pprint.pprint(representRecipe('http://allrecipes.com/Recipe/KISS-Salmon/Detail.aspx?soid=carousel_0_rotd&prop24=rotd'))