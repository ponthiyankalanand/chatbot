import psycopg2
import nltk
from nltk.corpus import stopwords
import datetime
from dbConfig import *
stop_words = stopwords.words('english')

log = open('log.txt', 'w')
def keygen():
	now = datetime.datetime.now()
	keynum = now.strftime("%H%M%f")
	return(keynum)

def dataProcessing(text):

	tokens = nltk.word_tokenize(text)
	print ("Tokens With Stop Words: ",tokens)

	tokensWithOutStopWords = []
	for word in tokens:
		if word not in stop_words:
			tokensWithOutStopWords.append(word)
	key=keygen()
	tokensWithOutStopWords.append(key)
	print("Tokens With Out Stop Words: ",tokensWithOutStopWords)

	return(tokensWithOutStopWords,key)
def dataInsert(data_val,token_val,key_val):
	conn = psycopg2.connect(database=NAME,user=USER,password=PASSWORD,host=HOST,port=port)
	cur=conn.cursor()
	try:
		cur.execute("insert into answer (data,token,key) values (%s, %s,%s)", (data_val,token_val,key_val))
		conn.commit()
		conn.close()
	except:
		x = str(datetime.datetime.now())
		log.writelines(x+"db inseration error"+"\n")

def training():

	file = open('input.txt', 'r')
	lines = file.readlines()
	trainingData = []
	for index, line in enumerate(lines):
		try:
		    text= ("{}".format(line.strip()))
		    tokens = dataProcessing(text.lower())
		    trainingData.append(tokens[0])
		    dataInsert(text,tokens[0],tokens[1])

		except:
			x = str(lines)
			log.writelines(x+"db inseration error"+"\n")
	file.close()
	train = open('trainingInput.txt', 'w')
	train.writelines(str(trainingData))
	train.close()
	print(trainingData)
training()

log.close()
