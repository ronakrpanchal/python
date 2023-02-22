def remove():
    s1=input("enter the string= ")
    s2=input("string to be removed= ")
    lr=len(s2)
    i=s1. find(s2)
    print("the final string is",s1[:i]+ s1[i+lr:])
remove()    
