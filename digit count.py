def dig():
    a=int(input("a= "))
    count=0
    while(a>0):
       count=count+1
       a=a//10
    print("no. of digits is",count)
dig()
    
