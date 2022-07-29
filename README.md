# Hai All
'Tele' is a small chatbot can operate with voice and text mode. We created Tele with python, postgres and a lots of love. 

# What Tele Can Do ?
Tele can listen, speak, answer your questions with in her knowledge base.

# How can be Train Tele?
## Step 1:
prepaire Answers in a file (line by line). Rename it with 'input.txt' then run 'python tokenInsert.py'.
## Step 2:
Test Tele, Run 'app.py' and talk with sara. If she return wrong answer say/type 'No' for the answer, Then Tele will store the question in 'feedback.txt' file. You can train again with this data.
## Step 3:
track the errors, Refer the 'log.txt' file for analize logs.

# Config file:
In dbConfig.py file we can config DB credintials and Chatbot name.

# Dependancy Packages
> pip install pyttsx3

> pip install speechrecognition

> pip install pipwin

> pipwin install pyaudio

> pip  install  psycopg2

> python -m pip install nltk==3.5

nltk.download(punkt),
nltk.download('stopwords')

> python -m pip install numpy matplotlib

# DB Query
-- Table: public.answer

-- DROP TABLE IF EXISTS public.answer;

CREATE TABLE IF NOT EXISTS public.answer
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    data character varying COLLATE pg_catalog."default" NOT NULL,
    token character varying COLLATE pg_catalog."default" NOT NULL,
    key integer,
    CONSTRAINT answer_pkey PRIMARY KEY (id),
    CONSTRAINT answer_token_key_key UNIQUE (token, id),
    CONSTRAINT token_unique UNIQUE (token)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.answer
    OWNER to postgres;

[PPT Doc] (https://docs.google.com/presentation/d/1nnJdWRHLIKYhyErknELVGB4M3oCSHz6-/edit?usp=sharing&ouid=117216474420121531915&rtpof=true&sd=true)

