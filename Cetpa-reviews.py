import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


from selenium import webdriver 
from bs4 import BeautifulSoup 
driver = webdriver.Chrome("C:\\usr\\chromedriver") 


Names = []
Review = []
Time = []
Rating_star=[]

url = "https://www.google.com/maps/place/CETPA+INFOTECH+PVT+LTD/@28.5826801,77.3138382,19.96z/data=!4m7!3m6!1s0x390ce45fa267c455:0x20e02d4622605a21!8m2!3d28.5825324!4d77.3160029!9m1!1b1?hl=en-IN"
driver.get(url)
content = driver.page_source

soup = BeautifulSoup(content)

for i in range(0,16,2):
    names = soup.findAll('div',attrs={'class':'section-review-title'})
    find_names = names[i]
    Names.append(find_names.contents[1].text)


for i in range(0,8):
    review = soup.find_all('span',{'class':'section-review-text'})
    review_text = review[i].text
    Review.append(review_text)
    
for i in range(0,8):
    time = soup.find_all('span',{'class':'section-review-publish-date'})
    time_text = time[i].text
    Time.append(time_text)    
    
    
for i in range(0,8):
    rated_star = soup.find_all('span',{'class':'section-review-stars'})
    star = rated_star[i]
    Rating_star.append(star.attrs['aria-label'][1:2])
    
dataset = pd.DataFrame({"Name":Names,"Review":Review,"Review-Duration":Time,"Stars":Rating_star})    
#dataset.to_csv("Reviews-Classifier/Scrapped-Reviews.csv",index=False,encoding='utf-8')                

def reviews(a):
    if(a == '5'):
        return 'positive'
    else:
        return 'negative'

dataset['Label'] = dataset['Stars'].apply(reviews)      


X = dataset.iloc[:,0:-1].values
y = dataset.iloc[:,-1].values
    

        
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

X[:,0] = le.fit_transform(X[:,0])
X[:,1] = le.fit_transform(X[:,1])
X[:,2] = le.fit_transform(X[:,2])
X[:,3] = le.fit_transform(X[:,3])


from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(categorical_features=[0,1,2,3])
X = ohe.fit_transform(X)
X = X.toarray()
y = le.fit_transform(y)


from sklearn.linear_model import LogisticRegression
log_reg = LogisticRegression()
log_reg.fit(X,y)
log_reg.score(X,y)


from sklearn.tree import DecisionTreeClassifier
dtc = DecisionTreeClassifier()
dtc.fit(X,y)
dtc.score(X,y)

y_pred = dtc.predict(X)

from sklearn.metrics import confusion_matrix
cnn = confusion_matrix(y,y_pred)

from sklearn.metrics import precision_score,recall_score,f1_score
precision_score(y,y_pred)
recall_score(y,y_pred)
f1_score(y,y_pred)


log_reg.predict(X[[4]])

        

              
                
                
                
                
                
                