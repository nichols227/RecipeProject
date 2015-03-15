from Tkinter import Tk, W, E, BOTH, N, S, Button, Entry, StringVar
from ttk import Style, Frame, Label
from PIL import Image, ImageTk
import tkFont
import urllib2
from recipe import representRecipe


exampleDict = {'cooking tools': ['oven', 'baking dish', 'bowl', 'aluminum foil', 'thermometer'], 'cooking methods': [u'sprinkle', u'mix', u'pour', u'bake'], 'ingredients': [{'name': u'chicken breast', 'preparation': 'none', 'descriptor': u'skinless and boneless', 'measurement': u'halves', 'quantity': u'4', 'prep-description': 'none', 'size': 'none'}, {'name': u'pepper flakes', 'preparation': u'red', 'descriptor': 'none', 'measurement': u'tablespoon', 'quantity': u'1', 'prep-description': 'none', 'size': 'none'}, {'name': u'honey', 'preparation': 'none', 'descriptor': 'none', 'measurement': u'cup', 'quantity': '.5', 'prep-description': 'none', 'size': 'none'}, {'name': u'mustard', 'preparation': 'none', 'descriptor': u'Dijon', 'measurement': u'cup', 'quantity': '.25', 'prep-description': 'none', 'size': 'none'}], 'steps': [{'tools_used': ['oven'], 'step': u'Preheat oven to 350 degrees F (175 degrees C).', 'ingredients used': [], 'methods_used': []}, {'tools_used': ['baking dish'], 'step': u'Place chicken breasts in a baking dish', 'ingredients used': [u'chicken breast'], 'methods_used': []}, {'tools_used': [], 'step': u'sprinkle with red pepper flakes', 'ingredients used': [u'pepper flakes'], 'methods_used': [u'sprinkle']}, {'tools_used': ['bowl'], 'step': u'Mix honey and mustard in a small bowl and pour mixture over chicken', 'ingredients used': [u'chicken breast', u'honey', u'mustard'], 'methods_used': [u'mix', u'pour']}, {'tools_used': ['aluminum foil', 'baking dish'], 'step': u'Cover baking dish with aluminum foil.', 'ingredients used': [], 'methods_used': []}, {'tools_used': ['oven'], 'step': u'Bake in the preheated oven until the juices run clear and chicken is no longer pink inside, about 40 minutes', 'ingredients used': [u'chicken breast'], 'methods_used': [u'bake'], 'time': u'40 minutes'}, {'tools_used': ['thermometer'], 'step': u'An instant-read meat thermometer inserted into the thickest part of a breast should read at least 160 degrees F (70 degrees C).', 'ingredients used': [u'chicken breast'], 'methods_used': []}], 'primary cooking method': u'bake'}


def makeGui():
	root = Tk()
	root.title("Recipe Parser")
	allframe = Frame(root)
	allframe.grid(column=0, row=0, sticky=(N, W, E, S))
	mainframe = Frame(allframe)
	mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

	def parseRecipe(event):
		recipeUrl = urlEntry.get()
		try:
			urllib2.urlopen(recipeUrl)
		except ValueError:
			print "Invalid URL. Please Try Again"
			urlEntry.delete(0, END)
			return
		if 'allrecipes.com' not in recipeUrl:
			print "Invalid URL. Please Try Again"
			urlEntry.delete(0, END)
			return
		fillGui(root, recipeUrl)

	style = Style()
	style.theme_use("default")

	mainframe.columnconfigure(0, pad=3, weight=1)
	mainframe.columnconfigure(1, pad=3, weight=1)
	mainframe.columnconfigure(2, pad=3, weight=1)
	mainframe.columnconfigure(3, pad=3, weight=1)
	mainframe.columnconfigure(4, pad=3, weight=1)
	mainframe.columnconfigure(5, pad=3, weight=1)
	mainframe.columnconfigure(6, pad=3, weight=1)
	mainframe.columnconfigure(7, pad=3, weight=1)
	mainframe.columnconfigure(8, pad=3, weight=1)
	mainframe.columnconfigure(9, pad=3, weight=1)

	mainframe.rowconfigure(0, pad=3, weight=1)
	mainframe.rowconfigure(1, pad=3, weight=1)
	mainframe.rowconfigure(2, pad=3, weight=1)
	mainframe.rowconfigure(3, pad=3, weight=1)
	mainframe.rowconfigure(4, pad=3, weight=1)
	mainframe.rowconfigure(5, pad=3, weight=1)
	mainframe.rowconfigure(6, pad=3, weight=1)
	mainframe.rowconfigure(7, pad=3, weight=1)
	mainframe.rowconfigure(8, pad=3, weight=1)
	mainframe.rowconfigure(9, pad=3, weight=1)
	mainframe.rowconfigure(10, pad=3, weight=1)
	mainframe.rowconfigure(11, pad=3, weight=1)
	mainframe.rowconfigure(12, pad=3, weight=1)
	mainframe.rowconfigure(13, pad=3, weight=1)
	mainframe.rowconfigure(14, pad=3, weight=1)
	mainframe.rowconfigure(15, pad=3, weight=1)

	getRecipeLabel = Label(allframe, text='Enter AllRecipes URL: ')
	getRecipeLabel.grid(row=0, column=0, columnspan=3)
	urlEntry = Entry(allframe)
	urlEntry.grid(row=0, column=3, columnspan=6)
	urlButton = Button(allframe, text='Parse')
	urlButton.grid(row=0, column=9, columnspan=2)
	urlButton.bind('<Button-1>', parseRecipe)
	root.mainloop()

def fillGui(root, url):
	recDict = representRecipe(url)
	stepBool = 0

	titleLabel = Label(root, text=recDict['recipe_name'])
	titleLabel.grid(row=1, column=0, columnspan=4)
	toolsLabel = Label(root, text='Tools Used:')
	toolsLabel.grid(row=2, column=0, columnspan=2)
	methodsLabel = Label(root, text='Methods Used:')
	methodsLabel.grid(row=2, column=2, columnspan=2)
	ingredsLabel = Label(root, text='Ingredients Used:')
	ingredsLabel.grid(row=2, column=4, columnspan=3)

	def showIngredLabel(event):
		for widget in ingredTextFrame.winfo_children():
			widget.destroy()

		for ingred in recDict['ingredients']:
			if ingred['name'] == event.widget['text']:
				fillIngredLabel(ingredTextFrame, ingred)
				return

	def leftStep(event):
		global stepBool 
		stepBool = 1
		for widget in stepFrame.winfo_children():
			widget.destroy()

		num = int(stepTextVar.get()) - 1
		if num == 0:
			num = len(recDict['steps'])
		fillStep(stepFrame, recDict['steps'][num-1], rowOffset)
		stepTextVar.set(str(num))

	def rightStep(event):
		global stepBool
		stepBool = 1
		for widget in stepFrame.winfo_children():
			widget.destroy()

		num = int(stepTextVar.get()) + 1
		if num > len(recDict['steps']):
			num = 1
		fillStep(stepFrame, recDict['steps'][num-1], rowOffset)
		stepTextVar.set(str(num))

	def stepChange(a, b, c):
		global stepBool
		if stepBool == 1:
			stepBool = 0
		else:
			for widget in stepFrame.winfo_children():
				widget.destroy()
			try:
				num = int(stepTextVar.get())
			except ValueError:
				num = 1
			if num <= 0:
				num = 1
			if num > len(recDict['steps']):
				num = len(recDict['steps'])
			fillStep(stepFrame, recDict['steps'][num-1], rowOffset)

	if len(recDict['cooking tools']) > 10:
		rowOffset = (len(recDict['cooking tools']) - 9)/2
	elif len(recDict['cooking methods']) > len(recDict['cooking tools']) and len(recDict['cooking methods']) > 10:
		rowOffset = (len(recDict['cooking methods']) - 9)/2
	else:
		rowOffset = 0

	for i in xrange(len(recDict['cooking tools'])):
		textString = '-' + recDict['cooking tools'][i]
		toolLabel = Label(root, text=textString)
		toolLabel.grid(row=(i/2) + 3, column=i%2)

	for i in xrange(len(recDict['cooking methods'])):
		textString = '-' + recDict['cooking methods'][i]
		methLabel = Label(root, text=textString)
		methLabel.grid(row=(i/2) + 3, column=(i%2) + 2)

	if len(recDict['ingredients']) > (18 + (3 * rowOffset)):	
		rowOffset = (len(recDict['ingredients']) - (16 + (3 * rowOffset)))/3

	textString = 'primary cooking method: ' + recDict['primary cooking method']
	primLabel = Label(root, text=textString)
	primLabel.grid(row=8 + rowOffset, column=0, columnspan=4)

	for i in xrange(len(recDict['ingredients'])):
		ingButton = Button(root, text=recDict['ingredients'][i]['name'])
		ingButton.grid(row=(i/3)+3, column=(i%3) + 4)
		ingButton.bind('<Button-1>', showIngredLabel)

	ingredTextFrame = Frame(root)
	ingredTextFrame.grid(row=2, column=7, rowspan=7, columnspan=3)

	stepFrame = Frame(root)
	stepFrame.grid(row=10+rowOffset, column=0, columnspan=10, rowspan=6)
	leftButton = Button(root, text='<')
	leftButton.grid(row=9+rowOffset, column=3)
	leftButton.bind('<Button-1>', leftStep)
	stepLabel = Label(root, text=' Step ')
	stepLabel.grid(row=9+rowOffset, column=4)

	stepTextVar = StringVar()
	stepTextVar.set('1')
	stepEntry = Entry(root, textvariable=stepTextVar)
	stepEntry.grid(row=9+rowOffset, column=5)
	stepTextVar.trace('w', stepChange)

	textString = ' of ' + str(len(recDict['steps'])) + ' '
	ofLabel = Label(root, text=textString)
	ofLabel.grid(row=9+rowOffset, column=6)
	rightButton = Button(root, text='>')
	rightButton.grid(row=9+rowOffset, column=7)
	rightButton.bind('<Button-1>', rightStep)

	fillStep(stepFrame, recDict['steps'][0], rowOffset)


def fillIngredLabel(root, inDict):
	nameLabel = Label(root, text=inDict['name'])
	nameLabel.grid(row=2, column=7, columnspan=3)

	descLabel = Label(root, text='Descriptor: ' + inDict['descriptor'])
	descLabel.grid(row=3, column=7, columnspan=3)

	prepLabel = Label(root, text='Preparationin: ' + inDict['preparation'])
	prepLabel.grid(row=4, column=7, columnspan=3)

	prepDescLabel = Label(root, text='Prep Description: ' + inDict['prep-description'])
	prepDescLabel.grid(row=5, column=7, columnspan=3)

	quantLabel = Label(root, text='Quantity: ' + inDict['quantity'])
	quantLabel.grid(row=6, column=7, columnspan=3)

	measLabel = Label(root, text='Measurement: ' + inDict['measurement'])
	measLabel.grid(row=7, column=7, columnspan=3)

	sizeLabel = Label(root, text='Size ' + inDict['size'])
	sizeLabel.grid(row=8, column=7, columnspan=3)

def fillStep(root, stepDict, rowOffset):
	stepLabel = Label(root, text='Step: ' + stepDict['step'])
	stepLabel.grid(row=10+rowOffset, column=0, columnspan=10)

	if 'time' in stepDict.keys():
		timeLabel = Label(root, text='Time: ' + stepDict['time'])
		timeLabel.grid(row=11+rowOffset, column=0, columnspan=10)
		rowOffset += 1


	ingredLabel = Label(root, text='Ingredients Used: ')
	ingredLabel.grid(row=11+rowOffset, column=0, columnspan=4)
	for i in xrange(len(stepDict['ingredients used'])):
		textString = '-' + stepDict['ingredients used'][i]
		ingLabel = Label(root, text=textString)
		ingLabel.grid(row=(i/4)+12+rowOffset, column=i%4)

	toolLabel = Label(root, text='Tools Used: ')
	toolLabel.grid(row=11+rowOffset, column=4, columnspan=3)
	for i in xrange(len(stepDict['tools_used'])):
		textString = '-' + stepDict['tools_used'][i]
		toLabel = Label(root, text=textString)
		toLabel.grid(row=(i/3)+12+rowOffset, column=(i%3)+4)

	methLabel = Label(root, text='Methods Used: ')
	methLabel.grid(row=11+rowOffset, column=7, columnspan=3)
	for i in xrange(len(stepDict['methods_used'])):
		textString = '-' + stepDict['methods_used'][i]
		meLabel = Label(root, text=textString)
		meLabel.grid(row=(i/3)+12+rowOffset, column=(i%3)+7)



makeGui()