# Team 11's NLP Recipe Project

### How to Run:

Run RecipeGui.py to launch gui. This will allow for an allrecipes link to be submitted to be parsed and transformed.

Alternatively, running recipe.py and uncommenting either the file dump line or the print line and copying the url into the url variable will allow for either creating a json file for the parsed recipe, or will print the parsed recipe. 

The file that does the recipe transformation is called transformation2.py. This file contains lists of ingredients that can be switched with each other. For example, if the user wanted to make a meal vegan, we would find the ingredients in the recipe that are in our list of meats and switch each of those ingredients with an ingredients from our vegan list

### Libraries Used:
This project requires the installation of BeautifulSoup4 to run. In order to do so, you can do run one of the below options depending on your operating system or installed software:

`$ apt-get install python-bs4`

`$ easy_install beautifulsoup4`

`$ pip install beautifulsoup4`

Or, you can install the package directly by downloading a tar file from [this link](http://www.crummy.com/software/BeautifulSoup/bs4/download/4.0/) and then running `$ python setup.py install` from the directory. 

