import json
from random import choice

meats = ['alligator','bear','beef','beef heart','beef liver','beef tongue','bone soup from allowable meats','buffalo', 'bison','calf liver','caribou','goat','ham','horse','kangaroo', 'lamb','marrow soup','moose','mutton','opossum','organ meats','pork','bacon','rabbit','snake','squirrel','tripe','turtle','veal','venison','chicken','chicken liver','cornish game hen','duck','duck liver','emu','gizzards','goose','goose liver','grouse','guinea hen','liver','organs','ostrich','partridge','pheasant','quail','squab','turkey']

vegMeatSubs = ['tofu','tempeh','seitan','eggplant','lentil','beans','beets','potatoes','chickpeas','tofurky','mushroom','falafel']

veganMeatSubs = ['cauliflower','tofu','tempeh','seitan','eggplant','lentil','beans','beets','potatoes','chickpeas','tofurky','mushroom','falafel']

allLactoseItems = ['milk','whole milk','whipping cream', 'creamer','cream', 'ice milk','soy milk','coconut cream', 'coconut milk','cheddar cheese','feta cheese','feta','mozzarella cheese', 'gouda','pepperjack cheese', 'parmesan cheese','asiago cheese','blue cheese','romano cheese','brie', 'butter', 'cream cheese', 'yogurt','sour cream','whipped cream','eggnog']

liquidLactoseItems = ['milk','whole milk','whipping cream', 'creamer','cream', 'ice milk']

liquidLactoseSubs = ['soy milk','coconut cream', 'coconut milk','lactose free milk']

cheeses = ['cheddar cheese','feta cheese','feta','mozzarella cheese', 'gouda','pepperjack cheese', 'parmesan cheese','asiago cheese','blue cheese','romano cheese','brie']
cheeseSubs = ['daiya shreds','rice vegan slices']

highCalorieMeat = ['beef','mutton','cod','herring','salmon','lard','chicken','goose','turkey','bacon']

highCalorieMeatSubs = ['tofu','turkey bacon','turkey burger']

highCalorieAdditive = ['flaxseed oil','butter','milk']

highCalorieAdditiveSubs = ['water']

highCalorieSweet = ['chocolate','peanut butter','honey','chocolate chips','whipped cream']

highCalorieSweetSubs = ['vanilla','cinnamon','low-fat whipped cream']

highFat = ['butter','olive oil']

highFatSubs = ['butter substitute spread']

allSpices = ['anise','allspice','basil','bay leaves', 'caraway seeds','cardamom','cayenne pepper','chili powder','chives','cilantro','cinnamon','cloves','coriander','cumin','curry powder','dill weed', 'dill seed', 'dill', 'fennel seed', 'fenugreek', 'five-spice powder', 'garlic','ginger','ginseng','mace','marjoram','mint','mustard','nutmeg','oregano','paprika','parsley','peppercorns','poppy seeds','poppy','wine','red pepper flakes', 'rosemary', 'saffron', 'sage', 'savory', 'tarragon', 'thyme', 'turmeric','garam masala','mustard seeds','tamarind','cinnamon','red chili powder','chili powder','wasabi','beni-shouga','shouga','gari','hashouga','myouga','purslane','hibiscus','schezuan','five spice powder','dill','saffron','vanilla']

indianSpices = ['chili powder','turmeric','cumin','paprika','garam masala','coriander','mustard seeds','tamarind','cinnamon','red chili powder']

japaneseSpices = ['ginger','wasabi','beni-shouga','shouga','gari','hashouga','myouga']

mexicanSpices = ['saffron','cilantro','purslane','hibiscus','cinnamon','allspice']

italianSpices = ['oregano','parsley','basil','sage','rosemary','thyme']

chineseSpices = ['schezuan','garlic','ginger','five spice powder','cinnamon']

genericSpices = ['salt','pepper','cinnamon','vanilla']

sauces = ['honey','ketchup','mustard','mayonnaise','soy sauce','steak sauce','worcestershire sauce','honey mustard','barbecue sauce','molasses','maple syrup','hot sauce','duck sauce','ranch','caesar dressing','vinegar','vinaigrette','peanut sauce','tomato sauce','sour cream','queso','sriracha','cocktail sauce','garlic sauce']

vegetables = ['beet','cabbage','broccoli','celery','onion','kale','lettuce','raddish','turnip', 'avocado','cucumber','tomato','pumpkin', 'carrots','spinach','okra','green beans','sugar snap peas','zucchini','sweet potato','asparagus','bell pepper','eggplant','pea','soybean','lemongrass','yams','brussels sprouts','cauliflower','red potatoes','potatoes','soybean','lima beans']

fruits = ['bananas','apples','oranges','grapes','blueberries','strawberries','watermelon','mango','raisins','lemons','limes','pineapples','tangerines','peach','apricots','blackberries','dates','pumpkin','coconut','cranberries','honeydew','kiwi fruit','pears','papaya','passionfruit','raspberry','star fruit','guava','grapefruit','cantaloupe','plums', 'sweet potato','yam']

highCarbs =['potatoes','sweet potatoes','corn','noodles','macaroni','rice','couscous','oatmeal','grits']

highCarbSubs = ['cauliflower','cottage cheese','eggplant','black bean spaghetti','zucchini','mushrooms']

gluten = ['flour','barley']

glutenFree = ['oat flour']

allRed = ['strawberries','watermelon','cranberries','grapefruit','apples','grapes','raisins','guava', 'raspberry','beans','beets']

allOrange = ['sweet potato','apricots','pumpkin','cantaloupe','papaya','peach','tangerines','oranges','carrots']

allYellow = ['egg','corn','bananas','apples','lemons','pineapples','passion fruit','starfruit']

allGreen = ['honeydew','apples','grapes','pears','kiwi fruit','limes','beet','cabbage','broccoli','celery','kale','lettuce','avocado','cucumber','spinach','okra','green beans','sugar snap peas','zucchini','asparagus','bell pepper','peas','soybean','lemongrass','brussels sprouts','lima beans']

allBlueOrPurple = ['blueberries','plums','eggplant']

allBlack = ['beans','blackberries']

allBrown = ['bear','beef','beef heart','beef liver','beef tongue','bone soup from allowable meats','buffalo', 'bison','calf liver','caribou','frog', 'goat','ham','horse','kangaroo', 'lamb','marrow soup','moose','mutton','opossum','organ meats','pork','bacon','rabbit','snake','squirrel','tripe','turtle','veal','venison','chicken','chicken liver','cornish game hen','duck','duck liver','gizzards','goose','goose liver','grouse','guinea hen','liver','organs','ostrich','partridge','pheasant','quail','squab','turkey', 'beans','soybean']

allWhite = ['alligator','chicken','turkey','ostrich','emu','hen','noodles','macaroni','potatoes','rice','oatmeal','grits','couscous','cottage cheese','onion','soybean']

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
	elif transformTo == 'chinese':
		originalList = allSpices
		transformList = chineseSpices
	elif transformTo == 'vegetarian':
		originalList = meats
		transformList = vegMeatSubs
	elif transformTo == 'vegetarian':
		originalList = meats
		transformList = veganMeatSubs
	elif transformTo == 'cheese':
		originalList = cheeses
		transformList = cheeseSubs
	elif transformTo == 'liquidLactose':
		originalList = liquidLactoseItems
		transformList = liquidLactoseSubs
	elif transformTo == 'highCalMeat':
		originalList = highCalorieMeat
		transformList = highCalorieMeatSubs
	elif transformTo == 'highCalAdditive':
		originalList = highCalorieAdditive
		transformList = highCalorieAdditiveSubs
	elif transformTo == 'highCalSweet':
		originalList = highCalorieSweet
		transformList = highCalorieSweetSubs
	elif transformTo == 'highFat':
		originalList = highFat
		transformList = highFatSubs
	elif transformTo == 'gluten':
		originalList = gluten
		transformList = glutenFree
	
	subbedList = []
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
						if candidate not in subbedList:
							sub = candidate
							subbedList.append(candidate)
							break
					if sub == None:
						sub = choice(transformList)
				
				else:
					for candidate in transformList:
						if candidate not in subbedList and candidate in color:
							sub = candidate
							subbedList.append(candidate)
							break
					if sub == None:
						sub = choice(transformList)
						
				print replaced + " replaced with " + sub
				break
				
def makeLactoseFree(data):
	transformation(data, 'cheese')
	transformation(data, 'liquidLactose')
	
def makeLowCal(data):
	transformation(data, 'highCalMeat')
	transformation(data, 'highCalAdditive')
	transformation(data, 'highCalSweet')

def main():
	json_data=open('recipe_representation4.json')
	data = json.load(json_data)
	#for ingredient in data['ingredients']:
	#	print ingredient['name']
	#transformation(data,'highCalMeat')
	#transformation(data,'highCalAdditive')
	#transformation(data,'highCalSweet')
	makeLowCal(data)
if __name__ == '__main__':
	main()