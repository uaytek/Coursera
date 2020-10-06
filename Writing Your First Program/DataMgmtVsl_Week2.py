import numpy as np # linear algebra
import pandas as pd # data processing, CSV I/file  (e.g. pd.read_csvfile 

#Read csv data
df = pd.read_csv('data/nesarc_pds.csv',low_memory=False)

df.columns = map(str.upper,df.columns)

#number of rows and columns
print("Data shape of all rows and columns:",df.shape)


#select just the features that are needed
df = df[["CONSUMER","S6Q1","S6Q3"]]

#number of rows and columns of analyed data.
print("Data shape of selected three columns and rows:",df.shape) 

#convert all values to numeric
df = df.apply(pd.to_numeric)

#print function for displaying frequency distribution
def PrintCountandPercentage(df,column,text):
    print("Counts of ",text)
    c1 = df[column].value_counts(sort=False)
    print(c1) 
    print("Percentage of ", text)
    p1 = df[column].value_counts(sort=False,normalize=True)
    print(p1)


PrintCountandPercentage(df,"CONSUMER","ALL DRINKING STATUS")
PrintCountandPercentage(df,"S6Q1","HAD PANIC ATTACK, SUDDENLY FELT FRIGHTENED/OVERWHELMED/NERVOUS")
PrintCountandPercentage(df,"S6Q3","THOUGHT WAS HAVING HEART ATTACK, BUT DOCTOR SAID JUST NERVES OR PANIC ATTACK")


#sub = df[(df["CONSUMER"]==1).any() & ((df["S6Q1"]==1).any() | (df["S6Q61"]==1).any() | (df["S6Q62"]==1).any()
#                             | (df["S6Q63"]==1).any() | (df["S6Q64"]==1).any() | (df["S6Q65"]==1).any() )]


sub = df[((df["CONSUMER"]==1) | (df["CONSUMER"]==2)) & ((df["S6Q1"]==1) | (df["S6Q1"]==1)  )]

print("Current or ex-drinkers having panic attack data columns and rows:",sub.shape)

PrintCountandPercentage(sub,"CONSUMER","DRINKING STATUS (Currnet and Ex Drinker)")
PrintCountandPercentage(sub,"S6Q1","HAD PANIC ATTACK, SUDDENLY FELT FRIGHTENED/OVERWHELMED/NERVOUS")
PrintCountandPercentage(sub,"S6Q3","THOUGHT WAS HAVING HEART ATTACK, BUT DOCTOR SAID JUST NERVES OR PANIC ATTACK")
