while True:
    x,y,z=map(int,input().split())
    if x<y<z:
        print('最小值:'+str(x))
    if z<x<y:
        print('最小值:'+str(z))
    if y<z<x:
        print('最小值:'+str(y))
        

        