import json
from sys import maxint
import operator

kb = {}
kb['chicken'] = {'use':['main dish','meat'],'vegetarian':False, 'vegan':False, 'pescatarian':False, 'lactose':False, 'gluten':False, 'kosher': True, 'calorie':124, 'sodium':73, 'fat':1.4,'carb':0,'protein':26.1,'fiber':0,'cuisine':['american','mexican','italian','indian','asian'],'color':['white','brown'],'spiciness':'low','typicalQuantity':'pounds', 'appliances':['oven','fryer','broiler','roaster','wok']}

kb['beef'] = {'use':['main dish','meat'],'vegetarian':False, 'vegan':False, 'pescatarian':False, 'lactose':False, 'gluten':False, 'kosher': True, 'calorie':213, 'sodium':61, 'fat':13,'carb':0,'protein':22,'fiber':0,'cuisine':['american','mexican','italian','indian','asian'],'color':['brown','red'],'spiciness':'low','typicalQuantity':'pounds', 'appliances':['grill','broiler','frying pan','roaster','wok']}

kb['egg'] = {'use':['main dish, cooking tool'],'vegetarian':True, 'vegan':False, 'pescatarian':True, 'lactose':False, 'gluten':False, 'kosher': True, 'calorie':78, 'sodium':62, 'fat':5,'carb':0.6,'protein':6,'fiber':0,'cuisine':['american','mexican','italian','asian'],'color':['white','yellow'],'spiciness':'low','typicalQuantity':'count', 'appliances':['wisk','pan']}

kb['ketchup'] = {'use':['condiment'],'vegetarian':True, 'vegan':True, 'pescatarian':True, 'lactose':False, 'gluten':False, 'kosher': True, 'calorie':19, 'sodium':154, 'fat':0,'carb':4.5,'protein':0.2,'fiber':0,'cuisine':['american','mexican','italian'],'color':['red'],'spiciness':'medium','typicalQuantity':'tbsp', 'appliances':[]}

kb['brown sugar'] = {'use':['seasoning'],'vegetarian':True, 'vegan':True, 'pescatarian':True, 'lactose':False, 'gluten':False, 'kosher': True, 'calorie':17, 'sodium':1, 'fat':0,'carb':4.5,'protein':0,'fiber':0,'cuisine':['american','mexican','italian'],'color':['brown'],'spiciness':'low','typicalQuantity':'tsp', 'appliances':[]}

kb['white sugar'] = {'use':['seasoning'],'vegetarian':True, 'vegan':False, 'pescatarian':True, 'lactose':False, 'gluten':False, 'kosher': True, 'calorie':9, 'sodium':0, 'fat':0,'carb':2.3,'protein':0,'fiber':0,'cuisine':['american','mexican','italian','indian'],'color':['white'],'spiciness':'low','typicalQuantity':'grams', 'appliances':[]}

kb['bacon'] = {'use':['side dish'],'vegetarian':False, 'vegan':False, 'pescatarian':False, 'lactose':False, 'gluten':False, 'kosher': False, 'calorie':43, 'sodium':137, 'fat':3.3,'carb':0.1,'protein':3,'fiber':0,'cuisine':['american'],'color':['brown'],'spiciness':'low','typicalQuantity':'unit', 'appliances':['frying pan']}

kb['vinegar'] = {'use':['seasoning'],'vegetarian':True, 'vegan':True, 'pescatarian':True, 'lactose':False, 'gluten':False, 'kosher': True, 'calorie':3, 'sodium':0, 'fat':0,'carb':0.1,'protein':0,'fiber':0,'cuisine':['american','italian','asian'],'color':['clear'],'spiciness':'low','typicalQuantity':'tbsp', 'appliances':[]}

kb['mustard'] = {'use':['condiment'],'vegetarian':True, 'vegan':True, 'pescatarian':True, 'lactose':False, 'gluten':False, 'kosher': True, 'calorie':3, 'sodium':57, 'fat':0.2,'carb':0.3,'protein':0.2,'fiber':0.2,'cuisine':['american'],'color':['yellow'],'spiciness':'medium','typicalQuantity':'tsp', 'appliances':[]}

kb['onion'] = {'use':['seasoning'],'vegetarian':True, 'vegan':True, 'pescatarian':True, 'lactose':False, 'gluten':False, 'kosher': True, 'calorie':44, 'sodium':4, 'fat':0.1,'carb':10,'protein':1.2,'fiber':1.9,'cuisine':['american','indian','asian'],'color':['white','red','yellow'],'spiciness':'medium','typicalQuantity':'unit', 'appliances':['knife']}

kb['vegetable oil'] = {'use':['cooking tool'],'vegetarian':True, 'vegan':True, 'pescatarian':True, 'lactose':False, 'gluten':False, 'kosher': True, 'calorie':120, 'sodium':0, 'fat':14,'carb':0,'protein':0,'fiber':0,'cuisine':['american','mexican','italian','indian','asian'],'color':['clear'],'spiciness':'low','typicalQuantity':'tbsp', 'appliances':[]}

kb['chili powder'] = {'use':['seasoning'],'vegetarian':True, 'vegan':True, 'pescatarian':True, 'lactose':False, 'gluten':False, 'kosher': True, 'calorie':22, 'sodium':131, 'fat':1.1,'carb':4,'protein':1.1,'fiber':2.8,'cuisine':['indian'],'color':['red'],'spiciness':'high','typicalQuantity':'tbsp', 'appliances':[]}

kb['ginger'] = {'use':['seasoning'],'vegetarian':True, 'vegan':True, 'pescatarian':True, 'lactose':False, 'gluten':False, 'kosher': True, 'calorie':9, 'sodium':1, 'fat':0.1,'carb':2,'protein':0.2,'fiber':0.2,'cuisine':['indian','asian'],'color':['white'],'spiciness':'medium','typicalQuantity':'grams', 'appliances':[]}

kb['garlic'] = {'use':['seasoning'],'vegetarian':True, 'vegan':True, 'pescatarian':True, 'lactose':False, 'gluten':False, 'kosher': True, 'calorie':4, 'sodium':0, 'fat':0,'carb':0.9,'protein':0.2,'fiber':0.1,'cuisine':['asian','indian','italian'],'color':['white'],'spiciness':'medium','typicalQuantity':'grams', 'appliances':[]}

kb['curry powder'] = {'use':['seasoning'],'vegetarian':True, 'vegan':True, 'pescatarian':True, 'lactose':False, 'gluten':False, 'kosher': True, 'calorie':21, 'sodium':3, 'fat':0.9,'carb':3.7,'protein':0.8,'fiber':2.1,'cuisine':['indian','asian'],'color':['yellow','red'],'spiciness':'high','typicalQuantity':'tbsp', 'appliances':[]}

kb['lentil'] = {'use':['main dish', 'vegetable'],'vegetarian':True, 'vegan':True, 'pescatarian':True, 'lactose':False, 'gluten':False, 'kosher': True, 'calorie':14, 'sodium':0, 'fat':0,'carb':2.5,'protein':1.1,'fiber':1,'cuisine':['indian','asian'],'color':['green','red','yellow'],'spiciness':'high','typicalQuantity':'tbsp', 'appliances':[]}

kb['turmeric'] = {'use':['seasoning'],'vegetarian':True, 'vegan':True, 'pescatarian':True, 'lactose':False, 'gluten':False, 'kosher': True, 'calorie':24, 'sodium':3, 'fat':0.7,'carb':4.4,'protein':0.5,'fiber':1.4,'cuisine':['indian'],'color':['yellow'],'spiciness':'medium','typicalQuantity':'tbsp', 'appliances':[]}

kb['american cheese'] = {'use':['flavor'],'vegetarian':True, 'vegan':False, 'pescatarian':True, 'lactose':True, 'gluten':False, 'kosher':True, 'calorie':104, 'sodium':468, 'fat':9, 'carb':1, 'protein':5, 'fiber':0, 'cuisine':['american'],'color':['orange'],'spiciness':'low','typicalQuantity':'slice','appliances':[]}

kb['white rice'] = {'use':['side dish''starch'],'vegetarian':True, 'vegan':True, 'pescatarian':True, 'lactose':False, 'gluten':False, 'kosher':True, 'calorie':206, 'sodium':2, 'fat':0.4, 'carb':45, 'protein':4.2, 'fiber':0.6,'cuisine':['american','asian','indian','mexican'],'color':['white'],'spiciness':'low','typicalQuantity':'cup', 'appliances':[]}

kb['ham'] = {'use':['main dish','meat'],'vegetarian':False, 'vegan':False, 'pescatarian':False, 'lactose':False, 'gluten':False, 'kosher':False, 'calorie':203, 'sodium':1684, 'fat':8, 'carb':2.1, 'protein':29, 'fiber':0, 'cuisine':['american'], 'color':['pink'],'spiciness':'low','typicalQuantity':'cup','appliances':['pan','oven']}

kb['potato'] ={'use':['vegetable','starch', 'side dish'],'vegetarian':True, 'vegan':True, 'pescatarian':True, 'lactose':False, 'gluten':False, 'kosher':True, 'calorie':163, 'sodium':13, 'fat':0.2, 'carb':37, 'protein':4.3, 'fiber':4.7,'cuisine':['american','mexican','indian'],'color':['white'],'spiciness':'low','typicalQuantity':'count', 'appliances':['pot', 'knife']}

kb['spaghetti dry']= {'use':['starch', 'main dish'],'vegetarian':True, 'vegan':True, 'pescatarian':True, 'lactose':False, 'gluten':True, 'kosher':True, 'calorie':212, 'sodium':3, 'fat':0.9, 'carb':43, 'protein':7, 'fiber':1.8, 'cuisine':['italian','american','indian','asian'],'color':['white'],'spiciness':'low','typicalQuantity':'ounces', 'appliances':['pot','stove']}

kb['tomato']= {'use':['vegetable'],'vegetarian':True, 'vegan':True, 'pescatarian':True, 'lactose':False, 'gluten':False, 'kosher':True, 'calorie':22, 'sodium':6, 'fat':0.2, 'carb':4.8, 'protein':1.1, 'fiber':1.5, 'cuisine':['italian','american','indian','asian','mexican'],'color':['red'],'spiciness':'low','typicalQuantity':'count','appliances':['knife']}

kb['flour']= {'use':[''],'vegetarian':True, 'vegan':True, 'pescatarian':True, 'lactose':False, 'gluten':True, 'kosher': True, 'calorie':398, 'sodium':7, 'fat':5, 'carb':77, 'protein':10, 'fiber':9, 'cuisine':['italian','american','indian','mexican'],'color':['white'],'spiciness':'low','typicalQuantity':'grams', 'appliances':[]}

kb['apple']= {'use':['fruit'],'vegetarian':True, 'vegan':True, 'pescatarian':True, 'lactose':False, 'gluten':False, 'kosher':True, 'calorie':95, 'sodium':2, 'fat':0.3, 'carb':25, 'protein':0.5, 'fiber':4.4, 'cuisine':['american','indian','italian','mexican'],'color':['green','red','yellow'],'spiciness':'low','typicalQuantity':'count', 'appliances':['knife']}

kb['orange']= {'use':['fruit'],'vegetarian':True, 'vegan':True, 'pescatarian':True, 'lactose':False, 'gluten':False, 'kosher':True, 'calorie':45, 'sodium':0, 'fat':0, 'carb':11, 'protein':0.9, 'fiber':2.3, 'cuisine':['american','indian','mexican','asian'],'color':['orange'],'spiciness':'low','typicalQuantity':'count', 'appliances':[]}

kb['jalapeno']= {'use':['seasoning'],'vegetarian':True, 'vegan':True, 'pescatarian':True, 'lactose':False, 'gluten':False, 'kosher':True , 'calorie':26, 'sodium':3, 'fat':0.3, 'carb':6, 'protein':0.8, 'fiber':2.5, 'cuisine':['mexican'],'color':['red'],'spiciness':'high','typicalQuantity':'cup', 'appliances':[]}

kb['bell pepper']= {'use':['vegetable','seasoning'],'vegetarian':True, 'vegan':True, 'pescatarian':True, 'lactose':False, 'gluten':False, 'kosher':True, 'calorie':24, 'sodium':4, 'fat':0.2, 'carb':6, 'protein':1, 'fiber':2, 'cuisine':['american','mexican','asian','indian'],'color':['red','green','orange','yellow'],'spiciness':'medium','typicalQuantity':'cup','appliances':['knife']}

kb['broccoli']= {'use':['seasoning','side dish'],'vegetarian':True, 'vegan':True, 'pescatarian':True, 'lactose':False, 'gluten':False, 'kosher':True, 'calorie':50, 'sodium':49, 'fat':0.6, 'carb':10, 'protein':4.2, 'fiber':3.8,'cuisine':['american','indian','asian'],'color':['green'],'spiciness':'low','typicalQuantity':'cup','appliances':[]}

kb['whole milk']= {'use':[''],'vegetarian':True, 'vegan':False, 'pescatarian':True, 'lactose':True, 'gluten':False, 'kosher':True, 'calorie':103, 'sodium':107, 'fat':2.4, 'carb':12, 'protein':8, 'fiber':0, 'cuisine':['american','italian'],'color':['white'],'spiciness':'low','typicalQuantity':'cup','appliances':[]}

kb['salmon']= {'use':['main dish','meat'],'vegetarian':False, 'vegan':False, 'pescatarian':True, 'lactose':False, 'gluten':False, 'kosher':True ,'calorie':412, 'sodium':117, 'fat':27, 'carb':0, 'protein':40, 'fiber':0, 'cuisine':['indian','asian','american'],'color':['pink','brown'],'spiciness':'low','typicalQuantity':'fillet','appliances':['oven','grill','fryer']}

kb['salt']= {'use':['seasoning'],'vegetarian':True, 'vegan':True, 'pescatarian':True, 'lactose':False, 'gluten':False, 'kosher':True, 'calorie':0, 'sodium':6976, 'fat':0, 'carb':0, 'protein':0, 'fiber':0, 'cuisine':['indian','asian','mexican','italian','american'],'color':['white'],'spiciness':'low','typicalQuantity':'tbsp','appliances':[]}

kb['mozzarella cheese']= {'use':['flavor','seasoning'],'vegetarian':True, 'vegan':False, 'pescatarian':True, 'lactose':True, 'gluten':False, 'kosher':True, 'calorie':78, 'sodium':4, 'fat':4.8, 'carb':0.9, 'protein':8, 'fiber':0, 'cuisine':['italian'],'color':['white'],'spiciness':'low','typicalQuantity':'slice','appliances':[]}

kb['mushroom']= {'use':['vegetable', 'side dish'],'vegetarian':True, 'vegan':True, 'pescatarian':True, 'lactose':False, 'gluten':False, 'kosher':True, 'calorie':21, 'sodium':5, 'fat':0.3, 'carb':3.7, 'protein':0.8, 'fiber':2.1, 'cuisine':['indian','asian','italian','american'],'color':['white'],'spiciness':'low','typicalQuantity':'tbsp','appliances':[]}

kb['pineapple']= {'use':['fruit'],'vegetarian':True, 'vegan':True, 'pescatarian':True, 'lactose':False, 'gluten':False, 'kosher':True, 'calorie':82, 'sodium':2, 'fat':0.2, 'carb':22, 'protein':0.9, 'fiber':2.3, 'cuisine':['asian','american'],'color':['yellow'],'spiciness':'low','typicalQuantity':'cup','appliances':[]}

kb['shrimp']= {'use':['main dish, side dish'],'vegetarian':False, 'vegan':False, 'pescatarian':True, 'lactose':False, 'gluten':False, 'kosher':False, 'calorie':85, 'sodium':119, 'fat':0.5, 'carb':0, 'protein':20, 'fiber':0, 'cuisine':['asian','american'],'color':['pink'],'spiciness':'low','typicalQuantity':'grams','appliances':[]}

kb['carrots']= {'use':['vegetable', 'side dish'],'vegetarian':True, 'vegan':True, 'pescatarian':True, 'lactose':False, 'gluten':False, 'kosher':True, 'calorie':25, 'sodium':42, 'fat':0.2, 'carb':6, 'protein':0.6, 'fiber':1.7, 'cuisine':['indian','american'],'color':['white'],'spiciness':'low','typicalQuantity':'slice','appliances':[]}

kb['cinnamon']= {'use':['seasoning'],'vegetarian':True, 'vegan':True, 'pescatarian':True, 'lactose':False, 'gluten':False, 'kosher':True, 'calorie':19, 'sodium':1, 'fat':0.1, 'carb':6, 'protein':0.3, 'fiber':4.1, 'cuisine':['indian','asian','american'],'color':['brown'],'spiciness':'medium','typicalQuantity':'tbsp','appliances':[]}

kb['parmesan cheese']= {'use':['flavor','seasoning'],'vegetarian':True, 'vegan':False, 'pescatarian':True, 'lactose':True, 'gluten':False, 'kosher':True, 'calorie':431, 'sodium':1529, 'fat':29, 'carb':4, 'protein':38, 'fiber':0, 'cuisine':['italian'],'color':['white'],'spiciness':'low','typicalQuantity':'cup','appliances':[]}

kb['cheddar cheese']= {'use':['flavor','seasoning'],'vegetarian':True, 'vegan':False, 'pescatarian':True, 'lactose':True, 'gluten':False, 'kosher':True, 'calorie':113, 'sodium':174, 'fat':9, 'carb':0.4, 'protein':7, 'fiber':0, 'cuisine':['mexican','american','italian'],'color':['orange'],'spiciness':'low','typicalQuantity':'slice','appliances':[]}

kb['corn']={'use':['vegetable','starch'],'vegetarian':True, 'vegan':False, 'pescatarian':True, 'lactose':True, 'gluten':True, 'kosher':False, 'calorie':606, 'sodium':58, 'fat':8, 'carb':123, 'protein':16, 'fiber':12, 'cuisine':['american'],'color':['white','yellow'],'spiciness':'low','typicalQuantity':'cup','appliances':[]}

kb['butter']={'use':[''],'vegetarian':True, 'vegan':False, 'pescatarian':True, 'lactose':True, 'gluten':False, 'kosher':True, 'calorie':102, 'sodium':2, 'fat':12, 'carb':0, 'protein':0.1, 'fiber':0, 'cuisine':['american','italian'],'color':['yellow', 'white'],'spiciness':'low','typicalQuantity':'tbsp','appliances':[]}

kb['sour cream']=  {'use':['condiment'],'vegetarian':True, 'vegan':False, 'pescatarian':True, 'lactose':True, 'gluten':False, 'kosher':True, 'calorie':23, 'sodium':4, 'fat':2.4, 'carb':0.4, 'protein':0.2, 'fiber':0, 'cuisine':['mexican','american','italian'],'color':['white'],'spiciness':'low','typicalQuantity':'tbsp','appliances':[]}

kb['black beans']= {'use':['vegetable','starch', 'main dish'],'vegetarian':True, 'vegan':True, 'pescatarian':True, 'lactose':False, 'gluten':False, 'kosher':True, 'calorie':227, 'sodium':2, 'fat':1, 'carb':41, 'protein':15, 'fiber':15, 'cuisine':['mexican','indian'],'color':['black'],'spiciness':'low','typicalQuantity':'cup','appliances':[]}

kb['pinto beans']={'use':['vegetable','starch', 'main dish'],'vegetarian':True, 'vegan':False, 'pescatarian':True, 'lactose':True, 'gluten':False, 'kosher':True, 'calorie':206, 'sodium':23, 'fat':2, 'carb':37, 'protein':12, 'fiber':11, 'cuisine':['mexican'],'color':['brown'],'spiciness':'low','typicalQuantity':'cup','appliances':[]}

kb['italian sausage']= {'vegetarian':False, 'vegan':False, 'pescatarian':False, 'lactose':False, 'gluten':False, 'kosher':False, 'calorie':234, 'sodium':821, 'fat':18.57, 'carb':2.9, 'protein':13, 'fiber':0.1, 'cuisine':['italian'], 'color':['brown'], 'spiciness':'low', 'typicalQuantity':'link', 'appliances':[], 'use':['main dish','meat']}

kb['green beans']= {'vegetarian':True, 'vegan':True, 'pescatarian':True, 'lactose':False, 'gluten':False, 'kosher':True, 'calorie':31, 'sodium':6, 'fat':0.2, 'carb':7, 'protein':1.8, 'fiber':2.7, 'cuisine':['italian', 'american', 'asian', 'indian'], 'color':['green'], 'spiciness':'low', 'typicalQuantity':'cup', 'appliances':[], 'use':['vegetable','side dish']}

kb['asparagus']= {'vegetarian':True, 'vegan':True, 'pescatarian':True, 'lactose':False, 'gluten':False, 'kosher':True, 'calorie':27, 'sodium':3, 'fat':0.2, 'carb':5, 'protein':3, 'fiber':2.8, 'cuisine':['american'], 'color':['green'], 'spiciness':'low', 'typicalQuantity':'cup', 'appliances':[], 'use':['vegetable', 'side dish']}

kb['brussels sprouts']={'vegetarian':True, 'vegan':True, 'pescatarian':True, 'lactose':False, 'gluten':False, 'kosher':True, 'calorie':38, 'sodium':22, 'fat':0.3, 'carb':8, 'protein':3, 'fiber':3.3, 'cuisine':[], 'color':['green'], 'spiciness':'low', 'typicalQuantity':'cup', 'appliances':[], 'use':['vegetable', 'side dish']}

for item in kb:
	kb[item]['lactose'] =  not kb[item]['lactose']
	kb[item]['gluten'] =  not kb[item]['gluten']

meats = ['bear','beef','beef heart','beef liver','beef tongue','bone soup from allowable meats','buffalo', 'bison','calf liver','caribou','goat','ham','horse','kangaroo', 'lamb','marrow soup','moose','mutton','opossum','organ meats','pork','bacon','rabbit','snake','squirrel','tripe','turtle','veal','venison','chicken','chicken liver','cornish game hen','duck','duck liver','emu','gizzards','goose','goose liver','grouse','guinea hen','liver','organs','ostrich','partridge','pheasant','quail','squab','turkey']
nutritionFeatures = ['calorie','sodium','fat','carb','protein','fiber']


def nutritionSimilarity(ingredient1, ingredient2, diffFeature):
	nutritionDiff = 0
	sameColor = False
	sameSpiciness = False
	if set(ingredient1['use']) & set(ingredient2['use']) and (diffFeature == '' or (ingredient2[diffFeature]<ingredient1[diffFeature] and diffFeature != 'protein') or (ingredient2[diffFeature]>ingredient1[diffFeature] and diffFeature == 'protein')):
		for feature in nutritionFeatures:
			if feature != diffFeature :
				if type(ingredient1[feature]) == int or type(ingredient1[feature]) == float:
					try:
						nutritionDiff += abs(ingredient1[feature]-ingredient2[feature])/ingredient1[feature]
					except ZeroDivisionError:
						nutritionDiff += 0			
		if set(ingredient1['color']) & set(ingredient2['color']):
			sameColor = True
		if ingredient1['spiciness'] == ingredient2['spiciness']:
			sameSpiciness = True
		return [nutritionDiff, sameColor, sameSpiciness]
	return [maxint, False, False]
	
def makeNutritionTransformation(ingredient, feature):
	mostSimilarValue = maxint
	mostSimilarIngredient = ''
	for item in kb:
		if item != ingredient:
			diff = nutritionSimilarity(kb[ingredient],kb[item],feature)
			score = diff[0]
			if diff[1]:
				score -=.2
			if diff[2]:
				score -=.2
			if score<mostSimilarValue:
				mostSimilarValue = score
				mostSimilarIngredient = item


	return mostSimilarIngredient
	

def makeAllNutritionTransformations(data,feature):
	myList = []
	for ingredient in data['ingredients']:
		if ingredient['name'] in kb.keys():		
			myList.append((ingredient['name'],kb[ingredient['name']][feature]))
	myList.sort(key=operator.itemgetter(1))
	myList.reverse()
	for ingredientToReplace in myList:
		replaced = makeNutritionTransformation(ingredientToReplace[0], feature)
		if replaced != '':
			print ingredientToReplace[0]
			print replaced
			print

def makeLifestyleTransformations(data,lifestyle):
	for ingredient in data['ingredients']:
		if ingredient['name'] in kb.keys() and kb[ingredient['name']][lifestyle] == False:
			#print ingredient['name'],kb[ingredient['name']][lifestyle]
			mostSimilarValue = maxint
			mostSimilarIngredient = ''
			for item in kb:
				if item != ingredient['name'] and kb[item][lifestyle] == True:
					diff = nutritionSimilarity(kb[ingredient['name']],kb[item],'')
					#print item,diff
					score = diff[0]
					if diff[1]:
						score -=.2
					if diff[2]:
						score -=.2
					if score<mostSimilarValue:
						mostSimilarValue = score
						mostSimilarIngredient = item

			print ingredient['name']
			print mostSimilarIngredient
			print
						

	
def main():
	json_data=open('recipe_representation4.json')

	data = json.load(json_data)
	
	cuisine = 'indian'
	for ingredient in data['ingredients']:
		if ingredient['name'] in kb.keys() and 	cuisine not in kb[ingredient['name']]['cuisine']:
			print ingredient['name']
			mostSimilarValue = maxint
			mostSimilarIngredient = ''
			for item in kb:
				if item != ingredient['name'] and cuisine in kb[item]['cuisine']:
					diff = nutritionSimilarity(kb[ingredient['name']],kb[item],'')
					#print item,diff
					score = diff[0]
					if diff[1]:
						score -=.2
					if diff[2]:
						score -=.2
					if score<mostSimilarValue:
						mostSimilarValue = score
						mostSimilarIngredient = item

			#print ingredient['name']
			#print mostSimilarIngredient
			#print
	#makeLifestyleTransformations(data,'lactose')					
	#makeAllNutritionTransformations(data,'carb')
	
	json_data.close()
				
if __name__ == "__main__":
	main()