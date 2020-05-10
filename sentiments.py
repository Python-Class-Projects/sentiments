from sentiments_Functions import *

#This file will contain the main program. The functions come from Henri_Alvarez_Sentiments_Functions.py
#It will first ask for the file name, to then later use inside of the read_sentiments function to create the dictionary containing all adjectives from the file read. 
#selection initially = 1 so that we can start the while loop as a true statement.
#then the application will print out a list of options for the user to select from. 
#the value will be stored inside of selection variable.
#if it is not = 3, then we know to run the selected choice.
#if the selection =1, then retrieve text to analyze, stored inside user_text.
#the remove_punct function is then used on the user_text to remove any punctuation.
#then retrieve our dictionary and run the read_sentiments on the file_name.
#next the text is analyzed and ran through the analyze_text function.
#from the analyze_text function, the list of sentiment scores, words, multiplier, contributions, and the accumulated contribution is retrieved to then print out.
#result variable is initialized with the value being a returned value from judge_sentiments, which has total_contribute as an argument to determine if it is +, -, etc.
#finally, for selection 1, the analysis is called, which prints out all the variables retrieved from the analyze_text and judge_sentiment functions. 
#for selection = 2, the file to analyze is retrieved.
#then the analyze_file function is called, which takes in the file_name and file_to_analyze
#if selection = 3, then we print a thank you and break out of the loop.

file_name = input("Enter name of sentiment words file: ")
selection = 1
while selection != 3:
	print("What would you like to do?")
	print("1. Analyze a single tweet")
	print("2. Analyze a file")
	print("3. Exit")
	selection = int(input("Enter the number of your choice: "))
	if selection == 1:
		user_text = input("Enter text to analyze: ")
		user_text = remove_punct(user_text)
		adjectives_dictonary = read_sentiments(file_name)
		sentiment_score_list, word, multiplier_list, contribute_list, total_contribute = analyze_text(user_text, adjectives_dictonary) 
		result = judge_sentiment(total_contribute)
		analysis(sentiment_score_list, word, multiplier_list, contribute_list, total_contribute, result)
	elif selection == 2:
		file_to_analyze = input("Enter name of file to analyze: ")
		analyze_file(file_name, file_to_analyze)
	elif selection == 3:
		print("Thank you for using this program.")
		break

