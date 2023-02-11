def circle():
    x=int(input("x= "))
    y=int(input("Y= "))
    r=int(input("r= "))
    a=pow(pow(x,2)+pow(y,2),1/2)
    if a==r:
        print("(",x,",",y,")","lies on the circle")
    elif a>r:
        print("(",x,",",y,")","lies outside the circle")
    else:
        print("(",x,",",y,")","lies inside the circle")
circle()
