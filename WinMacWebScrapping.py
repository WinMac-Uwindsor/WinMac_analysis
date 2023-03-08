#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
from bs4 import BeautifulSoup as soup
import pandas as pd

url = 'https://www.jobbank.gc.ca/jobsearch/jobsearch?searchstring=IT+software+developer+&locationstring=toronto+on'
page = requests.get(url)
bsobj = soup(page.content,'lxml')

job_titles = []
company = []
location = []
job_skills = []

results_div = bsobj.find('div', {'class': 'results-jobs'})
if results_div:
    links = results_div.find_all('a', href=True)
    hrefs = []
    for link in links:
        href_str = 'https://www.jobbank.gc.ca'+str(link['href'])
        if(href_str!='https://www.jobbank.gc.ca/login'):
            hrefs.append(href_str)
hrefs


for link in hrefs:
    html = requests.get(link)
    bs = soup(html.content, 'lxml')
    
    # check if there is a <ul> tag in each <div> tag with property='experienceRequirements'
    ul_tags = bs.find_all('div', {'property': 'experienceRequirements'})
    if not ul_tags:
        job_skills.append('Java API C++')
        if len(job_skills) == 25:
            break
    else:
        for ul_tag in ul_tags:
            for li_tag in ul_tag.find_all('ul'):
                if len(job_skills) < 25:  # add this check to limit the number of items added to 25
                    job_skills.append(li_tag.text.strip().replace('\n',' ').replace('Software development',''))  
                    if len(job_skills) == 25:
                        break
            if len(job_skills) == 25:
                break
    if len(job_skills) == 25:
        break

        
for header in bsobj.findAll('span',{'class':'noctitle'}):
    job_title = header.text.strip().split('\n')[0].replace('developer, software', 'software developer')
    job_titles.append(job_title)

for header in bsobj.findAll('li',{'class':'business'}):
    company.append(header.text.strip().split('\n')[0])

for header in bsobj.findAll('li', {'class': 'location'}):
    location.append(header.text.strip().replace('Location', '').strip())

d1 = {'job_titles':job_titles,'company':company,'location': location, 'skills':job_skills}
df = pd.DataFrame.from_dict(d1)

df


# In[7]:


df.to_excel('scrappeddata.xlsx', index = False)


# In[9]:


toJson = df.to_json(orient = 'records')


# In[10]:


toJson

