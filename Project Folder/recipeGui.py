from Tkinter import Tk, W, E, BOTH, N, S, Button, Entry, StringVar, Frame, Label
import urllib2
import tkFont
from recipe import representRecipe
import transformation2

fillers = ['or', 'the', 'and', 'to', 'of', 'in', 'a']

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



	root.columnconfigure(0, pad=3, weight=1)
	root.columnconfigure(1, pad=3, weight=1)
	root.columnconfigure(2, pad=3, weight=1)
	root.columnconfigure(3, pad=3, weight=1)
	root.columnconfigure(4, pad=3, weight=1)
	root.columnconfigure(5, pad=3, weight=1)
	root.columnconfigure(6, pad=3, weight=1)
	root.columnconfigure(7, pad=3, weight=1)
	root.columnconfigure(8, pad=3, weight=1)
	root.columnconfigure(9, pad=3, weight=1)

	root.rowconfigure(0, pad=3, weight=1)
	root.rowconfigure(1, pad=3, weight=1)
	root.rowconfigure(2, pad=3, weight=1)
	root.rowconfigure(3, pad=3, weight=1)
	root.rowconfigure(4, pad=3, weight=1)
	root.rowconfigure(5, pad=3, weight=1)
	root.rowconfigure(6, pad=3, weight=1)
	root.rowconfigure(7, pad=3, weight=1)
	root.rowconfigure(8, pad=3, weight=1)
	root.rowconfigure(9, pad=3, weight=1)
	root.rowconfigure(10, pad=3, weight=1)
	root.rowconfigure(11, pad=3, weight=1)
	root.rowconfigure(12, pad=3, weight=1)
	root.rowconfigure(13, pad=3, weight=1)
	root.rowconfigure(14, pad=3, weight=1)
	root.rowconfigure(15, pad=3, weight=1)

	getRecipeLabel = Label(allframe, text='Enter AllRecipes URL: ')
	getRecipeLabel.grid(row=0, column=0)
	urlEntry = Entry(allframe)
	urlEntry.grid(row=0, column=1)
	urlButton = Button(allframe, text='Parse')
	urlButton.grid(row=0, column=2)
	urlButton.bind('<Button-1>', parseRecipe)

	root.mainloop()

def fillGui(root, url, **keyArguments):
	titleFont = tkFont.Font(weight='bold', size=10)

	if 'newRecipe' in keyArguments.keys():
		recDict = keyArguments['newRecipe']
	else:
		recDict = representRecipe(url)
	stepBool = 0

	def transformRecipe(event):
		transformSplit = event.widget['text'].split(' ')
		transformSplit[0] = transformSplit[0].lower()
		func_name = getattr(transformation2, ''.join(transformSplit))
		finalTuple = func_name(recDict)
		toolFrame.grid_forget()
		methFrame.grid_forget()
		ingredFrame.grid_forget()
		ingredTextFrame.grid_forget()
		fullStepFrame.grid_forget()
		try:
			replaceFrame.grid_forget()
		except NameError:
			pass
		fillGui(root, url, newRecipe=recDict, replacedList=finalTuple)


	lactoseButton = Button(root, text='Make Lactose Free')
	lactoseButton.grid(row=0, column=3, sticky=N+E+W+S)
	lactoseButton.bind('<Button-1>', transformRecipe)

	calButton = Button(root, text='Make Low Cal')
	calButton.grid(row=0, column=4, sticky=N+E+W+S)
	calButton.bind('<Button-1>', transformRecipe)

	carbButton = Button(root, text='Make Low Carb')
	carbButton.grid(row=0, column=5, sticky=N+E+W+S)
	carbButton.bind('<Button-1>', transformRecipe)

	fatButton = Button(root, text='Make Low Fat')
	fatButton.grid(row=0, column=6, sticky=N+E+W+S)
	fatButton.bind('<Button-1>', transformRecipe)

	pescButton = Button(root, text='Make Pescatarian')
	pescButton.grid(row=0, column=7, sticky=N+E+W+S)
	pescButton.bind('<Button-1>', transformRecipe)

	vegButton = Button(root, text='Make Vegetarian')
	vegButton.grid(row=0, column=8, sticky=N+E+W+S)
	vegButton.bind('<Button-1>', transformRecipe)

	veganButton = Button(root, text='Make Vegan')
	veganButton.grid(row=1, column=3, sticky=N+E+W+S)
	veganButton.bind('<Button-1>', transformRecipe)

	mexButton = Button(root, text='Make Mexican')
	mexButton.grid(row=1, column=4, sticky=N+E+W+S)
	mexButton.bind('<Button-1>', transformRecipe)

	itButton = Button(root, text='Make Italian')
	itButton.grid(row=1, column=5, sticky=N+E+W+S)
	itButton.bind('<Button-1>', transformRecipe)

	japButton = Button(root, text='Make Japanese')
	japButton.grid(row=1, column=6, sticky=N+E+W+S)
	japButton.bind('<Button-1>', transformRecipe)

	indButton = Button(root, text='Make Indian')
	indButton.grid(row=1, column=7, sticky=N+E+W+S)
	indButton.bind('<Button-1>', transformRecipe)

	chiButton = Button(root, text='Make Chinese')
	chiButton.grid(row=1, column=8, sticky=N+E+W+S)
	chiButton.bind('<Button-1>', transformRecipe)

	titleLabel = Label(root, text=recDict['recipe_name'], font=titleFont)
	titleLabel.grid(row=1, column=0, columnspan=3)

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

	toolFrame = Frame(root, borderwidth=5, bg='#ffffff', bd=10)
	toolFrame.grid(row=2, column=0, columnspan=2, rowspan=(((len(recDict['cooking tools']) - 1)/2) + 2))
	toolsLabel = Label(toolFrame, text='Tools Used:', bg='#ffffff', font=titleFont)
	toolsLabel.grid(row=2, column=0, columnspan=2)
	for i in xrange(len(recDict['cooking tools'])):
		textString = '-' + recDict['cooking tools'][i]
		toolLabel = Label(toolFrame, text=textString, bg='#ffffff')
		toolLabel.grid(row=(i/2) + 3, column=i%2)

	methFrame = Frame(root, borderwidth=5, bg='#ffffff', bd=10)
	methFrame.grid(row=2, column=2, columnspan=2, rowspan=(((len(recDict['cooking methods']) - 1)/2) + 2))
	methodsLabel = Label(methFrame, text='Methods Used:', bg='#ffffff', font=titleFont)
	methodsLabel.grid(row=2, column=2, columnspan=2)
	for i in xrange(len(recDict['cooking methods'])):
		textString = '-' + recDict['cooking methods'][i]
		methLabel = Label(methFrame, text=textString, bg='#ffffff')
		methLabel.grid(row=(i/2) + 3, column=(i%2) + 2)

	if len(recDict['ingredients']) > (18 + (3 * rowOffset)):	
		rowOffset = (len(recDict['ingredients']) - (16 + (3 * rowOffset)))/3

	primFrame = Frame(root, bg='#ffffff', bd=10)
	primFrame.grid(row=5+rowOffset, column=0, columnspan=4, rowspan=2)
	primLabel = Label(primFrame, text='Primary Cooking Method: ', bg='#ffffff', font=titleFont)
	primLabel.grid(row=5 + rowOffset, column=0, columnspan=4)
	primaLabel = Label(primFrame, text=recDict['primary cooking method'], bg='#ffffff')
	primaLabel.grid(row=6+rowOffset, column=0, columnspan=4)

	if 'replacedList' in keyArguments.keys():
		replaceList = keyArguments['replacedList']
		replaceFrame = Frame(root, bg='#ffffff')
		replaceFrame.grid(row=7+rowOffset, column=0, columnspan=3, rowspan=7)
		replTitleLabel = Label(replaceFrame, bg='#ffffff', text='Changed Ingredients', font=titleFont)
		replTitleLabel.grid(row=7+rowOffset, column=0, columnspan=3, sticky=N)
		for i in xrange(len(replaceList)):
			repLabel = Label(replaceFrame, bg='#ffffff', text='-' +replaceList[i][0] + ' was replaced by ' +replaceList[i][1])
			repLabel.grid(row=i + 8 + rowOffset, column=0, columnspan=3, sticky=W)

	ingredFrame = Frame(root, borderwidth=5, bg='#ffffff')
	ingredFrame.grid(row=2, column=4, columnspan=3, rowspan=(((len(recDict['ingredients']) - 1)/3) + 2))
	ingredsLabel = Label(ingredFrame, text='Ingredients Used:', bg='#ffffff', font=titleFont)
	ingredsLabel.grid(row=2, column=4, columnspan=3)
	for i in xrange(len(recDict['ingredients'])):
		ingButton = Button(ingredFrame, text=recDict['ingredients'][i]['name'])
		ingButton.grid(row=(i/3)+3, column=(i%3) + 4, sticky=N+E+S+W)
		ingButton.bind('<Button-1>', showIngredLabel)

	ingredTextFrame = Frame(root, bg='#ffffff')
	ingredTextFrame.grid(row=2, column=7, rowspan=7, columnspan=3)

	fullStepFrame = Frame(root, bg='#ffffff')
	fullStepFrame.grid(row=9+rowOffset, column=3, columnspan=7, rowspan=7, sticky=N)

	stepFrame = Frame(fullStepFrame, bg='#ffffff')
	stepFrame.grid(row=10+rowOffset, column=3, columnspan=7, rowspan=6)
	leftButton = Button(fullStepFrame, text='<')
	leftButton.grid(row=9+rowOffset, column=4)
	leftButton.bind('<Button-1>', leftStep)
	stepLabel = Label(fullStepFrame, text=' Step ', bg='#ffffff')
	stepLabel.grid(row=9+rowOffset, column=5)

	stepTextVar = StringVar()
	stepTextVar.set('1')
	stepEntry = Entry(fullStepFrame, textvariable=stepTextVar, width=5)
	stepEntry.grid(row=9+rowOffset, column=6)
	stepTextVar.trace('w', stepChange)

	textString = ' of ' + str(len(recDict['steps'])) + ' '
	ofLabel = Label(fullStepFrame, text=textString, bg='#ffffff')
	ofLabel.grid(row=9+rowOffset, column=7)
	rightButton = Button(fullStepFrame, text='>')
	rightButton.grid(row=9+rowOffset, column=8)
	rightButton.bind('<Button-1>', rightStep)

	fillStep(stepFrame, recDict['steps'][0], rowOffset)


def fillIngredLabel(root, inDict):
	titleFont = tkFont.Font(weight='bold', size=10)

	nameLabel = Label(root, text=capit(inDict['name']), font=titleFont, bg='#ffffff')
	nameLabel.grid(row=2, column=7, columnspan=3)

	descLabel = Label(root, text='Descriptor: ' + inDict['descriptor'], bg='#ffffff')
	descLabel.grid(row=3, column=7, columnspan=3)

	prepLabel = Label(root, text='Preparationin: ' + inDict['preparation'], bg='#ffffff')
	prepLabel.grid(row=4, column=7, columnspan=3)

	prepDescLabel = Label(root, text='Prep Description: ' + inDict['prep-description'], bg='#ffffff')
	prepDescLabel.grid(row=5, column=7, columnspan=3)

	quantLabel = Label(root, text='Quantity: ' + inDict['quantity'], bg='#ffffff')
	quantLabel.grid(row=6, column=7, columnspan=3)

	measLabel = Label(root, text='Measurement: ' + inDict['measurement'], bg='#ffffff')
	measLabel.grid(row=7, column=7, columnspan=3)

	sizeLabel = Label(root, text='Size ' + inDict['size'], bg='#ffffff')
	sizeLabel.grid(row=8, column=7, columnspan=3)

def fillStep(root, stepDict, rowOffset):
	titleFont = tkFont.Font(weight='bold', size=10)

	stepLabel = Label(root, text='Step: ' + stepDict['step'], bg='#ffffff')
	stepLabel.grid(row=10+rowOffset, column=3, columnspan=7)

	if 'time' in stepDict.keys():
		timeLabel = Label(root, text='Time: ' + stepDict['time'], bg='#ffffff')
		timeLabel.grid(row=11+rowOffset, column=3, columnspan=7)
		rowOffset += 1

	inFrame = Frame(root, bg='#d1cdcd', bd=15)
	inFrame.grid(row=11+rowOffset, column=3, columnspan=3, rowspan=3)
	ingredLabel = Label(inFrame, text='Ingredients Used: ', bg='#d1cdcd', font=titleFont)
	ingredLabel.grid(row=11+rowOffset, column=3, columnspan=3)
	for i in xrange(len(stepDict['ingredients used'])):
		textString = '-' + stepDict['ingredients used'][i]
		ingLabel = Label(inFrame, text=textString, bg='#d1cdcd')
		ingLabel.grid(row=(i/3)+12+rowOffset, column=(i%3) + 3)

	toolFrame = Frame(root, bg='#d1cdcd', bd=15)
	toolFrame.grid(row=11+rowOffset, column=6, columnspan=2, rowspan=3)
	toolLabel = Label(toolFrame, text='Tools Used: ', bg='#d1cdcd', font=titleFont)
	toolLabel.grid(row=11+rowOffset, column=6, columnspan=2)
	for i in xrange(len(stepDict['tools_used'])):
		textString = '-' + stepDict['tools_used'][i]
		toLabel = Label(toolFrame, text=textString, bg='#d1cdcd')
		toLabel.grid(row=(i/2)+12+rowOffset, column=(i%2)+6)

	methFrame = Frame(root, bg='#d1cdcd', bd=15)
	methFrame.grid(row=11+rowOffset, column=8, columnspan=2, rowspan=3)
	methLabel = Label(methFrame, text='Methods Used: ', bg='#d1cdcd', font=titleFont)
	methLabel.grid(row=11+rowOffset, column=8, columnspan=2)
	for i in xrange(len(stepDict['methods_used'])):
		textString = '-' + stepDict['methods_used'][i]
		meLabel = Label(methFrame, text=textString, bg='#d1cdcd')
		meLabel.grid(row=(i/2)+12+rowOffset, column=(i%2)+8)

def capit(strg):
	strArr = strg.split(' ')
	startingStr = strArr[0].capitalize()
	del strArr[0]
	newArr = map(lambda x: x.capitalize() if x not in fillers else x, strArr)
	newArr.insert(0, startingStr)
	return ' '.join(newArr)

makeGui()