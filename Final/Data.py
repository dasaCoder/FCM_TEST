import pandas as pd
import dataframe

data = pd.read_csv(r'D:\Academic\Level 4 - Semester 1\Research Project\Monkey.csv',  names=['category'])

data.fillna('Nothing')
print(data)

df = pd.DataFrame(data)


a = ['software', 'developer', 'programmer', 'python', 'Android', ' Java', 'OOP', 'HTML', 'CSS', 'C#', 'C', 'web', 'Mobile', 'iOS', 'C++', 'JQuery', 'PHP', 'JavaScript', 'AngularJS', '.NET', 'SOAP', 'REST', 'XML', 'AJAX', 'Eclips', 'ASP.NET', 'NodeJS', 'Enterprise', 'Design,Patterns']
b = ['QA', 'Tester', 'Quality,Assurence', 'Automation', 'Selenium', 'Testing']
e = ['Business']
f = ['Networking', 'LAN', 'WAN', 'Switches', 'Cisco,Packet,Tracer', 'Wireless']
i = ['Manager', 'owner', 'Management']
j = ['PHD', 'MSC', 'postgraduate', 'Research']
l = ['Lecturer', 'tutor', 'Instructor']
m = ['Database', 'MySQL', 'Oracle', 'SQL', 'Apache']
n = ['Data,Science', 'Data', 'Machine,Learning']



g = 'Software Engineering'
z = 'Quality Assurence'
ee = 'Business Analysis'
ff = 'Networking'
ii = 'Management'
jj = 'Research'
ll = 'Lecturing'
mm = 'Database'
nn = 'Data Science'

c='Other'

d = {g:a, z:b, ee:e, ff:f, ii:i, jj:j, ll:l, mm:m, nn:n}

df['new_category'] = c

for k, v in d.items():
    pat = '|'.join(v)
    mask = df.category.str.contains(pat, case=False)

    df.loc[mask, 'new_category'] = k

print (df.head(60))

