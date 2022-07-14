import psycopg2
import nltk
from nltk.corpus import stopwords
import datetime

NAME= "knowledge"
USER="postgres"
PASSWORD="admin"
HOST="127.0.0.1"
port="5432"

stop_words = stopwords.words('english')

log = open('log.txt', 'w')
def dataProcessing(text):

	tokens = nltk.word_tokenize(text)
	print ("Tokens With Stop Words: ",tokens)

	tokensWithOutStopWords = []
	for word in tokens:
		if word not in stop_words:
			tokensWithOutStopWords.append(word)
	print("Tokens With Out Stop Words: ",tokensWithOutStopWords)
	return(tokensWithOutStopWords)
def dataInsert(data_val,token_val):
	conn = psycopg2.connect(database=NAME,user=USER,password=PASSWORD,host=HOST,port=port)
	cur=conn.cursor()
	try:
		cur.execute("insert into answer (data,token) values (%s, %s)", (data_val,token_val))
		conn.commit()
		conn.close()
	except:
		x = str(datetime.datetime.now())
		log.writelines(x+"db inseration error"+"\n")

def training():
	file = open('input.txt', 'r')
	lines = file.readlines()

	for index, line in enumerate(lines):
	    text= ("{}".format(line.strip()))
	    tokens = dataProcessing(text)
	    dataInsert(text,tokens)
	file.close()

training()
log.close()
