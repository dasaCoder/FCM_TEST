import pandas as pd
import dataframe

data = pd.read_csv(r'D:\Academic\Level 4 - Semester 1\Research Project\Categorized Data\NEW DATA.csv')

data = data.fillna('Nothing')

data.to_csv(r'D:\Academic\Level 4 - Semester 1\Research Project\Categorized Data\WithoutNaN.csv', index=False)



