while True:
    x,y=map(int,input().split())
    if x>=0 and x<=100 and y>=0 and y<=100:
        print('inside')
    else:
        print('outside')
