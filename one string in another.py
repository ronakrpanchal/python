def check():
    s1=input("enter the string1= ")
    s2=input("enter the string2= ")
    if s1 in s2:
        print(s1,"is present in",s2)
    elif s2 in s1:
        print(s2,"is present in",s1)
    else:
        print("none of them is present")
check()        
