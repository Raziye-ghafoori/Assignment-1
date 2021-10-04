print('enter heigh:')
h=float(input())
print('enter weight:')
w=int(input())

BMI=w/(h*h)

if BMI<18.5:
    print('you are  underweight')
elif BMI>=18.5  or BMI<=24.9:
        print('you are  normal')
elif BMI>=25 or BMI<=29.9:
         print('you are  overweight')
elif BMI>=30 or BMI<=34.9 :
       print('you are  obese')
elif BMI>=35:
     print('you are  extremely obese')


