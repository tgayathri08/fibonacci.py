n=int(input("enter num:"))
f1=0
f2=1
i=0
while (i<n):
    print(f1, end=", ")
    i+=1
    next=f1+f2
    f1=f2
    f2=next
print()

