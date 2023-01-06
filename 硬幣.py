while True:
    x=int(input())
    print('NT50={}'.format(x//50))
    x %=50
    print('NT10={}'.format(x//10))
    x %=10
    print('NT5={}'.format(x//5))
    x %=5
    print('NT1={}'.format(x))