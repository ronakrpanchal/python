def collinear():
    x1=int(input("x1= "))
    y1=int(input("y1= "))
    x2=int(input("x2= "))
    y2=int(input("y2= "))
    x3=int(input("x3= "))
    y3=int(input("y3= "))
    a = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
 
    if (a == 0):
        print("collinear")
    else:
        print ("not collinear")
collinear()        
