class wordTools:
    filename = 0
#### This function opens the text file
    def fileToString(self, filename):
        myFile = open(filename)
        myText  = ""
        for ch in myFile:
            myText = myText + ch
        return myText
       
        
######## AVERAGE SENTENCE LENGTH ####################################################################
######## THIS FUNCTION CALCULATES THE AMOUNT OF VOWELS IN THIS TEXT FILE ############################ 
        
    def vowelsCount(self, textfile):
        vowels = ("a", "e", "i", "o", "u")
        vcount = 0
        for letter in textfile:
            if (letter.lower() in vowels): #####program takes each letter, converts it to lower case and counts it
                vcount = vcount + 1        ##### For each letter scanned, 1 is added to the count
        return vcount

######## AVERAGE SENTENCE LENGTH ####################################################################
######## THIS FUNCTION CALCULATES THE AMOUNT OF CONSONANTS IN THIS TEXT FILE ########################  

    def consonantsCount(self,textfile):
        consonants = ("b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z")
        ccount = 0
        for letter in textfile:
            if (letter.lower() in consonants): #####program takes each letter, converts it to lower case and counts it   
                ccount = ccount + 1            ##### For each letter scanned, 1 is added to the count
        return ccount

######## AVERAGE SENTENCE LENGTH ####################################################################
######## THIS FUNCTION CALCULATES THE AMOUNT OF SENTENCES IN THIS TEXT FILE ######################### 
     
    def sentencesCount(self,textfile):
        sentence = ("?",".",)
        scount = 0
        for letter in textfile:
            if (letter in sentence):    
                scount = scount + 1  ##### For each character scanned, 1 is added to the count
        return scount

######## AVERAGE SENTENCE LENGTH ####################################################################
######## THIS FUNCTION CALCULATES THE AMOUNT OF WORDS IN THIS TEXT FILE ############################# 
      
    def wordCount(self,textfile):
        words = (" ")
        wcount = 1
        for letter in textfile:
            if (letter in words):    
                wcount = wcount + 1   ##### For each space scanned, 1 is added to the count
        return wcount

######## AVERAGE SENTENCE LENGTH #####################################################################
######## THIS FUNCTION CALCULATES THE AMOUNT OF QUESTIONS IN THIS TEXT FILE ########################## 
    
    def questionCount(self,textfile):
        questionmarks = ("?")
        qcount = 0
        for letter in textfile:
            if (letter in questionmarks):  ##### For each character scanned, 1 is added to the count 
                qcount = qcount + 1
        return qcount

######## AVERAGE WORD LENGTH #########################################################################
######## THIS FUNCTION CALCULATES THE AVERAGE CHARACTER LENGTH OF THE WORDS IN THIS TEXT FILE ########

    def averageWordLen(self,textfile):
        characters = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
        words = (" ")
        chcount =float(0)
        wcount =float(0)
        for letter in textfile:
            if (letter.lower() in characters): #####program takes each letter, converts it to lower case and counts it
                chcount = chcount + 1          ##### For each letter scanned, 1 is added to the count
            elif (letter in words):    
                wcount = wcount + 1
        averageWLen = '%.2f' %(chcount/wcount)
        return averageWLen
    
######## AVERAGE SENTENCE LENGTH ######################################################################
######## THIS FUNCTION CALCULATES THE AVERAGE CHARACTER LENGTH OF THE SENTENCES IN THIS TEXT FILE #####
    
    def averageSentenceLen(self,textfile):    
        characters = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
        sentences = (".""?")
        chcount =float(0)
        scount =float(0)
        for letter in textfile:
            if (letter.lower() in characters): #####program takes each letter, converts it to lower case and counts it
                chcount = chcount + 1  
            elif (letter in sentences):    
                scount = scount + 1
        averageSLen = '%.2f' %(chcount/scount)
        return averageSLen
    

