l=["vinoth","mohamad naveed","vijay"]
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if len(l[i])<len(l[j]):
            l[i],l[j]=l[j],l[i]
print(l[0])
