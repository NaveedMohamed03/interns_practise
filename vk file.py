l=["vinoth","mohamad naveed","vijay"]
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if len(l[i])<len(l[j]):
            l[i],l[j]=l[j],l[i]
print(l[0])

"""
1.take a list of strings
2.for loop to iterate and check the condition
3.after sorting print the first  element
"""