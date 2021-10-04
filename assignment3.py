print('enter 3 numbers:')
a=int(input())
b=int(input())
c=int(input())

if a<b+c:

    if b<c+a:

        if c<a+b:

            print('we craet a triangle')

        else:
            print('we cant crate a triangle')
    else:

        print('we cant crate a triangle')
else:
    print('we cant crate a triangle')