import json
from random import choice

meats = ['alligator','bear','beef','beef heart','beef liver','beef tongue','bone soup from allowable meats','buffalo', 'bison','calf liver','caribou','crocodile','frog', 'goat','ham','horse','kangaroo', 'lamb','marrow soup','moose','mutton','opossum','organ meats','pork','bacon','rabbit','snake','squirrel','tripe','turtle','veal','venison','chicken','chicken liver','cornish game hen','duck','duck liver','emu','gizzards','goose','goose liver','chitterlings','grouse','crickets','guinea hen','liver','organs','ostrich','partridge','pheasant','quail','squab','turkey','egg','carabao','salami','pepperoni','sausage','ground beef','steak','bacon','turkey bacon','turkey burgers','cow tongue','beef jerky','smoked sausage','hot sausage','bologna','pickled bologna','hotdogs','squab','escargot']

seafood = ['flounder','tuna','anchovy','herring','basa','hake','scup','smelt','rainbow trout','hardshell clam','blue crab','peekytoe crab','spanner crab','cuttlefish','eastern oyster','pacific oyster','black sea bass','european sea bass','hybrid striped bass','bream','cod','drum','haddock','hoki','alaska pollock','rockfish','pink salmon','snaper','tilapia','turbot','walleye','lake whitefish','wolffish','hardshell clam','surf clam','cockle','jonah crab','snow crab','crayfish','bay scallop','chinese white shrimp','crayfish','arctic char','carp','catfish','dory','grouper','halibut','monkfish','pompano','dover sole','sturgeon','tilefish','wahoo','yellowtail','abalone','conch','stone crab','american lobster','spiny lobster','octopus','black tiger shrimp','freshwater shrimp','gulf shrimp','pacific white shrimp','squid','sablefish','atlantic salmon','coho salmon','skate','dungeness crab','king crab','blue mussel','greenshell mussel','pink shrimp','herring','lingcod','moi','orange roughy','atlantic ocean perch','lake victoria perch','yellow perch','european oyster','sea urchin','barramundi','cusk','dogfish','kingklip','mahimahi','opah','mako shark','swordfish','albacore tuna','yellowfin tuna','geoduck clam','squat lobster','sea scallop','rock shrimp','caviar','atlantic mackerel','escolar','chinook salmon','chum salmon','american shad','barracuda','chilean sea bass','cobia','croaker','eel','blue marlin','mullet','sockeye salmon','bluefin tuna']

pescMeatSubs = ['tuna','anchovy','herring','basa','hake','scup','smelt','rainbow trout','hardshell clam','blue crab','peekytoe crab','spanner crab','cuttlefish','eastern oyster','pacific oyster','black sea bass','european sea bass','tofu','tempeh','seitan','eggplant','lentil','beans','beets','potatoes','chickpeas','tofurky','mushroom,''falafel','flounder','hybrid striped bass','bream','cod','drum','haddock','hoki','alaska pollock','rockfish','pink salmon','snaper','tilapia','turbot','walleye','lake whitefish','wolffish','hardshell clam','surf clam','cockle','jonah crab','snow crab','crayfish','bay scallop','chinese white shrimp','crayfish','arctic char','carp','catfish','dory','grouper','halibut','monkfish','pompano','dover sole','sturgeon','tilefish','wahoo','yellowtail','abalone','conch','stone crab','american lobster','spiny lobster','octopus','black tiger shrimp','freshwater shrimp','gulf shrimp','pacific white shrimp','squid','sablefish','atlantic salmon','coho salmon','skate','dungeness crab','king crab','blue mussel','greenshell mussel','pink shrimp','herring','lingcod','moi','orange roughy','atlantic ocean perch','lake victoria perch','yellow perch','european oyster','sea urchin','barramundi','cusk','dogfish','kingklip','mahimahi','opah','mako shark','swordfish','albacore tuna','yellowfin tuna','geoduck clam','squat lobster','sea scallop','rock shrimp','atlantic mackerel','escolar','chinook salmon','chum salmon','american shad','barracuda','chilean sea bass','cobia','croaker','eel','blue marlin','mullet','sockeye salmon','bluefin tuna','caviar']

vegMeatSubs = ['tofu','tempeh','seitan','cauliflower','eggplant','lentil','beans','beets','potatoes','chickpeas','tofurky','mushroom,''falafel','fakin bacon','veggie burger']

veganMeatSubs = ['cauliflower','tofu','tempeh','seitan','eggplant','lentil','beans','beets','potatoes','chickpeas','tofurky','mushroom','falafel','fakin bacon','veggie burger']

allLactoseItems = ['milk','whole milk','whipping cream', 'creamer','cream', 'ice milk','soy milk','coconut cream', 'coconut milk','cheddar cheese','feta cheese','feta','mozzarella cheese', 'gouda','pepperjack cheese', 'parmesan cheese','asiago cheese','blue cheese','romano cheese','brie', 'butter', 'cream cheese', 'yogurt','sour cream','whipped cream','eggnog']

liquidLactoseItems = ['milk','whole milk','whipping cream', 'creamer','cream', 'ice milk']

liquidLactoseSubs = ['soy milk','coconut cream', 'coconut milk','lactose free milk']

cheeses = ['cheddar cheese','feta cheese','feta','mozzarella cheese', 'gouda','pepperjack cheese', 'parmesan cheese','asiago cheese','blue cheese','romano cheese','brie','colby','bergenost','colby cheese','cottage cheese','monterey jack cheese','muenster cheese','swiss cheese']

cheeseSubs = ['daiya shreds','rice vegan slices']

highCalorieMeat = ['beef','mutton','lard','chicken','goose','turkey','bacon']

highCalorieSeafood = ['cod','herring','salmon']

highCalorieSeafoodSubs = ['tuna','shrimp','lobster']

highCalorieMeatSubs = ['tofu','turkey bacon','turkey burger']

highCalorieAdditive = ['flaxseed oil','butter','milk']

highCalorieAdditiveSubs = ['skim milk']

highCalorieVegan = ['potatoes','beans']

highCalorieVeganSubs = ['cauliflower','tofu','tempeh','seitan','eggplant','lentil','beets','chickpeas','tofurky','mushroom','falafel','fakin bacon','veggie burger']

highCalorieSweet = ['chocolate','peanut butter','honey','chocolate chips','whipped cream','molasses','jelly','syrup','custard']

highCalorieSweetSubs = ['vanilla','cinnamon','low-fat whipped cream']

highFat = ['butter','olive oil']

highFatSubs = ['butter substitute spread']

highCarbBread = ['bread','flour tortilla','corn tortilla','biscuits','rolls','cornbread']

highCarbBreadSubs = ['zucchini','lettuce wrap','spinach wrap','cauliflower tortilla']

highCarbStarch = ['potatoes','red potatoes','sweet potatoes','corn','noodles','macaroni','brown rice','white rice','couscous','oatmeal','grits','nuts']

highCarbStarchSubs = ['black bean spaghetti','cauliflower','cottage cheese','eggplant','spaghetti squash','carrots','zucchini','mushrooms']

allSpices = ['anise','allspice','basil','bay leaves', 'caraway seeds','cardamom','cayenne pepper','chili powder','chives','cilantro','cinnamon','cloves','coriander','cumin','curry powder','dill weed', 'dill seed', 'dill', 'fennel seed', 'fenugreek', 'five-spice powder', 'garlic','ginger','ginseng','mace','marjoram','mint','mustard','nutmeg','oregano','paprika','parsley','peppercorns','poppy seeds','poppy','wine','red pepper flakes', 'rosemary', 'saffron', 'sage', 'savory', 'tarragon', 'thyme', 'turmeric','garam masala','mustard seeds','tamarind','cinnamon','red chili powder','chili powder','wasabi','beni-shouga','shouga','gari','hashouga','myouga','purslane','hibiscus','schezuan','five spice powder','dill','saffron','vanilla']

indianSpices = ['chili powder','turmeric','cumin','paprika','garam masala','coriander','mustard seeds','tamarind','cinnamon','red chili powder']

japaneseSpices = ['ginger','wasabi','beni-shouga','shouga','gari','hashouga','myouga']

mexicanSpices = ['saffron','cilantro','purslane','hibiscus','cinnamon','allspice','cayenne pepper']

italianSpices = ['oregano','parsley','basil','sage','rosemary','thyme','garlic']

chineseSpices = ['schezuan','garlic','ginger','five spice powder','cinnamon']

genericSpices = ['salt','pepper','cinnamon','vanilla']

sauces = ['honey','ketchup','mustard','mayonnaise','soy sauce','steak sauce','worcestershire sauce','honey mustard','barbecue sauce','molasses','maple syrup','hot sauce','duck sauce','ranch','caesar dressing','vinegar','vinaigrette','peanut sauce','tomato sauce','sour cream','queso','sriracha','cocktail sauce','garlic sauce']

vegetables = ['beet','cabbage','broccoli','celery','onion','kale','lettuce','raddish','turnip', 'avocado','cucumber','tomato','pumpkin', 'carrots','spinach','okra','green beans','sugar snap peas','zucchini','sweet potato','asparagus','bell pepper','eggplant','pea','soybean','lemongrass','yams','brussels sprouts','cauliflower','red potatoes','potatoes','soybean','lima beans']

fruits = ['bananas','apples','oranges','grapes','blueberries','strawberries','watermelon','mango','raisins','lemons','limes','pineapples','tangerines','peach','apricots','blackberries','dates','pumpkin','coconut','cranberries','honeydew','kiwi fruit','pears','papaya','passionfruit','raspberry','star fruit','guava','grapefruit','cantaloupe','plums', 'sweet potato','yam']

gluten = ['flour','barley','bread','flour tortilla']

allRed = ['strawberries','watermelon','cranberries','grapefruit','apples','grapes','raisins','guava', 'raspberry','beans','beets']

allOrange = ['sweet potato','apricots','pumpkin','cantaloupe','papaya','peach','tangerines','oranges','carrots']

allYellow = ['egg','corn','bananas','apples','lemons','pineapples','passion fruit','starfruit','honey']

allGreen = ['honeydew','apples','grapes','pears','kiwi fruit','limes','beet','cabbage','broccoli','celery','kale','lettuce','avocado','cucumber','spinach','okra','green beans','sugar snap peas','zucchini','asparagus','bell pepper','peas','soybean','lemongrass','brussels sprouts','lima beans']

allBlueOrPurple = ['blueberries','plums','eggplant']

allBlack = ['beans','blackberries']

allBrown = ['bear','beef','beef heart','beef liver','beef tongue','bone soup from allowable meats','buffalo', 'bison','calf liver','caribou','frog', 'goat','ham','horse','kangaroo', 'lamb','marrow soup','moose','mutton','opossum','organ meats','pork','bacon','rabbit','snake','squirrel','tripe','turtle','veal','venison','chicken','chicken liver','cornish game hen','duck','duck liver','gizzards','goose','goose liver','grouse','guinea hen','liver','organs','ostrich','partridge','pheasant','quail','squab','turkey', 'beans','soybean','chocolate','peanut butter','molasses']

allWhite = ['alligator','chicken','turkey','ostrich','emu','hen','noodles','macaroni','potatoes','rice','oatmeal','grits','couscous','cottage cheese','onion','soybean','whipped cream']

def transformation(data,originalList,transformList, type):	
	subbedList = []
	allIngredients = []
	tupleList = []
	
	for ingredient in data['ingredients']:
		allIngredients.append(ingredient['name'])
	
	for ingredient in data['ingredients']:
		for itemToReplace in originalList:
			if itemToReplace in ingredient['name'] and ingredient['name'] not in transformList:
				replaced = ingredient['name']
				sub = None
				color = None
				if replaced in allRed:
					color = allRed
				elif replaced in allOrange:
					color = allOrange
				elif replaced in allYellow:
					color = allYellow
				elif replaced in allGreen:
					color = allGreen
				elif replaced in allBlueOrPurple:
					color = allBlueOrPurple
				elif replaced in allBlack:
					color = allBlack
				elif replaced in allWhite:
					color = allWhite
				
				if color == None:
					for candidate in transformList:
						if candidate not in subbedList and candidate not in allIngredients:
							sub = candidate
							subbedList.append(candidate)
							break
					if sub == None:
						sub = choice(transformList)
				
				else:
					print "color!"
					for candidate in transformList:
						if candidate not in subbedList and candidate in color and candidate not in allIngredients:
							sub = candidate
							subbedList.append(candidate)
							break
					if sub == None:
						sub = choice(transformList)
						
				for step in data['steps']:
					for i in range(len(step['ingredients used'])):
						if replaced in step['ingredients used'][i]:
							step['step'] = step['step'].replace(step['ingredients used'][i], sub)
							step['ingredients used'][i] = sub
							
				ingredient['name'] = sub

				tupleList.append((replaced,sub,type))
				print replaced + " replaced with " + sub
				break
	return tupleList

def removeWithoutReplace(data, listToRemove):
	for ingredient in data['ingredients']:
		for itemToReplace in listToRemove:
			if itemToReplace in ingredient['name']:
				print "Remove " +ingredient['name']
							
def makeLactoseFree(data):
	tupleList = []
	tupleList +=transformation(data, cheeses, cheeseSubs, "Lactose Free")
	tupleList +=transformation(data, liquidLactoseItems, liquidLactoseSubs, "Lactose Free")
	return tupleList
	#removeWithoutReplace(data, allLactoseItems, "Lactose Free")
	
def makeLowCal(data):
	tupleList = []
	tupleList +=transformation(data, highCalorieSeafood, highCalorieSeafoodSubs, "Low Calorie")
	tupleList +=transformation(data, highCalorieMeat, highCalorieMeatSubs, "Low Calorie")
	tupleList +=transformation(data, highCalorieAdditive, highCalorieAdditiveSubs, "Low Calorie")
	tupleList +=transformation(data, highCalorieSweet, highCalorieSweetSubs, "Low Calorie")
	tupleList +=transformation(data, highCalorieVegan, highCalorieVeganSubs, "Low Calorie")
	return tupleList
	
def makeLowCarb(data):
	tupleList = []
	tupleList += transformation(data, highCarbBread, highCarbBreadSubs, "Low Carb")
	tupleList += transformation(data, highCarbStarch, highCarbStarchSubs, "Low Carb")
	return tupleList
	
def makeLowFat(data):
	return transformation(data, highFat, highFatSubs, "Low Fat")
	
def makePescatarian(data):
	return transformation(data, meats, pescMeatSubs, "Pescatarian")
	
def makeVegetarian(data):
	allMeats = meats+seafood
	return transformation(data,allMeats,vegMeatSubs, "Vegetarian")
	
def makeVegan(data):
	allMeats = meats+seafood
	return transformation(data,allMeats,veganMeatSubs, "Vegan")
	
def makeMexican(data):
	return transformation(data,allSpices,mexicanSpices, "Mexican")
	
def makeItalian(data):
	return transformation(data,allSpices,italianSpices, "Italian")
	
def makeJapanese(data):
	return transformation(data,allSpices,japaneseSpices, "Japanese")
	
def makeIndian(data):
	return transformation(data,allSpices,indianSpices, "Indian")
	
def makeChinese(data):
	return transformation(data,allSpices,chineseSpices, "Chinese")
	



def main():
	json_data=open('recipe_representation5.json')
	data = json.load(json_data)
	
	tupleList = makeVegan(data)
	print tupleList
	
	#for step in data['steps']:
	#	print step['ingredients used']
	#	print step['step']	
if __name__ == '__main__':
	main()