
'''

import csv

filename = 'empnames.csv'

with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        print(row)


'''
import pandas as pd

df = pd.read_csv('emp.csv')
print(df)
count = 0
file1 = open("myfile.txt", "w")

for row in df.iterrows():
   # print(str(df['FirstName'][count])+" "+ str(df['LastName'][count]) )
    full_name = str(df['FirstName'][count]) + " " + str(df['LastName'][count])
    email = str(df['Email'][count])
    count += 1
    print(f"<vcard ba:dial-id='{count}'><fn><text>{full_name}</text></fn><email ba:index='{count}'><text>{email}</text></email></vcard> \n")
    file1.write(f"<vcard ba:dial-id='{count}'><fn><text>{full_name}</text></fn><email ba:index='{count}'><text>{email}</text></email></vcard> \n")

