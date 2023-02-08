def ls3():
    a=int(input("a= "))
    b=int(input("b= "))
    c=int(input("c= "))
    l=max(a,b,c)
    s=min(a,b,c)
    if l==s:
        print("all are same")
    else:
        print(l,"largest",s,"smallest")
ls3()
        
