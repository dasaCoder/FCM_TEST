import pandas as pd
import dataframe

data = pd.read_csv(r'D:\Academic\Level 4 - Semester 1\Research Project\Classify\DataNew11.csv')

df = pd.DataFrame(data)


Org1 = {'Software Engineering':1,
        'Quality Assurance':2,
        'Business System Analysis':3,
        'Communication and Networks':4,
        'Database':5,
        'Data Sience':6,
        'Computer Science':7,
        'System/Infrastructure integration &  Administration':8,
        'Information Technology':9,
        'Computer systems organization':10,
        'Concurrent computing':11,
        'Cloud Computing':12,
        'Data Structures and Algorithms':13,
        'Mathematics of computing':14,
        'Software organization & Operating Systems':15,
        'Multimedia, Animation and Graphic Design':16,
        'Cyber & Information Security':17,
        'Information System':18,
        'Artificial Intelligence':19,
        'Bio-informatics':20,
        'Computer Hardware':21,
        'E-Governance':22,
        'GIS':23,
        'Human computer interaction':24,
        'Big Data':25,
        'Theory of computation':26,
        'Applied computing':27,
        'Management':28,
        'Marketing':29,
        'Other':0 }

df.Org1 = [Org1[item] for item in df.Org1]
#print(df)

Org2 = {'Software Engineering':1,
        'Quality Assurance':2,
        'Business System Analysis':3,
        'Communication and Networks':4,
        'Database':5,
        'Data Sience':6,
        'Computer Science':7,
        'System/Infrastructure integration &  Administration':8,
        'Information Technology':9,
        'Computer systems organization':10,
        'Concurrent computing':11,
        'Cloud Computing':12,
        'Data Structures and Algorithms':13,
        'Mathematics of computing':14,
        'Software organization & Operating Systems':15,
        'Multimedia, Animation and Graphic Design':16,
        'Cyber & Information Security':17,
        'Information System':18,
        'Artificial Intelligence':19,
        'Bio-informatics':20,
        'Computer Hardware':21,
        'E-Governance':22,
        'GIS':23,
        'Human computer interaction':24,
        'Big Data':25,
        'Theory of computation':26,
        'Applied computing':27,
        'Management':28,
        'Marketing':29,
        'Other':0 }

df.Org2 = [Org2[item] for item in df.Org2]
#print(df)

Edu1 = {'Software Engineering':1,
        'Quality Assurance':2,
        'Business System Analysis':3,
        'Communication and Networks':4,
        'Database':5,
        'Data Sience':6,
        'Computer Science':7,
        'System/Infrastructure integration &  Administration':8,
        'Information Technology':9,
        'Computer systems organization':10,
        'Concurrent computing':11,
        'Cloud Computing':12,
        'Data Structures and Algorithms':13,
        'Mathematics of computing':14,
        'Software organization & Operating Systems':15,
        'Multimedia, Animation and Graphic Design':16,
        'Cyber & Information Security':17,
        'Information System':18,
        'Artificial Intelligence':19,
        'Bio-informatics':20,
        'Computer Hardware':21,
        'E-Governance':22,
        'GIS':23,
        'Human computer interaction':24,
        'Big Data':25,
        'Theory of computation':26,
        'Applied computing':27,
        'Management':28,
        'Marketing':29,
        'Other':0 }

df.Edu1 = [Edu1[item] for item in df.Edu1]
#print(df)

Edu2 = {'Software Engineering':1,
        'Quality Assurance':2,
        'Business System Analysis':3,
        'Communication and Networks':4,
        'Database':5,
        'Data Sience':6,
        'Computer Science':7,
        'System/Infrastructure integration &  Administration':8,
        'Information Technology':9,
        'Computer systems organization':10,
        'Concurrent computing':11,
        'Cloud Computing':12,
        'Data Structures and Algorithms':13,
        'Mathematics of computing':14,
        'Software organization & Operating Systems':15,
        'Multimedia, Animation and Graphic Design':16,
        'Cyber & Information Security':17,
        'Information System':18,
        'Artificial Intelligence':19,
        'Bio-informatics':20,
        'Computer Hardware':21,
        'E-Governance':22,
        'GIS':23,
        'Human computer interaction':24,
        'Big Data':25,
        'Theory of computation':26,
        'Applied computing':27,
        'Management':28,
        'Marketing':29,
        'Other':0 }

df.Edu2 = [Edu2[item] for item in df.Edu2]
#print(df)

Edu3 = {'Software Engineering':1,
        'Quality Assurance':2,
        'Business System Analysis':3,
        'Communication and Networks':4,
        'Database':5,
        'Data Sience':6,
        'Computer Science':7,
        'System/Infrastructure integration &  Administration':8,
        'Information Technology':9,
        'Computer systems organization':10,
        'Concurrent computing':11,
        'Cloud Computing':12,
        'Data Structures and Algorithms':13,
        'Mathematics of computing':14,
        'Software organization & Operating Systems':15,
        'Multimedia, Animation and Graphic Design':16,
        'Cyber & Information Security':17,
        'Information System':18,
        'Artificial Intelligence':19,
        'Bio-informatics':20,
        'Computer Hardware':21,
        'E-Governance':22,
        'GIS':23,
        'Human computer interaction':24,
        'Big Data':25,
        'Theory of computation':26,
        'Applied computing':27,
        'Management':28,
        'Marketing':29,
        'Other':0 }

df.Edu3 = [Edu3[item] for item in df.Edu3]


Skill1 = {'Software Engineering':1,
        'Quality Assurance':2,
        'Business System Analysis':3,
        'Communication and Networks':4,
        'Database':5,
        'Data Sience':6,
        'Computer Science':7,
        'System/Infrastructure integration &  Administration':8,
        'Information Technology':9,
        'Computer systems organization':10,
        'Concurrent computing':11,
        'Cloud Computing':12,
        'Data Structures and Algorithms':13,
        'Mathematics of computing':14,
        'Software organization & Operating Systems':15,
        'Multimedia, Animation and Graphic Design':16,
        'Cyber & Information Security':17,
        'Information System':18,
        'Artificial Intelligence':19,
        'Bio-informatics':20,
        'Computer Hardware':21,
        'E-Governance':22,
        'GIS':23,
        'Human computer interaction':24,
        'Big Data':25,
        'Theory of computation':26,
        'Applied computing':27,
        'Management':28,
        'Marketing':29,
        'Other':0 }

df.Skill1 = [Skill1[item] for item in df.Skill1]


Skill2 = {'Software Engineering':1,
        'Quality Assurance':2,
        'Business System Analysis':3,
        'Communication and Networks':4,
        'Database':5,
        'Data Sience':6,
        'Computer Science':7,
        'System/Infrastructure integration &  Administration':8,
        'Information Technology':9,
        'Computer systems organization':10,
        'Concurrent computing':11,
        'Cloud Computing':12,
        'Data Structures and Algorithms':13,
        'Mathematics of computing':14,
        'Software organization & Operating Systems':15,
        'Multimedia, Animation and Graphic Design':16,
        'Cyber & Information Security':17,
        'Information System':18,
        'Artificial Intelligence':19,
        'Bio-informatics':20,
        'Computer Hardware':21,
        'E-Governance':22,
        'GIS':23,
        'Human computer interaction':24,
        'Big Data':25,
        'Theory of computation':26,
        'Applied computing':27,
        'Management':28,
        'Marketing':29,
        'Other':0 }

df.Skill2 = [Skill2[item] for item in df.Skill2]


Skill3 = {'Software Engineering':1,
        'Quality Assurance':2,
        'Business System Analysis':3,
        'Communication and Networks':4,
        'Database':5,
        'Data Sience':6,
        'Computer Science':7,
        'System/Infrastructure integration &  Administration':8,
        'Information Technology':9,
        'Computer systems organization':10,
        'Concurrent computing':11,
        'Cloud Computing':12,
        'Data Structures and Algorithms':13,
        'Mathematics of computing':14,
        'Software organization & Operating Systems':15,
        'Multimedia, Animation and Graphic Design':16,
        'Cyber & Information Security':17,
        'Information System':18,
        'Artificial Intelligence':19,
        'Bio-informatics':20,
        'Computer Hardware':21,
        'E-Governance':22,
        'GIS':23,
        'Human computer interaction':24,
        'Big Data':25,
        'Theory of computation':26,
        'Applied computing':27,
        'Management':28,
        'Marketing':29,
        'Other':0 }

df.Skill3 = [Skill3[item] for item in df.Skill3]


Skill4 = {'Software Engineering':1,
        'Quality Assurance':2,
        'Business System Analysis':3,
        'Communication and Networks':4,
        'Database':5,
        'Data Sience':6,
        'Computer Science':7,
        'System/Infrastructure integration &  Administration':8,
        'Information Technology':9,
        'Computer systems organization':10,
        'Concurrent computing':11,
        'Cloud Computing':12,
        'Data Structures and Algorithms':13,
        'Mathematics of computing':14,
        'Software organization & Operating Systems':15,
        'Multimedia, Animation and Graphic Design':16,
        'Cyber & Information Security':17,
        'Information System':18,
        'Artificial Intelligence':19,
        'Bio-informatics':20,
        'Computer Hardware':21,
        'E-Governance':22,
        'GIS':23,
        'Human computer interaction':24,
        'Big Data':25,
        'Theory of computation':26,
        'Applied computing':27,
        'Management':28,
        'Marketing':29,
        'Other':0 }

df.Skill4 = [Skill4[item] for item in df.Skill4]


Skill5 = {'Software Engineering':1,
        'Quality Assurance':2,
        'Business System Analysis':3,
        'Communication and Networks':4,
        'Database':5,
        'Data Sience':6,
        'Computer Science':7,
        'System/Infrastructure integration &  Administration':8,
        'Information Technology':9,
        'Computer systems organization':10,
        'Concurrent computing':11,
        'Cloud Computing':12,
        'Data Structures and Algorithms':13,
        'Mathematics of computing':14,
        'Software organization & Operating Systems':15,
        'Multimedia, Animation and Graphic Design':16,
        'Cyber & Information Security':17,
        'Information System':18,
        'Artificial Intelligence':19,
        'Bio-informatics':20,
        'Computer Hardware':21,
        'E-Governance':22,
        'GIS':23,
        'Human computer interaction':24,
        'Big Data':25,
        'Theory of computation':26,
        'Applied computing':27,
        'Management':28,
        'Marketing':29,
        'Other':0 }

df.Skill5 = [Skill5[item] for item in df.Skill5]

Skill6 = {'Software Engineering':1,
        'Quality Assurance':2,
        'Business System Analysis':3,
        'Communication and Networks':4,
        'Database':5,
        'Data Sience':6,
        'Computer Science':7,
        'System/Infrastructure integration &  Administration':8,
        'Information Technology':9,
        'Computer systems organization':10,
        'Concurrent computing':11,
        'Cloud Computing':12,
        'Data Structures and Algorithms':13,
        'Mathematics of computing':14,
        'Software organization & Operating Systems':15,
        'Multimedia, Animation and Graphic Design':16,
        'Cyber & Information Security':17,
        'Information System':18,
        'Artificial Intelligence':19,
        'Bio-informatics':20,
        'Computer Hardware':21,
        'E-Governance':22,
        'GIS':23,
        'Human computer interaction':24,
        'Big Data':25,
        'Theory of computation':26,
        'Applied computing':27,
        'Management':28,
        'Marketing':29,
        'Other':0 }

df.Skill6 = [Skill6[item] for item in df.Skill6]


Skill7 = {'Software Engineering':1,
        'Quality Assurance':2,
        'Business System Analysis':3,
        'Communication and Networks':4,
        'Database':5,
        'Data Sience':6,
        'Computer Science':7,
        'System/Infrastructure integration &  Administration':8,
        'Information Technology':9,
        'Computer systems organization':10,
        'Concurrent computing':11,
        'Cloud Computing':12,
        'Data Structures and Algorithms':13,
        'Mathematics of computing':14,
        'Software organization & Operating Systems':15,
        'Multimedia, Animation and Graphic Design':16,
        'Cyber & Information Security':17,
        'Information System':18,
        'Artificial Intelligence':19,
        'Bio-informatics':20,
        'Computer Hardware':21,
        'E-Governance':22,
        'GIS':23,
        'Human computer interaction':24,
        'Big Data':25,
        'Theory of computation':26,
        'Applied computing':27,
        'Management':28,
        'Marketing':29,
        'Other':0 }

df.Skill7 = [Skill7[item] for item in df.Skill7]


Skill8 = {'Software Engineering':1,
        'Quality Assurance':2,
        'Business System Analysis':3,
        'Communication and Networks':4,
        'Database':5,
        'Data Sience':6,
        'Computer Science':7,
        'System/Infrastructure integration &  Administration':8,
        'Information Technology':9,
        'Computer systems organization':10,
        'Concurrent computing':11,
        'Cloud Computing':12,
        'Data Structures and Algorithms':13,
        'Mathematics of computing':14,
        'Software organization & Operating Systems':15,
        'Multimedia, Animation and Graphic Design':16,
        'Cyber & Information Security':17,
        'Information System':18,
        'Artificial Intelligence':19,
        'Bio-informatics':20,
        'Computer Hardware':21,
        'E-Governance':22,
        'GIS':23,
        'Human computer interaction':24,
        'Big Data':25,
        'Theory of computation':26,
        'Applied computing':27,
        'Management':28,
        'Marketing':29,
        'Other':0 }

df.Skill8 = [Skill8[item] for item in df.Skill8]




df.to_csv(r'D:\Academic\Level 4 - Semester 1\Research Project\Classify\last1.csv', index=False)
