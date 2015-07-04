import functions2

text = functions2.wordTools() ##### Creates an object called text that inherits the wordTools class. 
text = text.fileToString("someText.txt") ### The object text calls the filetostring function and applies it to the "txt" file

######## VOWEL COUNT ########
vowelsC = functions2.wordTools()#### Creates the vowelsC object which copys/inherits properties or variables from the wordTools class 
vowelsC = vowelsC.vowelsCount(text) ##### The object vowelsC calls/uses/applies the vowelsCount function to the text object

######## CONSONANT COUNT ########
consonantsC = functions2.wordTools()
consonantsC = consonantsC.consonantsCount(text)

######## SENTENCE COUNT ########
sentencesC = functions2.wordTools()
sentencesC = sentencesC.sentencesCount(text)

######## WORD COUNT ########
wordC = functions2.wordTools()
wordC = wordC.wordCount(text)

######## QUESTION COUNT ########
questionC = functions2.wordTools() 
questionC = questionC.questionCount(text)

######## AVERAGE WORD LENGTH ########
averageWordLength = functions2.wordTools()
averageWordLength = averageWordLength.averageWordLen(text)

######## AVERAGE SENTENCE LENGTH ########
averageSentenceLength = functions2.wordTools()
averageSentenceLength = averageSentenceLength.averageSentenceLen(text)

print "Results can printed to the screen by selecting option 1 or the results can be printed to a separte file by selecting option 2"

option = raw_input("Please select Option: ")
print "\n"

######## PRINT TO SCREEN ########
if (option=="1"):
    print text
    print "\n"
    print "There are", vowelsC,  "vowels in this text file"
    print "There are", consonantsC, "consonants in this text file"
    print "There are", sentencesC, "sentences in this text file"
    print "There are", wordC,  "words in this text file"
    print "There are", questionC, "questions in this text file"
    print "There are on average", averageWordLength, "characters in each word"
    print "There are on average", averageSentenceLength, "characters in each sentence"
    
######## PRINT TO FILE ########
elif (option =="2"):
    outFile = open("outputFile.txt","w")
    outFile.write("There are ")
    outFile.write(str(vowelsC))
    outFile.write(" vowels in this text file")
    outFile.write("\n")
    outFile.write("There are ")
    outFile.write(str(consonantsC))
    outFile.write(" consonants in this text file")
    outFile.write("\n")
    outFile.write("There are ")
    outFile.write(str(sentencesC))
    outFile.write(" sentences in this text file")
    outFile.write("\n")
    outFile.write("There are ")
    outFile.write(str(wordC))
    outFile.write(" words in this text file")
    outFile.write("\n")
    outFile.write("There are ")
    outFile.write(str(questionC))
    outFile.write(" questions in this text file")
    outFile.write("\n")
    outFile.write("There are on average ")
    outFile.write(str(averageWordLength))
    outFile.write(" characters in each word")
    outFile.write("\n")
    outFile.write("There are on average ")
    outFile.write(str(averageSentenceLength))
    outFile.write(" characters in each sentence")
    outFile.write("\n")
    outFile.write("End of Program")
    outFile.close()
    





