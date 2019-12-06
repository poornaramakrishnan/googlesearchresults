import pandas as pd
import requests
from bs4 import BeautifulSoup
from time import sleep
import time


check=pd.read_excel(r"filename.xlsx")

check["link1"]=""
check["link2"]=""
check["link3"]=""
check["des1"]=""
check["des2"]=""
check["des3"]=""
check["flag"]=""

start_time = time.time()

for index,row in check.iterrows():
    try:
        search_item=str(row["Name"])
        url="https://www.google.co.in/search?q=" +search_item
        response=requests.get(url)
        soup=BeautifulSoup(response.content,"html.parser")
        #links3=soup.findAll('div')
        links3=soup.findAll('div',attrs={'class':'BNeawe vvjwJb AP7Wnd'})
        
        j=0
        urls=[]
        for h in links3:
            print(h)
            urls.append(h)
            j=j+1
            if(j==3):
              continue
        try:
            check.set_value(index,"link1",str(urls[0]))
            check.set_value(index,"link2",str(urls[1]))
            check.set_value(index,"link3",str(urls[2]))
            check.set_value(index,"flag",1)
        except IndexError as e:
            check.set_value(index,"flag",0)
        
    
        links1=soup.findAll('div',attrs={'class':"BNeawe s3v9rd AP7Wnd"})
    
        desc=[]
        i=0
        for link in links1:
            #print (link.text)
            desc.append(link.text)
            i=i+1
            if(i==3):
                break
        try:
            check.set_value(index,"des1",str(desc[0]))
            check.set_value(index,"des2",str(desc[1]))
            check.set_value(index,"des3",str(desc[2]))
            check.set_value(index,"flag",1)
        except IndexError as e:
            check.set_value(index,"flag",0)
    except requests.exceptions.SSLError as e:
        print("sleeping")
        sleep(150)
        continue
    

print("--- %s seconds ---" % (time.time() - start_time))
