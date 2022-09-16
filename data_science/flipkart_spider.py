from base64 import urlsafe_b64decode
from dputils import scrape


# STEP 1  get the data as soup object 
# STEP 2 create the set-up dictionaries (MOST IMPORTANT)
# STEP 3 pass the dictionaries into the extract_many function
# STEP 4 repeat  step 1 to step 3 until data keeps coming 
# STEP 5 check and save data into a file 

def get_data(q):
   # STEP 1 :understanding the url

   #STEP 2 : target dict. , items dict., etc
   t = {'tag':'div','attrs':{'class':'_1YokD2 _3Mn1Gg'}} 
   rep_items ={'tag':'div','attrs':{'class':'_1AtVbE col-12-12'}} 
   title ={'tag':'div','attrs':{'class':'_4rR01T'}}
   price = {'tag':'div','attrs':{'class':'_30jeq3 _1_WHN1'}}
   link ={'tag':'a','attrs':{'class':'_1fQZEK'},'output':'href'} 
   pos=1
   all_data=[]
   
   while True:
       url = f'https://www.flipkart.com/search?q={q}&page={pos}'
       print(url)
       soup=scrape.get_webpage_data(url)
         #STEP 3 : 
       data=scrape.extract_many(soup,target=t,items=rep_items,title=title,price=price,link=link)
       if isinstance(data,list):
           if len(data)>0:
                pos+= 1
                all_data.extend(data)
           else:
                break
       else:
            break
   return all_data
 # use
laptops=get_data('laptops')
pd.Dataframe(laptops).to_csv('laptop_data.csv')

 




#STEP 3 : 
data=scrape.extract_many(soup,target=t,items=rep_items,title=title,price=price,link=link)
print(data)