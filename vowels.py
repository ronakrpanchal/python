def count():
    s=input("enter the string= ")
    v="aeiouAEIOU"
    c=0
    for i in s:
        if i in v:
            c+=1
    print("no of vowels =",c)
count()
