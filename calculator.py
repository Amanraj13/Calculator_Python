print("\nPlease use the correct expression to avoid errors\n")
print("\nTo Add two number enter: + ")
print("\nTo substract two number enter: -")
print("\nTo Multiply two number enter: *")
print("\nTo divide two number enter: /")
print("\nTo find square  of two number enter: S")
print("\nTo find cube of two number enter: C ")
choice=input("\nEnter your choice:")


if(choice=='+'):
    num1=float(input("\nEnter the first number:"))
    num2=float(input("\nEnter the second number:"))
    sum1=num1+num2
    print("\nThe sum of the two number is:",sum1)
elif(choice=='-'):
    num1=float(input("\nEnter the first number:"))
    num2=float(input("\nEnter the second number:"))
    diff=num1-num2
    print("\nThe difference of the two number is:",diff)
elif(choice=='*'):
    num1=float(input("\nEnter the first number:"))
    num2=float(input("\nEnter the second number:"))
    product=num1*num2
    print("\nThe product of the two number is:",product)
elif(choice=='/'):
    num1=float(input("\nEnter the divident:"))
    num2=float(input("\nEnter the divisor:"))
    quotient=num1/num2
    print("\nThe quotient is:",quotient)
elif(choice=='S'):
    num1=float(input("\nEnter the number:"))
    square=num1*num1
    print("\nThe square of the number is:",square)
elif(choice=='C'):
    num1=float(input("\nEnter the number:"))
    cube=num1*num1*num1
    print("\nThe cube of the number is:",cube)
else:
    print("\nWrong choice entered. Please try again")
    

    
