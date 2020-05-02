import pandas as pd
import dataframe

data = pd.read_csv(r'D:\Academic\Level 4 - Semester 1\Research Project\Categorized Data\Skills\Book11.csv',  names=['category'])

df = pd.DataFrame(data)

a = ['software', 'developer', 'programmer', 'Programming', 'Hibernate', 'Web', 'Mobile', 'Android', 'iOS', 'Agile', 'OOP', 'JS', 'Design Patterns', 'Technical Lead', 'Tech Lead', 'Support Engineer', 'Enterprise Application Development', 'Maven', 'SDLC']
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

df['new_category'] = c

for k, v in d.items():
    pat = '|'.join(v)
    mask = df.category.str.contains(pat, case=False)

    df.loc[mask, 'new_category'] = k


df.to_csv(r'D:\Academic\Level 4 - Semester 1\Research Project\Categorized Data\Skill8.csv', index=False)
