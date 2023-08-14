#!/usr/bin/env python
# coding: utf-8

# In[5]:


import requests
import json
apiKey='6227b8015de23b3474002d31bcc75478'


# In[18]:


for i in range(1,10):
    res=requests.get('https://api.themoviedb.org/3/discover/movie',params={'api_key':apiKey,'page':i,'region':'IN','year':2018})
    data=res.json()
    for i in data["results"]:
        if 'Andhadhun' in i['title']:
            print(i['id'])
            break
        


# In[19]:


for i in range(1,10):
    res = requests.get('https://api.themoviedb.org/3/discover/movie',params={'api_key':apiKey,'page':i,'region':'IN','year':2018}) 
    data=res.json()
    for i in data['results']:
        if 'Andhadhun' in i['title']:
            print(i['id'])
            break


# In[23]:


r=requests.get('https://api.themoviedb.org/3/search/company',params={'api_key':apiKey,'page':1,'region':'IN','year':2018})
data=r.json()
print(data)


# In[24]:


for i in range(1,10):
    res = requests.get('https://api.themoviedb.org/3/discover/movie',params={'api_key':apiKey,'page':i,'region':'IN','year':2009}) 
    data=res.json()
    for i in data['results']:
        if '3 Idiots' in i['title']:
            print(i['vote_count'],i['vote_average'])
            break


# In[7]:


import requests
import json
apiKey='6227b8015de23b3474002d31bcc75478'

#for i in range(1,10):
res = requests.get('https://api.themoviedb.org/3/person/popular',params={'api_key':apiKey}) 
data=res.json()
data=data['results'][0]
mostpopularid=data['id']
mostpopularid


# In[15]:


res = requests.get('https://api.themoviedb.org/3/person/2786960',params={'api_key':apiKey}) 
data=res.json()
print(data['name'],'-',data['place_of_birth'])


# In[21]:


res = requests.get('https://api.themoviedb.org/3/person/1108120-alia-bhatt/external_ids',params={'api_key':apiKey}) 
data=res.json()
print(data['instagram_id'],data['twitter_id'])


# In[1]:


import requests
import json
apiKey='6227b8015de23b3474002d31bcc75478'


res = requests.get('https://api.themoviedb.org/3/tv/1418/season/06/episode/05',params={'api_key':apiKey,'query':'The Big Bang Theory'}) 
data=res.json()
print(data['name'],'-',data['air_date'])

