#import files
import pyttsx3
from speechrec import *
import nltk
from nltk.corpus import stopwords
import psycopg2
from dbConfig import *

#declaration
engine = pyttsx3.init()

sound = engine.getProperty('voices')
stop_words = stopwords.words('english')
# print(stop_words)
#functions
def searchFinalAns(key):
	conn = psycopg2.connect(database=NAME,user=USER,password=PASSWORD,host=HOST,port=port)
	cur=conn.cursor()
	cur.execute('select data from answer where key = %s', key)
	rows = cur.fetchall()


def maxCatcher(List):
	counter = 0
	num = List[0]
     
	for i in List:
		curr_frequency = List.count(i)
		if(curr_frequency> counter):
			counter = curr_frequency
			num = i
	print("repeated", num)
	return(num)

def search(token_key):
		conn = psycopg2.connect(database=NAME,user=USER,password=PASSWORD,host=HOST,port=port)
		cur=conn.cursor()
		key=[]
		length= len(token_key)
		if (length	> 4):
			length = 4
		count = 0
		while (length != 0):
			val = token_key[count]
			length = length - 1
			count = count + 1
			sql='SELECT key from answer  WHERE token LIKE %s'
			search_term = val
			like_pattern = '%{}%'.format(search_term)
			cur.execute(sql, (like_pattern,))
			rows = cur.fetchall()
			key.append(rows)
			conn.commit()
			print(key)
		ansKey=maxCatcher(key)
		conn.close()
		return(ansKey)


def wrongAns(data):
	print(data)

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
	#search(tokensWithOutStopWords)
	return(tokensWithOutStopWords)
#main
def main():
	mode =1 #1 for text mode, 2 for voice
	while(True):
		if (mode==2):
			print("Say `Activate keybord` for test input mode \n Report wrong answer `Wrong answer`")
			sans = speechtotext()
			data = str(sans.lower()) 
			token = dataProcessing(data)
			searchKey=search(token)

			var="tara"
			if (var == name):
				speak("anand")
			elif(data == 'goodbye'):
				print (":)")
				break
			elif(data=='activate keyboard'):
				mode=1
			elif(data =='wrong answer'):
				wrongAns(data)
		elif (mode==1):
			#try:
			data = str((input("Enter your Query ")).lower())
			print (data)
			token = dataProcessing(data)
			mode_change = int(input("Enter	2 for Activate Voice Mode"))
			print(type(mode_change))
			if (mode_change==2):
				mode=2
			else:
				#nothing to do
				print("text mode")
			ans=(input("Are you happy with this answer? Y/N")).lower()
			if (ans=='y'):
				print("thanks")
			elif (ans=='n'):
				wrongAns(data)
			else:
				print('wrong input')
			#except:
				#print("system failed :(")

main()
