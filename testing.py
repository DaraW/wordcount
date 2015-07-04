import functions2
text = functions2.wordTools()
text = text.fileToString("someText.txt")


######## VOWEL COUNT ########
vowels = ("a", "e", "i", "o", "u")
vcount = 0
for letter in text:
    if (letter.lower() in vowels):    #####program takes each letter, converts it to lower case and counts it
        vcount = vcount + 1
        
        
######## CONSONANT COUNT ########
consonants = ("b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z")
ccount = 0
for letter in text:
    if (letter.lower() in consonants):    #####program takes each letter, converts it to lower case and counts it
        ccount = ccount + 1
        
        
######## SENTENCE COUNT ########
sentence = ("?",".",)
scount = 0
for letter in text:
    if (letter in sentence):    
        scount = scount + 1
        
        
######## WORD COUNT ########
words = (" ")
wcount = 1
for letter in text:
    if (letter in words):    
        wcount = wcount + 1


######## AVERAGE WORD LENGTH ########
characters = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
words = (" ")
chcount =float(0)
wcount =float(0)
for letter in text:
    if (letter.lower() in characters):
        chcount = chcount + 1  
    elif (letter in words):    
        wcount = wcount + 1
averageWLen = '%.2f' %(chcount/wcount)


######## AVERAGE SENTENCE LENGTH ########
characters = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
sentences = (".""?")
chcount =float(0)
scount =float(0)
for letter in text:
    if (letter.lower() in characters):
        chcount = chcount + 1  
    elif (letter in sentences):    
        scount = scount + 1
averageSLen = '%.2f' %(chcount/scount)

print vcount
print ccount
print scount
print wcount
print chcount, "(character count)"
print averageWLen
print averageSLen

print "SUCCESS!"



######## DIFFERENT AVERAGE WORD LENGTH & AVERAGE SENTENCE LENGTH FUNCTIONS ########
#words = text.split()
#avgWLen = sum(len(word) for word in words)/len(words)

#sentences = text.split(".") ###### .split() - splits the textfile into it's individual components based on "."
#avg_Len = sum(len(x.split()) for x in  sentences) / len( sentences)
     

#print words
#print avgWLen
#print avg_Len