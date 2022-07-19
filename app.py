#import files
import pyttsx3
from speechrec import *
import nltk
from nltk.corpus import stopwords
import psycopg2
from dbConfig import *
import re

#declaration
engine = pyttsx3.init()

sound = engine.getProperty('voices')
stop_words = stopwords.words('english')
# print(stop_words)
#functions
def searchFinalAns(key):
	ans=[]
	conn = psycopg2.connect(database=NAME,user=USER,password=PASSWORD,host=HOST,port=port)
	cur=conn.cursor()
	cur.execute('select data from answer where key = %s', (key,))
	rows = str(cur.fetchone())
	ans.append(re.sub("[}{,.)(]",'', rows))
	#print(ans[0])
	conn.close()
	return(ans[0])


def maxCatcher(List):
	counter = 0
	num = List[0]
     
	for i in List:
		curr_frequency = List.count(i)
		if(curr_frequency> counter):
			counter = curr_frequency
			num = i
 
	#print("repeated", num)
	if (num=="None"):
		num='001'
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
			rows = str(cur.fetchone())
			#print(rows)
			key.append(re.sub("[}{,.')(]",'', rows))
			conn.commit()
			#print(key)
		ansKey=maxCatcher(key)
		conn.close()
		return(ansKey)


def wrongAns(data):
	texttoappend=data
	appendFile=open('feedback.txt','a')
	appendFile.write('\n')
	appendFile.write(texttoappend)
	print("feedback recorded")

def speak(ans):
	engine.say(ans)
	engine.runAndWait()
def dataProcessing(text):

	tokens = nltk.word_tokenize(text)
	#print (tokens)

	tokensWithOutStopWords = []
	for word in tokens:
		if word not in stop_words:
			tokensWithOutStopWords.append(word)
	#print(tokensWithOutStopWords)
	#search(tokensWithOutStopWords)
	return(tokensWithOutStopWords)
#main
def main():
	mode =1 #1 for text mode, 2 for voice
	while(True):
		if (mode==2):
			print("Say `Activate keybord` for test input mode")
			sans = speechtotext()
			print("You: ",sans)
			data = str(sans.lower()) 
			if(data=='activate keyboard'):
				mode=1
				speak("Text input mode enabled")
			elif(data == 'goodbye'):
					print (":)")
					break
			else:
				token = dataProcessing(data)
				var="sara"
				if (name == var):
					searchKey=search(token)
					out=searchFinalAns(searchKey)
					speak(out)
					speak('Are you happy with this answer?. yes or no?')
					sans = speechtotext()
					if (sans=='yes'):
						print("thanks")
					elif (sans=='no'):
						wrongAns(data)
					else:
						print('wrong input')
				elif(data =='wrong answer'):
					wrongAns(data)
		elif (mode==1):
			#try:
			data = str((input(" Enter your Query ")).lower())
			print ("You: ",data)
			token = dataProcessing(data)
			searchVal=search(token)
			out=searchFinalAns(searchVal)
			print(name,": ",out)
			ans=(input(" Are you happy with this answer? Y/N")).lower()
			if (ans=='y'):
				print("thanks")
			elif (ans=='n'):
				wrongAns(data)
			else:
				print('wrong input')
			mode_change = int(input("Enter	2 for Activate Voice Mode"))
			print(type(mode_change))
			if (mode_change==2):
				mode=2
				print("Voice mode enabled")
			else:
				#nothing to do
				print("text mode")
			#except:
				#print("system failed :(")

main()
