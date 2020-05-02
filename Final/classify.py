import pandas as pd
import dataframe

data = pd.read_csv(r'D:\Academic\Level 4 - Semester 1\Research Project\Classify\Test.csv',  names=['category'])

df = pd.DataFrame(data)

a = ['software', 'developer', 'programmer', 'Matlab', 'GIT', 'Spring' 'Programming', 'Development', 'Eclipse', 'Hibernate', 'Web', 'Mobile', 'Android', 'iOS', 'Agile', 'OOP', 'JS', 'Design Patterns', 'Technical Lead', 'Tech Lead', 'Support Engineer', 'Enterprise Application Development', 'Maven', 'SDLC','Requirements analysis', 'JAVA', 'Python', 'HTML', '.NET', 'Ruby', 'COBOL', 'XML', ' jQuery', 'Bootstrap', 'PHP', 'Cascading Style Sheets', 'Visual Studio', 'Visual Basic']
b = ['QA', 'Tester', 'Quality', 'Automation', 'Selenium', 'Testing', 'Test']
e = ['Business', 'Functional Analyst', ' Solution', 'System Analyst', 'Requirements Analysis', 'Analysis', 'Analytical Skills']
f = ['Networking', 'Switches', 'Cisco Packet Tracer', 'Wireless', 'Network', 'TCP', 'LAN-WAN', 'Telecommunication', 'Communication']
h = ['Database', 'MySQL', 'Oracle', 'SQL', 'Apache', ' MongoDB ']
i = ['Data Science', 'Data Scientist', 'Data Analysis', 'Data Mining']
j = ['Computer Science', 'Computer Engineering']
l = ['Systems Engineer', 'System Administrator', 'System Administration', 'System Integration', 'Infrastructure']
m = ['Information Technology',  'ICT']
n = ['Computer architecture', 'Embedded system', 'Real-time computing', 'Dependability']
o = ['Distributed System', 'Cluster Computing', 'Concurrent computing', 'Parallel computing', 'Distributed computing', 'Multithreading', 'Multiprocessing', 'HPC', 'High Performance']
p = ['Cloud Computing']
q = ['Algorithms', 'Data Structures', 'Computational geometry', 'Algorithm']
r = ['Mathematics', 'Physical Science', 'physics', 'Discrete mathematics',  'Probability', 'Statistics', 'Mathematical software', 'Information theory', 'Mathematical analysis', 'Numerical analysis']
s = ['Operating Systems', 'Windows', 'Ubuntu', 'Linux', 'Unix', 'Virtual machine']
t = ['Multimedia', 'Animation', 'Graphic', 'Digital Media', 'Animation', 'Rendering', 'Image',  'Mixed reality', 'Virtual reality' , 'Solid modeling', 'Skechup', ' Tomcat', 'Augmented Reality']
u = ['Cyber', 'Information Security',  'Security', 'Cryptography', 'detection']
w = ['Information System']
x = ['Artificial Intelligence', 'Deep Learning', 'Computer Vision', 'Robotics', 'Natural Language', 'Machine Learning', 'NLP']
y = ['Bioinformatics', 'Biology', 'Biomedical']
ab = ['Printed circuit board', 'Peripheral', 'Integrated circuit', 'Very Large Scale Integration','Systems on Chip (SoCs)', 'Energy consumption (Green computing)', 'Electronic', 'Hardware acceleration', 'Computer Hardware', 'Microcontrollers', 'Internet of Things', 'Arduino', 'PCB Design']
ac = ['E-Governance', 'Legal', 'Law']
ad = ['Geography', 'Geographic', 'GIS', 'Geoinformatics']
ae = ['Human Computer Interaction', 'User Interface', 'User Experience', 'UI/UX',  'Interaction design', 'Social computing', 'Ubiquitous computing', 'Visualization', 'Accessibility']
af = ['Big Data', 'Hadoop']
ag = ['Model of computation', 'Formal language', 'Automata theory', 'Computability theory', 'Computational complexity theory', 'Logic', 'Semantics']
ah = ['Enterprise software', 'Computational', 'Video games', 'E-Commerce', 'E-Learning', 'Word Processing', 'Operations research', 'Educational technology', 'Document management']
ai = ['Manager', 'owner', 'Management', 'Director', 'Strategy', 'Managing', 'Planning']
aj = ['Marketing', 'Banking', 'Finance', 'Account', 'Customer', 'Sales', 'Pricing', 'Markets', 'Financial']

#w = ['JAVA', 'Python', 'HTML', '.NET', 'Ruby', 'COBOL', 'XML', ' jQuery', 'Bootstrap', 'PHP', 'Cascading Style Sheets']
#j = ['PHD', 'MSC', 'postgraduate', 'Research']
#l = ['Lecturer', 'tutor', 'Instructor', 'Demonstrator']

aa = 'Software Engineering'
bb = 'Quality Assurance'
ee = 'Business System Analysis'
ff = 'Communication and Networks'
hh = 'Database'
ii = 'Data Sience'
jj = 'Computer Science'
ll = 'System/Infrastructure integration &  Administration'
mm = 'Information Technology'
nn = 'Computer systems organization'
oo = 'Concurrent computing'
pp = 'Cloud Computing'
qq = 'Data Structures and Algorithms'
rr = 'Mathematics of computing'
ss = 'Software organization & Operating Systems'
tt = 'Multimedia, Animation and Graphic Design'
uu = 'Cyber & Information Security'
ww = 'Information System'
xx = 'Artificial Intelligence'
yy = 'Bio-informatics'
abb = 'Computer Hardware'
acc = 'E-Governance'
add = 'GIS'
aee = 'Human computer interaction'
aff = 'Big Data'
agg = 'Theory of computation'
ahh = 'Applied computing'
aii = 'Management'
ajj = 'Marketing'
z = 'Other'
#jj = 'Research'
#ll = 'Lecturing'
#ww = 'Programming Languages

d = {aa:a, bb:b, ee:e, ff:f, hh:h, ii:i, jj:j, ll:l, mm:m, nn:n, oo:o, pp:p, qq:q, rr:r, ss:s, tt:t, uu:u, ww:w, xx:x, yy:y,  abb:ab, acc:ac, add:ad, aee:ae,aff:af, agg:ag, ahh:ah, aii:ai, ajj:aj}


df['new_category'] = z



for k, v in d.items():
    pat = '|'.join(v)
    mask = df.category.str.contains(pat, case=False)

    df.loc[mask, 'new_category'] = k


df.to_csv(r'D:\Academic\Level 4 - Semester 1\Research Project\Classify\skill11.csv', index=False)
