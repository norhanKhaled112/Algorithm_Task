insertion=[5,2,4,6,1,3]
for i in range(1,len(insertion)):
    j=i-1
    temp=insertion[i]
    while(j>=0 and insertion[j]>temp):
        insertion[j+1]=insertion[j]
        j=j-1
    insertion[j+1]=temp
print(insertion)