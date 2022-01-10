import json


with open("words.json") as f:
	data = json.load(f)
	
	model = [None]*len(data)
	prise = [None]*len(data)
	country = [None]*len(data)
	mark = [None]*len(data)
	description = [None]*len(data)
	link = [None]*len(data)
	
	for elem in data:
		model[elem['_id']] = elem["model"]
		prise[elem['_id']] = elem["prise"]
		country[elem['_id']] = elem["country"]
		mark[elem['_id']] = elem["mark"]
		description[elem['_id']] = elem["descripton"]
		link[elem['_id']] = elem["link"]
	
	print(model)
