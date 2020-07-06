from recipeDefn import initRecipe,unpackRecipe
from requests_oauthlib import OAuth1Session
from random import shuffle
#path = './recipe_txts/Cajun.rtf'
creds = open("creds.txt","r+").readlines()
session = OAuth1Session(creds[0].strip(),creds[1].strip(),creds[2].strip(),creds[3].strip())

file = open("AllRecipes.rtf","r+")

count = 0 
line_blank_strip = []
for line in file: 
	count += 1
	if line.rstrip(): 
		line_blank_strip.append(line.strip())

file.close() 

startOfRecipe, endOfRecipe = None, None 
recipes = []
for i in range(len(line_blank_strip)): 
	if '* Exported from MasterCook *' == line_blank_strip[i]: 
		startOfRecipe = i

	if 'Nutr. Assoc. : 0' == line_blank_strip[i]: 
		endOfRecipe = i + 1

	if startOfRecipe != None and endOfRecipe != None: 
		recipes.append(initRecipe(line_blank_strip[startOfRecipe:endOfRecipe])) 
		startOfRecipe, endOfRecipe = None, None



random_index = [i for i in range(len(recipes))]
shuffle(random_index)

#for i in random_index: 
recipe = recipes[10]
print(unpackRecipe(recipe))



#params = {'status':"Hello World!"}
url = "https://api.twitter.com/1.1/statuses/update.json"


