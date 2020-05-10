#reads the file name, ignores any line with #, and retrieves all words and scores from the lines that contain "#a" in parts[0], which parts = line.split("\t")
#once we have the words and scores from parts[0] and parts[1], we then store the word and score inside of a dictionary called adjectives_dictionary.
#we add the dictionary properties for every line that does not contain "#" and must contain "#a" in parts[0]. This value is then returned at the end of the function.

def read_sentiments(file_name):
	adjectives_dictonary = {}
	word = []
	score = []

	my_file = open(file_name,"r")
	for line in my_file:
		line = line.strip()
		parts = line.split("\t")

		if line[0] != "#" and "#a" in parts[0]:
			word = parts[0]
			word = word.replace("#a","")
			score = float(parts[1])
			adjectives_dictonary[word] = score
	my_file.close()
	return adjectives_dictonary
#remove_punct will take in a string, whill place the value into the remove_punctuation variable; This initialization occurs in case the string does not need to be modified and removed of any 
#punctuation. The string to take in, "punct_word", will then be splitted into an array to loop through each index of the array and to modify the index in case there is punctuation.
#once the string is modified if it occurs, then we join back the punct_word into a string. This will be stored in removed_punctuation in the return statement.

def remove_punct(punct_word):
	removed_punctuation = punct_word
	punct_word = punct_word.split(" ")
	for index in range(len(punct_word)):	
		if ',' in punct_word[index]:
			punct_word[index] = punct_word[index].replace(",","")
		elif '.' in punct_word[index]:
			punct_word[index] = punct_word[index].replace(".","")
		removed_punctuation = " ".join(punct_word)
	return removed_punctuation

#analyze_text will take in the string after removing any punctuation and the adjectives dictionary. 
#sentiment_score_list, word, multiplier_list, contribute_list,  are all variables initialized to an empty list, which will contain all the scores, words, multipliers, contribution
#in respective order. This is achieved with the append method for each iteration.
#multiplier, total_contribute are initialized to 0, and for each iteration inside of the loop, multiplier will be initialized depending on the if statement and total_contribute
#will keep on adding the values for each specific case to hold the end total of contribution to display. All these variables will get returned at the end.

def analyze_text(removed_punctuation, adjectives_dictonary):
	sentiment_score_list = [] 
	text = removed_punctuation.split(" ")
	word = []
	for element in text:
		if element in adjectives_dictonary:
			sentiment_score_list.append(adjectives_dictonary[element])
			word.append(element)

	multiplier = 0
	multiplier_list = []
	contribute_list = []
	total_contribute = 0

	for index, element in enumerate(text):
		if element in word:
			
			if text[index - 1] == "really" or text[index - 1] == "very" or text[index - 1] == "totally" or text[index - 1] == "extremely" or text[index - 1] == "super":
				multiplier = 2
				multiplier_list.append(multiplier)
				contribute_list.append(adjectives_dictonary[element] * multiplier)
				total_contribute += adjectives_dictonary[element] * multiplier

			elif text[index - 1] == "slightly" or text[index - 1] == "pretty" or text[index - 1] == "mildly" or text[index - 1] == "somewhat":
				multiplier = 0.5
				multiplier_list.append(multiplier)
				contribute_list.append(adjectives_dictonary[element] * multiplier)
				total_contribute += adjectives_dictonary[element] * multiplier

			elif text[index -1] == "too":
				multiplier = -0.5
				multiplier_list.append(multiplier)
				contribute_list.append(adjectives_dictonary[element] * multiplier)
				total_contribute += adjectives_dictonary[element] * multiplier


			elif text[index - 1] == "not" or text[index - 2] == "not":
				multiplier = -1
				multiplier_list.append(multiplier)
				contribute_list.append(adjectives_dictonary[element] * multiplier)
				total_contribute += adjectives_dictonary[element] * multiplier

			else:
				multiplier = 1
				multiplier_list.append(multiplier)
				contribute_list.append(adjectives_dictonary[element] * multiplier)
				total_contribute += adjectives_dictonary[element] * multiplier


	return sentiment_score_list, word, multiplier_list, contribute_list, total_contribute

#judge_sentiment will take in the total_contribute and check whether the result is positive, slightly positive, etc. It will then return the result to later display.
def judge_sentiment(total_contribute):
	result = ""
	if total_contribute > 0.5:
		result = "positive"
	elif total_contribute > 0 and total_contribute < 0.5:
		result = "slightly positive"
	elif total_contribute == 0:
		result = "neutral"
	elif total_contribute < 0 and total_contribute > -0.5:
		result = "slightly negative"
	else:
		result = "negative" 
	return result

#analyze_file will take in the file_name, file_to_analyze retrieved by user input, then inside of the function, will retrieve the adjectives_dictionary using the file_name.
#my_file will open and contain access to file_to_analyze as "read." words, scores, multiplier_list, contribute_list are all lists that will append the respective values for each iteration.
#total_contribute will add the values of each contribution of each iteration onto itself to hold the total.
#text is at first initialized to an empty string, but gets reassigned to the line of the file, but having the line remove of any punctuation by placing the line inside of the remove_punct.
#the text is then splitted, so that we can loop through each word in the line and check if it is inside the adjectives_dictionary.
#after the iterations, we find the result by passing total_contribute as an argument to judge_sentiment.
#after retrieving all the data for each iteration, the analysis function gets called with scores, words, multiplier_list, contribute_list and results. It will then print the date to the user.
def analyze_file(file_name, file_to_analyze):
	adjectives_dictonary = read_sentiments(file_name)
	my_file = open(file_to_analyze,"r")
	words = []
	scores = []
	multiplier_list = []
	contribute_list = []
	total_contribute = 0
	text = ""
	for line in my_file:
		line = line.strip()
		text = remove_punct(line).lower()
		text = text.split(" ")

		for element in text:
			if element in adjectives_dictonary and adjectives_dictonary[element] != 0:
				words.append(element)
				scores.append(adjectives_dictonary[element])

		for index, element in enumerate(text):
			if element in words:

				if text[index - 1] == "really" or text[index - 1] == "very" or text[index - 1] == "totally" or text[index - 1] == "extremely" or text[index - 1] == "super":
					multiplier = 2
					multiplier_list.append(multiplier)
					contribute_list.append(adjectives_dictonary[element] * multiplier)
					total_contribute += adjectives_dictonary[element] * multiplier

				elif text[index - 1] == "slightly" or text[index - 1] == "pretty" or text[index - 1] == "mildly" or text[index - 1] =="somewhat":
					multiplier = 0.5
					multiplier_list.append(multiplier)
					contribute_list.append(adjectives_dictonary[element] * multiplier)
					total_contribute += adjectives_dictonary[element] * multiplier

				elif text[index -1] == "too":
					multiplier = -0.5
					multiplier_list.append(multiplier)
					contribute_list.append(adjectives_dictonary[element] * multiplier)
					total_contribute += adjectives_dictonary[element] * multiplier

				elif text[index - 1] == "not" or text[index - 2] == "not":
					multiplier = -1
					multiplier_list.append(multiplier)
					contribute_list.append(adjectives_dictonary[element] * multiplier)
					total_contribute += adjectives_dictonary[element] * multiplier

				else:
					multiplier = 1
					multiplier_list.append(multiplier)
					contribute_list.append(adjectives_dictonary[element] * multiplier)
					total_contribute += adjectives_dictonary[element] * multiplier

	my_file.close()
	result = judge_sentiment(total_contribute)	
	analysis(scores, words, multiplier_list, contribute_list, total_contribute, result)

#The analysis function will take in all the variables that will get printed for the user to see. It will loop through each list index at the length of word.
def analysis(sentiment_score_list, word, multiplier_list, contribute_list, total_contribute, result):
	print("{word:<10}{score:^10}{mult:^10}{contrib:>10}".format(word = "Word", score = "Score", mult = "Mult", contrib = "Contrib"))
	print("-" * 40)
	for index in range(len(word)):
		print(f"{word[index]:<10}{sentiment_score_list[index]:^10.4f}{multiplier_list[index]:^10.4f}{contribute_list[index]:>10.4f}")
	print()
	print(f"With a score of {total_contribute:1.4f}, the text is judged {result}.")
	print()