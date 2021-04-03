import math 
import csv
import plotly.express as px
import pandas as pd

with open ("data.csv",newline='') as f :
    reader=csv.reader(f)
    file_data=list(reader)

data=file_data[0]

#step 1: finding mean

def mean (data):
    n=len(data)
    total=0
    for x in data:
        total +=int (x)

    mean= total / n 
    return mean 

# step 2: squaring and getting the values

squared_list=[]
for number in data: 
    a= int (number)-mean (data)
    a = a**2
    squared_list.append(a)

# step 3: gettting sum

sum=0
for i in squared_list:
    sum=sum+i

# step 4: divinding the sum by the total values

result=sum / (len(data)-1)

# step 5: getting the standard deviation by taking square root of the result

std_deviation=math.sqrt(result)
print ("standard deviation of the data is: -->",std_deviation)

# extra stuff turning it into a graph:

df=pd.read_csv("data.csv")
fig= px.scatter()
fig.show()



