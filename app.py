#import files
import pyttsx3
from speechrec import *
import nltk
from nltk.corpus import stopwords

#declaration
engine = pyttsx3.init()
name='robo'
sound = engine.getProperty('voices')
stop_words = stopwords.words('english')
# print(stop_words)
#functions
def speak(ans):
	engine.say(ans)
	engine.runAndWait()
def dataProcessing(text):

	tokens = nltk.word_tokenize(text)
	print (tokens)

	tokensWithOutStopWords = []
	for word in tokens:
		if word not in stop_words:
			tokensWithOutStopWords.append(word)
	print(tokensWithOutStopWords)
	return(tokensWithOutStopWords)
#main
def main():

	while(True):
		sans = speechtotext()
		data = str(sans.lower()) 
		token = dataProcessing(data)
		var="tara"
		if (var == name):
			speak("anand")
		elif(data == 'goodbye'):
			print (":)")
			break
 
main()
