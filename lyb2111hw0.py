with open ('iowa-liquor-sample.csv') as liquors:
	counter = 0
	for line in liquors:
		lowerline = line.lower()
		if lowerline.find ("single malt scotch") != -1:
			counter += 1
	print (counter)
