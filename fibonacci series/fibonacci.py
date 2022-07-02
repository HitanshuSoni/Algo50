seqLen = int(input("Enter how many number sequence you want to print "))

num1, num2 = 0, 1

count = 0

if seqLen <= 0:
    print("Please enter a number number which is greater than zero")

elif seqLen == 1:
    print("Fibonacci sequence of first", seqLen, "is: ", num1)

else:
    print("Fibonacci sequence of First", seqLen, "is: ")
    
    while count < seqLen:
        print(num1)
        temp = num1 + num2
        num1 = num2
        num2 = temp

        count+=1


