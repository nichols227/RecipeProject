import urllib2
from bs4 import BeautifulSoup
import pprint
import collections
import re
import heapq
import time
import json
prim_methods = ['saute', 'bake', 'grill', 'roast', 'barbeque', 'broil', 'boil', 'poach', 'freeze', 'fry', 'steam', 'smoke', 'simmer', 'blanch', 'pan-fry']
other_methods = ['brown', 'dip', 'toss', 'serve', 'cook', 'add', 'sprinkle', 'melt', 'garnish', 'chop', 'grate', 'stir', 'shake', 'mince', 'crush', 'squeeze', 'mix', 'julienne', 'dice', 'peel', 'shave', 'knead', 'blend', 'brush', 'grease', 'season', 'pour', 'grind', 'whisk', 'chill', 'drain', 'combine', 'heat', 'refrigerate', 'grease', 'preheat', 'arrange', 'microwave', 'coat', 'baste', 'place', 'drizzle', 'roll', 'wet']
non_descripts = ['breast', 'cutlets', 'seeds', 'whites', 'white', 'crumbs', 'flakes', 'powder', 'salt', 'oil', 'filets', 'sauce', 'jam', 'pepper', 'cheese', 'juice', 'leaves', 'noodles', 'wine', 'sugar', 'fillets', 'thighs', 'wings']
all_tools = ['stove', 'casserole dish', 'thermometer', 'aluminum foil', 'saucepan', 'oven', 'pan', 'pot', 'wok', 'grater', 'whisk', 'ladle', 'grill', 'bowl', 'knife', 'colander', 'cutting board', 'spatula', 'funnel', 'peeler', 'strainer', 'rolling pin', 'baking dish', 'skillet', 'mortar and pestle', 'plastic wrap', 'deep-fryer', 'baking sheet', 'can opener', 'slow cooker', 'blender', 'knife', 'microwave', 'baster', 'pan', 'microwave safe bowl']

#Overall Function that takes a url and creates the dictionary
def representRecipe(url):
	soup = BeautifulSoup(urllib2.urlopen(url).read())
	recipeDict = {}
	ingreds = getIngreds(soup)
	ingred_names =[]
	for ing in ingreds:
		ingred_names.append(ing['name'])
	finalDict = getSteps(soup, ingred_names)
	finalDict['ingredients'] = ingreds
	finalDict['recipe_name'] = soup.find('h1', id='itemTitle').string
	return finalDict

#Half of the recipe parser that gets the ingredients and puts them in various functions
def getIngreds(soup):
	ingredients = []
	ingreds = soup.find_all('p', 'fl-ing')
	for ing in ingreds:
		labs = ing.find_all('span')
		labels = []
		for lab in labs:
			labels.append(lab.string.lower())
		newDict = {'name': 'none', 'quantity': 'none', 'size': 'none', 'measurement': 'none', 'descriptor': 'none', 'preparation': 'none', 'prep-description': 'none'}
		if(len(labels) > 1):
			commas = labels[1].split(',')
			#special skinless, boneless case that caused roblems for the system
			if commas[0] == 'skinless' or commas[0] == 'boneless':
				chicken_name = commas[1][1:].split(' ')
				newDict['name'] = ' '.join(chicken_name[1:3])
				newDict['descriptor'] = commas[0] + ' and ' + chicken_name[0]
				newDict['quantity'] = labels[0]
				newDict['measurement'] = chicken_name[-1]
				ingredients.append(newDict)
				continue

			#Normal parsing for anem
			name = commas[0].split(' ')
			preps = []
			prep_descripts = []
			if len(name) > 1:
				count = 0
				#Bring everything ending with an 'ed' to prep and everything with a 'ly' to prep-description
				while count < len(name):
					pre = name[count]
					if pre.endswith('ed') and pre != 'red':
						preps.append(pre)
						name.pop(count)
					elif pre.endswith('ly'):
						prep_descripts.append(pre)
						name.pop(count)
					else:
						count += 1
			#Parses name based on what the last word is - if it is in the non-descripts array, or the array that holds words that need the prefix before, function finds the first prefix that can be used
			if len(name) > 1:
				if (name[-1] in non_descripts):
					if (len(name) == 2):
						newDict['name'] = ' '.join(name)
					else:
						i = -2
						while (-1 * i) < len(name):
							if name[i] in non_descripts:
								i -= 1
							else:
								newDict['name'] = ' '.join(name[i:])
								newDict['descriptor'] = ' '.join(name[:i])
								break
						else:
							newDict['name'] = ' '.join(name)
				else:
					newDict['name'] = name[-1]
					newDict['descriptor'] = ' '.join(name[:-1])
			else:
				newDict['name'] = name[0].lower()

			#Gets the measurement and quantity of the ingredient
			meas = labels[0]
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
			
			#Combines any previously found prep and prep-desctrion attributes, and also looks for anything after commas for prep
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
			taste = labels[0].replace(',', '').split(' ')
			for i in xrange(len(taste)):
				if taste[i] == 'to':
					newDict['name'] = ' '.join(taste[0:i])
					newDict['measurement'] = ' '.join(taste[i:])
					break
			else:
				newDict['name'] = ' '.join(taste)

		ingredients.append(newDict)

	return ingredients


#Function that takes the directions and parses them into steps and what methods, tools, and ingredients are used in those steps
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


			#First checks for methods that are written after commas
			stepDict['step'] = step
			step = step.lower()
			step_comma = step.split(', ')
			del step_comma[0]
			step_comma = map(lambda x: x.split(' ')[0], step_comma)
			for j in step_comma:
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

			split_string = re.split(',? |\.', step)
			and_p = False

			#Then gets rid of commas and finds methods at the start of the step of after the words 'and' or 'then'
			for i, j in enumerate(split_string):
				if j == 'and' or j== 'then':
					and_p = True
				elif i == 0 or and_p:
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
						if j not in methods_used:
							methods_used.append(j)
					elif j in other_methods:
						if j not in methods:
							methods.append(j)
						if j not in methods_used:
							methods_used.append(j)
				elif (j == 'minutes') or (j == 'seconds') or (j == 'hours') or (j == 'minute') or (j == 'second') or (j == 'hour'):
					if 'time' in stepDict.keys():
						stepDict['time'] += ' or '
						if split_string[i-2] == 'to' and is_number(split_string[i-1]) and is_number(split_string[i-3]):
							stepDict['time'] += split_string[i-3] + '-' + split_string[i-1] + ' ' + j
						else:
							stepDict['time'] += ' '.join(split_string[i-1:i+1])
					elif split_string[i-2] == 'to' and is_number(split_string[i-1]) and is_number(split_string[i-3]):
						stepDict['time'] = split_string[i-3] + '-' + split_string[i-1] + ' ' + j
					elif split_string[i-1] == 'more':
						if split_string[i-2] == 'or':
							stepDict['time'] = split_string[i-3] + ' ' + j
						else:
							stepDict['time'] = split_string[i-2] + ' ' + j
					else:
						stepDict['time'] = ' '.join(split_string[i-1:i+1])

			#Finds any ingredient names i nthe stirng. Splits the string into n-grams absed on the size of the name, but then checks the ingredients for just one fo the words in case the recipe didn't list the full word
			step_commaless = re.sub(r'\.|,', '',step).split(' ')
			for name in names:
				N = len(name.split(' '))
				grams = [' '.join(step_commaless[i:i+N]) for i in xrange(len(step_commaless) - N + 1)]
				if name in grams :
					if name not in ings_used:
						ings_used.append(name)
				elif name[-1] == 's' and name[0:-1] in grams:
					if name not in ings_used:
						ings_used.append(name)
				else:
					split_name = name.split(' ')
					if len(split_name) > 1:
						for one_name in split_name:
							if one_name in step and name not in ings_used and one_name != 'and':
								if name not in ings_used:
									ings_used.append(name)

			#Uses the same process as above to find tools in the step string
			for tool in all_tools:
				N = len(tool.split(' '))
				grams = [' '.join(step_commaless[i:i+N]) for i in xrange(len(step_commaless) - N + 1)]
				if tool in grams:
					if tool not in tools_used:
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

#Checks to make sure measurement is a number
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

#Your URL goes here:
url = None

#Uncomment following two lines to create json file
#with open('recipe_representation.json', 'w') as outfile:
#	json.dump(representRecipe(url), outfile)

#Uncomment following line to print json object
#print json.dumps(representRecipe(url))