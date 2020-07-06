class recipe(): 
	def __init__(self):
		self.name = None 
		self.author = '' 
		self.size = '' 
		self.ingredeintList = ''
		self.stepsList = ''

def makeName(recipe,texts): 
	recipe.name = texts[1]


def makeSize(recipe,texts):
	for line in texts: 
		if 'Serving Size  :' in line:
			authorString = str(line)
			after_key = authorString.partition('Serving Size  :')[2]
			size = after_key.partition('Preparation Time')[0]
			recipe.size = int(size or None) 
			break 

def makeAuthor(recipe,texts): 
	for line in texts: 
		if 'Recipe By     :' in line: 
			authorString = str(line)
			author = authorString.partition('Recipe By     :')[2]
			if author != None: 
				recipe.author = author 
			break 

def makeIngredient(recipe,texts): 
	for line in texts:

		if 'Amount  Measure       Ingredient -- Preparation Method' == line: 
			startindex = texts.index(line) + 2

		if 'Nutr. Assoc. :' in line: 
			endindex = texts.index(line) - 2
			break 

	ingredeintList = [] 
	for line in texts[startindex:endindex]: 
		ingredeintList.append(" ".join(line.split()))

	stepsList = [] 
	for line in texts[endindex:endindex+1][0].split('.'): 

		stepsList.append(" ".join(line.split()))


	recipe.ingredeintList = ingredeintList
	recipe.stepsList = stepsList 

def unpackRecipe(obj): 
	unpacked = []

	unpacked.append(obj.name)
	#unpacked.append(obj.author)
	if obj.size != '': 
		size = "Serving Size: " + str(obj.size)
		unpacked.append(size)
	for line in obj.ingredeintList: 
		unpacked.append(line)
	for line in obj.stepsList: 
		unpacked.append(line)

	new_list = list(filter(None, unpacked))
	a, index = len(new_list), 0

	while index < a: 
		if len(new_list[index]) > 280: 
			new_list.insert(index+1, new_list[index][280:])
			new_list[index] = new_list[index][:280]
			a += 1
		index += 1
	
	return new_list


def initRecipe(texts): 
	Recipe = recipe()
	makeName(Recipe, texts)
	makeAuthor(Recipe, texts)
	makeIngredient(Recipe, texts)
	return Recipe






