a=int(input())
if a%4==0:
    print('ost 0')
else:
    if a%4:
        print('ost 1')
    else:
        if a%4==2:
            print('ost 2')
        else:
            print('ost 3')