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

url = "https://www.google.com/maps/place/CETPA+INFOTECH+PVT+LTD/@28.5825653,77.3138356,17z/data=!4m7!3m6!1s0x390ce45fa267c455:0x20e02d4622605a21!8m2!3d28.5825324!4d77.3160029!9m1!1b1"
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
dataset.to_csv("Reviews-Classifier/Scrapped-Reviews.csv",index=False,encoding='utf-8')                

        
        

              
                
                
                
                
                
                