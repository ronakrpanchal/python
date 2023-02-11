def rect():
    l=int(input("length= "))
    b=int(input("base= "))
    a=l*b
    p=2*(l+b)
    if a>p:
        print("area is greater than perimeter")
    else:
        print("area is equal to perimeter")
rect()
