def marks():
    a=int(input("Physics= "))
    b=int(input("computer= "))
    c=int(input("maths= "))
    t=a+b+c
    print("total marks=",t)
    avg=t/3
    print("average= ",avg)
    print("grade in physics=")
    if a>0 and a<=39:
        print("fail")
    elif a>39 and a<=44:
        print("P")
    elif a>44 and a<=49:
        print("C")
    elif a>49 and a<=54:
        print("B")
    elif a>54 and a<=59:
        print("B+")
    elif a>59 and a<=69:
        print("A")
    elif a>69 and a<=79:
        print("A+")
    elif a>79 and a<=100:
        print("O")
    else:
        print("NA")
    print("grade in computer=")
    if b>0 and b<=39:
        print("fail")
    elif b>39 and b<=44:
        print("P")
    elif b>44 and b<=49:
        print("C")
    elif b>49 and b<=54:
        print("B")
    elif b>54 and b<=59:
        print("B+")
    elif b>59 and b<=69:
        print("A")
    elif b>69 and b<=79:
        print("A+")
    elif b>79 and b<=100:
        print("O")
    else:
        print("NA")    
    print("grade in maths=")
    if c>0 and c<=39:
        print("fail")
    elif c>39 and c<=44:
        print("P")
    elif c>44 and c<=49:
        print("C")
    elif c>49 and c<=54:
        print("B")
    elif c>54 and c<=59:
        print("B+")
    elif c>59 and c<=69:
        print("A")
    elif c>69 and c<=79:
        print("A+")
    elif c>79 and c<=100:
        print("O")
    else:
        print("NA")    
marks()        
        
