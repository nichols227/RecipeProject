from Tkinter import Tk, W, E, BOTH, N, S, Button, Entry
from ttk import Style, Frame, Label
from PIL import Image, ImageTk
import tkFont
import recipe


exampleDict = {'cooking tools': ['oven', 'baking dish', 'bowl', 'aluminum foil', 'thermometer'], 'cooking methods': [u'sprinkle', u'mix', u'pour', u'bake'], 'ingredients': [{'name': u'chicken breast', 'preparation': 'none', 'descriptor': u'skinless and boneless', 'measurement': u'halves', 'quantity': u'4', 'prep-description': 'none', 'size': 'none'}, {'name': u'pepper flakes', 'preparation': u'red', 'descriptor': 'none', 'measurement': u'tablespoon', 'quantity': u'1', 'prep-description': 'none', 'size': 'none'}, {'name': u'honey', 'preparation': 'none', 'descriptor': 'none', 'measurement': u'cup', 'quantity': '.5', 'prep-description': 'none', 'size': 'none'}, {'name': u'mustard', 'preparation': 'none', 'descriptor': u'Dijon', 'measurement': u'cup', 'quantity': '.25', 'prep-description': 'none', 'size': 'none'}], 'steps': [{'tools_used': ['oven'], 'step': u'Preheat oven to 350 degrees F (175 degrees C).', 'ingredients used': [], 'methods_used': []}, {'tools_used': ['baking dish'], 'step': u'Place chicken breasts in a baking dish', 'ingredients used': [u'chicken breast'], 'methods_used': []}, {'tools_used': [], 'step': u'sprinkle with red pepper flakes', 'ingredients used': [u'pepper flakes'], 'methods_used': [u'sprinkle']}, {'tools_used': ['bowl'], 'step': u'Mix honey and mustard in a small bowl and pour mixture over chicken', 'ingredients used': [u'chicken breast', u'honey', u'mustard'], 'methods_used': [u'mix', u'pour']}, {'tools_used': ['aluminum foil', 'baking dish'], 'step': u'Cover baking dish with aluminum foil.', 'ingredients used': [], 'methods_used': []}, {'tools_used': ['oven'], 'step': u'Bake in the preheated oven until the juices run clear and chicken is no longer pink inside, about 40 minutes', 'ingredients used': [u'chicken breast'], 'methods_used': [u'bake'], 'time': u'40 minutes'}, {'tools_used': ['thermometer'], 'step': u'An instant-read meat thermometer inserted into the thickest part of a breast should read at least 160 degrees F (70 degrees C).', 'ingredients used': [u'chicken breast'], 'methods_used': []}], 'primary cooking method': u'bake'}


def makeGui():
	root = Tk()
	root.title("Recipe Parser")
	allframe = Frame(root)
	allframe.grid(column=0, row=0, sticky=(N, W, E, S))
	mainframe = Frame(allframe)
	mainframe.grid(column=0, row=1, sticky=(N, W, E, S))

	def parseRecipe(event):
		recipeUrl = urlEntry.get()
		try:
			urllib2.urlopen(recipeUrl)
		except ValueError:
			print "Invalid URL. Please Try Again"
			urlEntry.delete(0, END)
			return
		if recipeUrl.split('.')[1] != 'allrecipes':
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
	

makeGui()