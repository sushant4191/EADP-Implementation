flag=0
while(flag==0):
    import random
    q=[]
    a=[x for x in range(65,91)]
    for f in range(48,58):
        a.append(f)
    for e in range(97,123):
        a.append(e)
    a.append(35)
    a.append(42)
    matrix=[]
    for i in range(0,8):
        inArray=[] 
        for j in range(0,8):
            c=a[random.randint(0,len(a)-1)]
            a.remove(c)
            inArray.append(chr(c))
        matrix.append(inArray)
    print("Enter The Number of passcode Digits:")
    num=int(input())
    for i in range(len(matrix)):
        print(matrix[i])
    for r in range(num):
        l=random.randint(0,7)
        p=random.randint(0,7)
        q.append(matrix[l][p])
    print("The Dynamic Code is:-")
    for k in q:
        print(k," ",end="")
    print("\nTo Continue Generating Passwords \n i. Press 0 Else \n ii.Press 1 to exit!")
    ch=int(input())
    if(ch==0):
        flag=0
    elif(ch==1):
        flag=1
print(q)