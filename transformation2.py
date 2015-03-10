import json
from random import choice

meats = ['bear','beef','beef heart','beef liver','beef tongue','bone soup from allowable meats','buffalo', 'bison','calf liver','caribou','goat','ham','horse','kangaroo', 'lamb','marrow soup','moose','mutton','opossum','organ meats','pork','bacon','rabbit','snake','squirrel','tripe','turtle','veal','venison','chicken','chicken liver','cornish game hen','duck','duck liver','emu','gizzards','goose','goose liver','grouse','guinea hen','liver','organs','ostrich','partridge','pheasant','quail','squab','turkey']

vegMeatSubs = ['tofu','tempeh','seitan','eggplant','lentil','beans','beets','potatoes','chickpeas','tofurky']

veganMeatSubs = []

allLactoseItems = ['milk','whole milk','whipping cream', 'creamer','cream', 'ice milk','soy milk','coconut cream', 'coconut milk','cheddar cheese','feta cheese','feta','mozzarella cheese', 'gouda','pepperjack cheese', 'parmesan cheese','asiago cheese','blue cheese','romano cheese','brie', 'butter', 'cream cheese', 'yogurt']

liquidLactoseItems = ['milk','whole milk','whipping cream', 'creamer','cream', 'ice milk']

liquidLactoseSubs = ['soy milk','coconut cream', 'coconut milk']

cheeses = ['cheddar cheese','feta cheese','feta','mozzarella cheese', 'gouda','pepperjack cheese', 'parmesan cheese','asiago cheese','blue cheese','romano cheese','brie']

cheeseSubs = ['daiya shreds','rice vegan slices']

highCalorie = ['beef','mutton','cod','herring','salmon','lard','chicken','goose','turkey','bacon','flaxseed oil']

highCalorieSubs = []

highFat = []

highFatSubs = []

allSpices = ['anise','allspice','basil','bay leaves', 'caraway seeds','cardamom','cayenne pepper','chili powder','chives','cilantro','cinnamon','cloves','coriander','cumin','curry powder','dill weed', 'dill seed', 'dill', 'fennel seed', 'fenugreek', 'five-spice powder', 'garlic','ginger','ginseng','mace','marjoram','mint','mustard','nutmeg','oregano','paprika','parsley','peppercorns','poppy seeds','poppy', 'red pepper flakes', 'rosemary', 'saffron', 'sage', 'savory', 'tarragon', 'thyme', 'turmeric','garam masala','mustard seeds','tamarind','cinnamon','red chili powder','chili powder','wasabi','beni-shouga','shouga','gari','hashouga','myouga','purslane','hibiscus']

indianSpices = ['chili powder','turmeric','cumin','paprika','garam masala','coriander','mustard seeds','tamarind','cinnamon','red chili powder']

japaneseSpices = ['ginger','wasabi','beni-shouga','shouga','gari','hashouga','myouga']

mexicanSpices = ['saffron','cilantro','purslane','hibiscus','cinnamon','allspice']

italianSpices = ['oregano','parsley','basil','sage','rosemary','thyme']


def transformation(data,transformTo):
	if transformTo == 'indian':
		originalList = allSpices
		transformList = indianSpices
	elif transformTo == 'japanese':
		originalList = allSpices
		transformList = japaneseSpices
	elif transformTo == 'mexican':
		originalList = allSpices
		transformList = mexicanSpices
	elif transformTo == 'italian':
		originalList = allSpices
		transformList = italianSpices
	elif transformTo == 'vegetarian':
		originalList = meats
		transformList = vegMeatSubs
	elif transformTo == 'lactoseFree':
		originalList = cheeses
		transformList = cheeseSubs
	elif transformTo == 'liquidLactose':
		originalList = liquidLactoseItems
		transformList = liquidLactoseSubs
	
	subbedList = []
	for ingredient in data['ingredients']:
		for itemToReplace in originalList:
			#print itemToReplace
			if itemToReplace in ingredient['name'] and ingredient['name'] not in transformList:
				replaced = ingredient['name']
				sub = None
				for candidate in transformList:
					if candidate not in subbedList:
						sub = candidate
						subbedList.append(candidate)
						break
				if sub == None:
					sub = choice(transformList)
					
				print replaced + " replaced with " + sub
				break
def main():
	json_data=open('recipe_representation3.json')
	data = json.load(json_data)
	transformation(data,'lactoseFree')
	transformation(data,'liquidLactose')
if __name__ == '__main__':
	main()