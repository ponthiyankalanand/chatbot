#Hai All
'Sara' is a small chatbot can operate with voice and text mode. We created Sara with python, postgres and a lots of love. 

#What Sara Can Do ?
Sara can listen, speak, answer your questions with in her knowledge base.

#How can be Train Sara?
##Step 1:
prepaire Answers in a file (line by line). Rename it with 'input.txt' then run 'python tokenInsert.py'.
##Step 2:
Test Sara, Run 'app.py' and talk with sara. If she return wrong answer say/type 'No' for the answer, Then Sara will store the question in 'feedback.txt' file. You can train again with this data.
##Step 3:
track the errors, Refer the 'log.txt' file for analize logs.

#Config file:
In dbConfig.py file we can config DB credintials and Chatbot name.

#Dependancy Packages
>pip install pyttsx3
>pip install speechrecognition
>pip install pipwin
>pipwin install pyaudio
>pip  install  psycopg2
>python -m pip install nltk==3.5
nltk.download(punkt),
nltk.download('stopwords')
>python -m pip install numpy matplotlib


