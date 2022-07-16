#from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
#from sklearn.model_selection import train_test_split # Import train_test_split function
#from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
df = pd.read_csv("test.csv")
df.head()
#print(df)
inputs= df.drop('key',axis='columns')
target= df['key']
le_token= LabelEncoder()
inputs['token1_n'] = le_token.fit_transform(inputs['token1'])
inputs['token2_n'] = le_token.fit_transform(inputs['token2'])
inputs['token3_n'] = le_token.fit_transform(inputs['token3'])
inputs_n= inputs.drop(['token1','token2','token3'],axis='columns')

print(inputs_n) 
model = tree.DecisionTreeClassifier()
model.fit(inputs_n,target)
#model.score(inputs,target)
model.predict([ [0,0,1] ])
#print(inputs,target)
#col_names = ['key', 'token']