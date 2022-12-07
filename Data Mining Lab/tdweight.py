import pandas as pd
df=pd.read_csv('weightass.csv')
data=df.values.tolist()
c1=0
c2=0
r1=0
r2=0
for i in range(2):
    for j in range(2):
        if(i==0):
            r1=r1+int(data[i][j])
        if(i==1):
            r2=r2+int(data[i][j])
        if(j==0):
            c1=c1+int(data[i][j])
        if(j==1):
            c2=c2+int(data[i][j])
print("Total count for Row 1 :",r1)
print("Total count for Row 2 :",r2)
print("Total count for Col 1 :",c1)
print("Total count for Col 2 :",c2)
print("")
for i in range(2):
    for j in range(2):
        if(i==0):
            print("t_weight of "+str(data[i][j]) +" is: ",float((data[i][j]/r1 )* 100))

        if(i==1):
            print("t_weight of "+str(data[i][j]) +" is: ",float((data[i][j]/r2 )* 100))

        if(j==0):
            print("d_weight of "+str(data[i][j]) +" is: ",float((data[i][j]/c1)* 100))

        if(j==1):
            print("d_weight of "+str(data[i][j]) +" is: ",float((data[i][j]/c2 )* 100))