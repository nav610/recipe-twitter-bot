from recipeDefn import initRecipe

file = open("AllRecipes.txt","r+")

line_blank_strip = []
for line in file: 
	print(line)
	if line.rstrip(): 
		line_blank_strip.append(line.strip())


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



### go through the file and consider everything in * Exported to * Exported as one recipe
### make recipe object with certain fields and fill those fields in 
### use recipe object to make a pure txt file with everything stripped and tweet ready 
### go line by line and tweet each recipe 

