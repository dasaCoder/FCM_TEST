#!/usr/bin/env python
# coding: utf-8

# In[1]:


#get_ipython().system('pip install selenium')
#get_ipython().system('pip install bs4')


# In[35]:


import requests, os, random, sys, time
from selenium import webdriver
from bs4 import BeautifulSoup
import re

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")


# In[3]:


browser = webdriver.Chrome('chromedriver.exe',chrome_options=options)

browser.get('https://www.linkedin.com/uas/login')

file = open('config.txt')


# In[4]:


lines = file.readlines()
username = lines[0]
password = lines[1]

elementID = browser.find_element_by_id('username')
elementID.send_keys(username)

elementID = browser.find_element_by_id('password')
elementID.send_keys(password)

elementID.submit()

visitingProfileID = '/in/dulanga-rajapaksha-53bb31140/'
fullLink = 'https://www.linkedin.com' + visitingProfileID
browser.get(fullLink)

link = 'https://www.linkedin.com/in/dilusha-dasanayaka-446637113/'
browser.get(link)

SCROLL_PAUSE_TIME = 1


# In[5]:


last_height = browser.execute_script("return document.body.scrollHeight")

for i in range(3):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight/4);")
    time.sleep(SCROLL_PAUSE_TIME)

    browser.execute_script("window.scrollTo(document.body.scrollHeight/4, document.body.scrollHeight/2);")
    time.sleep(SCROLL_PAUSE_TIME)

    browser.execute_script("window.scrollTo(document.body.scrollHeight/2, document.body.scrollHeight*0.75);")
    time.sleep(SCROLL_PAUSE_TIME)

    browser.execute_script("window.scrollTo(document.body.scrollHeight*0.75, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)

    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
        last_height = new_height


# In[6]:


browser.execute_script("window.scrollTo(document.body.scrollHeight/2, document.body.scrollHeight*0.6);")
#text = browser.find_element_by_link_text.get_text().strip()
browser.find_element_by_class_name('pv-skills-section__additional-skills').click()


# In[7]:


src = browser.page_source
soup = BeautifulSoup(src, 'lxml')


###Name Setion
name_div = soup.find('div', {'class': 'flex-1 mr5'})
name_loc = name_div.find_all('ul')
name = name_loc[0].find('li').get_text().strip()
print(name)
location = name_loc[1].find('li').get_text().strip()
print(location)


###aboutme Section
aboutme_div = soup.find('div', {'class': 'profile-detail'})
aboutme_loc = aboutme_div.find('div', {'class': 'pv-oc ember-view'})
aboutme_section = aboutme_loc.find('p')
aboutme = aboutme_section.find('span').get_text().strip()


# In[37]:


exp_section = soup.find('section', {'id': 'experience-section'})
#print(exp_section)
experice_ls = []
if exp_section:
    exp_section = exp_section.find('ul')
    li_tag = exp_section.find_all('li')
    
    if len(li_tag) >= 0:
        x = 0
        while x < len(li_tag):
            li_tag1 = li_tag[x].find('a')
            if li_tag1:
                job_title1 = li_tag1.find('h3').get_text().strip()
                if str(job_title1) == 'Company Name' or str(job_title1) == 'Undergraduate' :
                    print('ignored')
                elif re.match('Company Name', job_title1):
                    print("t")
                    ls_ul = li_tag1.find_all('ul')
                    if ls_ul:
                        print("s")
                        job_ls = ls_ul.find_all('li')
                        if job_ls:
                            title_3 = job_ls.find('h3').get_text().strip()
                            print('s')
                            print(title_3)
                else:
                    experice_ls.append(job_title1)
            x = x + 1
print(experice_ls)


# In[39]:


###Education Section
edu_section = soup.find('section', {'id': 'education-section'})
edu_ls = []
if edu_section:
    edu_sec_ul = edu_section.find('ul')
    if edu_sec_ul:
        edu_sectionlist = edu_section.find_all('li')

        if edu_sectionlist:
            if len(edu_sectionlist) > 0:
                educationp = edu_sectionlist[0].find_all('p')
                educationspan = educationp[1].find_all('span')
                education1 = educationspan[1].get_text().strip()
                edu_ls.append(education1)

            if len(edu_sectionlist) > 1:
                educationp = edu_sectionlist[1].find_all('p')
                educationspan = educationp[1].find_all('span')
                education2 = educationspan[1].get_text().strip()
                edu_ls.append(education2)

            if len(edu_sectionlist) > 2:
                educationp = edu_sectionlist[2].find_all('p')
                educationspan = educationp[1].find_all('span')
                education3 = educationspan[1].get_text().strip()
                edu_ls.append(education3)
print(edu_ls)


# In[9]:


skills = []
skill_section = soup.find('div', {'id': 'skill-categories-expanded'})
if skill_section:
    skill_divs = skill_section.find_all('div',{'class':'pv-skill-category-list'})
    if len(skill_divs) > 0:
        for elem in skill_divs:
            elem_ol = None
            elem_ol = elem.find('ol')
            if elem_ol:
                elem_lis = elem_ol.find_all('li')
                if len(elem_lis) > 0:
                    i = 0
                    while i < len(elem_lis):
                        skills.append(elem_lis[i].find_all('span',{'class':'pv-skill-category-entity__name-text'})[0].get_text().strip())
                        i = i + 1
print(skills)


# In[49]:


applicant_details = edu_ls[:3] + experice_ls[:2] + skills[:7]
print(applicant_details)


# In[68]:


a = ['software','Computer Software Engineering', 'developer', 'programmer', 'Programming', 'Hibernate', 'Web', 'Mobile', 'Android', 'iOS', 'Agile', 'OOP', 'JS', 'Design Patterns', 'Technical Lead', 'Tech Lead', 'Support Engineer', 'Enterprise Application Development', 'Maven', 'SDLC', 'C++', 'Microsoft Excel']
b = ['QA', 'Tester', 'Quality', 'Automation', 'Selenium', 'Testing', 'Test']
e = ['Business', 'Functional Analyst', ' Solution', 'System Analyst', 'Requirements Analysis']
f = ['Networking', 'Switches', 'Cisco Packet Tracer', 'Wireless', 'Network', 'TCP', 'LAN-WAN']
i = ['Manager', 'owner', 'Management', 'Director', 'Strategy']
j = ['PHD', 'MSC', 'postgraduate', 'Research']
l = ['Lecturer', 'tutor', 'Instructor', 'Demonstrator']
m = ['Database', 'MySQL', 'Oracle', 'SQL', 'Apache', ' MongoDB ']
n = ['Data Science', 'Machine Learning', 'Data Scientist', 'Data Analysis', 'Statistics', 'Data Mining']
p = ['Computer Science', 'Computer Engineering', 'Systems Engineer', 'System Administrator', 'System Administration']
q = ['Information Technology',  'ICT']
r = ['Computer Architecture']
s = ['Distributed System', 'Cluster Computing']
t = ['Cloud Computing']
u = ['Algorithms', 'Data Structures']
w = ['JAVA', 'Python', 'HTML', '.NET', 'Ruby', 'COBOL', 'XML', ' jQuery', 'Bootstrap', 'PHP', 'Cascading Style Sheets']
x = ['Mathematics', 'Physical Science', 'physics']
y = ['Operating Systems', 'Windows', 'Ubuntu', 'Linux', 'Unix']
za = ['Multimedia', 'Animation', 'Graphic', 'Digital Media']
ab = ['Cyber', 'Information Security']
ac = ['Information System']
ad = ['Artificial Intelligence', 'Deep Learning', 'Computer Vision', 'Robotics', 'Natural Language']
ae = ['Bioinformatics', 'Biology', 'Biomedical']
af = ['Telecommunication', 'Communication']
ag = ['Computer Hardware', 'Embedded System', 'Microcontrollers ', 'Electronic', 'Internet of Things', 'Arduino', 'PCB Design']
ah = ['Marketing', 'E-Commerce', 'Banking', 'Finance', 'Account', 'Customer', 'Sales', 'Pricing', 'Markets']
aj = ['E-Governance', 'Legal', 'Law']
ak = ['Geography', 'Geographic', 'GIS', 'Geoinformatics']
al = ['Human Computer Interaction', 'User Interface', 'User Experience', 'UI/UX']
ao = ['Big Data', 'Hadoop']


g = 'Software Engineering'
z = 'Quality Assurance'
ee = 'Business Analysis'
ff = 'Networking'
ii = 'Management'
jj = 'Research'
ll = 'Lecturing'
mm = 'Database'
nn = 'Data Science'
pp = 'Computer Science'
qq = 'Information Technology'
rr = 'Computer Architecture'
ss = 'Distributed System'
tt = 'Cloud Computing'
uu = 'Data Structures and Algorithms'
ww = 'Programming Languages'
xx = 'Mathematics'
yy = 'Operating Systems'
zz = 'Multimedia, Animation and Graphic Design'
abb = 'Cyber Security'
acc = 'Information System'
add = 'Artificial Intelligence'
aee = 'Bio-informatics'
aff = 'Telecommunication'
agg = 'Embedded System'
ahh = 'Marketing and E-Commerce'
ajj = 'E-Governance'
akk = 'GIS'
all = 'HCI'
aoo = 'Big Data'


c='Other'

d = {g:a, z:b, ee:e, ff:f, ii:i, jj:j, ll:l, mm:m, nn:n, pp:p, zz:za, qq:q, rr:r, ss:s, tt:t, uu:u, ww:w, xx:x, yy:y, abb:ab, acc:ac, add:ad, aee:ae,aff:af, agg:ag, ahh:ah, akk:ak, all:al, aoo:ao}


# In[69]:


converted_array = []
for record in applicant_details:
    is_found = False
    for val in d:
        if record in d[val]:
            print(record,'yes')
            converted_array.append(val)
            is_found = True
            break
    if is_found == False:
        converted_array.append('Other')


# In[70]:


print(converted_array)






