
def makeName(recipe, texts): 
	recipe.name = texts[0]


def makeSize(recipe,texts):
	for line in texts: 
		if 'Serving Size  :' in line:
			authorString = str(line)
			after_key = authorString.partition('Serving Size  :')[2]
			size = after_key.partition('Preparation Time')[0]
			recipe.size = int(size or None) 
			break 

def makeAuthor(recipe, texts): 
	for line in texts: 
		if 'Recipe By     :' in line: 
			authorString = str(line)
			author = authorString.partition('Recipe By     :')[2]
			if author != None: 
				recipe.author = author 
			break 

def makeIngredient(recipe, texts): 
	for line in texts:

		if 'Amount  Measure       Ingredient -- Preparation Method' == line: 
			startindex = texts.index(line) + 2

		if 'Nutr. Assoc. :' in line: 
			endindex = texts.index(line) - 2
			break 

	ingredeintList = [] 
	for line in texts[startindex:endindex]: 
		ingredeintList.append(line)

	stepsList = [] 
	for line in texts[endindex:endindex+1][0].split('.'): 
		stepsList.append(line)


	recipe.ingredeintList = ingredeintList
	recipe.stepsList = stepsList 
