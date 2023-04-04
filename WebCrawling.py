#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests

#URL = 'https://www.jobbank.gc.ca/jobsearch/jobsearch?searchstring=software+developer&locationstring=toronto+on'
URL = 'https://www.jobbank.gc.ca/jobsearch/jobsearch?searchstring=IT+software+developer+&locationstring=toronto+on'
page = requests.get(URL)


# In[4]:


from bs4 import BeautifulSoup as soup


# In[5]:


page.status_code


# In[6]:


bsobj = soup(page.content,'lxml')
results_div = bsobj.find('div', {'class': 'results-jobs'})
if results_div:
    links = results_div.find_all('a', href=True)
    hrefs = []
    for link in links:
        href_str = 'https://www.jobbank.gc.ca'+str(link['href'])
        if(href_str!='https://www.jobbank.gc.ca/login'):
        	hrefs.append(href_str)

hrefs


# In[83]:


job_skills = []
for link in hrefs:
    html = requests.get(link)
    #print(html.status_code)
    bs = soup(html.content,'lxml')
    #for a in bs.findAll('div',{'class':'col-md-9'}):
    for a in bs.findAll('ul',{'class':'csvlist'}):
     	job_skills.append(a.text.strip())
 
print(len(job_skills))
#job_skills


# In[77]:


import pandas as pd
job_skills = []
for link in hrefs:
    html = requests.get(link)
    bs = soup(html.content, 'lxml')
    for a in bs.findAll('ul', {'class': 'csvlist'}):
        skills = a.text.strip().replace('\n', ' ').replace('Experience and specialization Computer and technology knowledge','')
        if skills:
            job_skills.append(skills)
print(len(job_skills))
print(len(job_titles))
print(len(company))

 #   d1 = {'job_titles':job_titles,'company':company,'location': location, 'skills':i}

#df = pd.DataFrame.from_dict(d1)
#df


# In[ ]:





# In[8]:


bs = soup(html.content,'lxml')
bs.findAll('div',{'class':'col-md-9'})


# In[33]:


job_titles = []
for header in bsobj.findAll('span',{'class':'noctitle'}):
    job_title = header.text.strip().split('\n')[0].replace('developer, software', 'software developer')
   # job_title = job_title.replace('developer, software', 'software developer')
    job_titles.append(job_title)
    
job_titles


# In[34]:


company = []
for header in bsobj.findAll('li',{'class':'business'}):
    company.append(header.text.strip().split('\n')[0])

company

#for com in company:
#    print(com)


# In[29]:


#location = []

#for header in bsobj.findAll('li',{'class':'location'}):
#    location.append(header.text.strip().split('\n \t', ))

#location
location = []

for header in bsobj.findAll('li', {'class': 'location'}):
    location.append(header.text.strip().replace('Location', '').strip())

location


# In[68]:


for i in job_skills:
    d1 = {'job_titles':job_titles,'company':company,'location': location, 'skills':i}
import pandas as pd
df = pd.DataFrame.from_dict(d1)
df


# In[69]:


import pandas as pd
df = pd.DataFrame.from_dict(d1)
df


# In[70]:


df


# In[15]:


results_div = bsobj.find('div', {'class': 'results-jobs'})
if results_div:
    links = results_div.find_all('a', href=True)
    hrefs = []
    for link in links:
        href_str = 'https://www.jobbank.gc.ca'+str(link['href'])
        hrefs.append(href_str)

hrefs


# In[16]:


bsobj.find('div', {'class': 'results-jobs'})

