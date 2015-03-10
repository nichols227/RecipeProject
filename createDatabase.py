import json
import recipe

json_data=open('kb.json')
before = json.load(json_data)
json_data.close()

allIngredients = []
for category in before:
	for ingredient in before[category]:
		if ingredient not in allIngredients:
			allIngredients.append(ingredient)
			
def addToKB(url):
	newRecipe = recipe.representRecipe(url)
	for ingredient in newRecipe['ingredients']:
		name = ingredient['name']
		if name not in allIngredients:
			for key in before.keys():
				if name not in before[key]:
					enter = raw_input("should " + name + ' be in ' + key + "? (y/n)")
					if enter == 'y':
						before[key].append(name)
					if enter == 'q':
						return before
					if enter == 's':
						break
if __name__ == "__main__":
	addToKB('http://allrecipes.com/Recipe/Steak-Soup/Detail.aspx?event8=1&prop24=SR_Thumb&e11=steak&e8=Quick%20Search&event10=1&e7=Home%20Page&soid=sr_results_p1i2')
	with open('kb.json', 'w') as outfile:
		json.dump(before, outfile)