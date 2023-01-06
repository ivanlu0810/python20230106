while True:
    i=int(input())
    if i >31:
        print('輸入不能超過31')
    else:
        print(1<<i)