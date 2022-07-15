# Program to display the Fibonacci sequence up to n-th term or the Fibonacci number closer to a certain number F

# Function to find the Fibonacci number which is closest to F
def nearestFibonacci(num):
    # Base Case
    if (num == 0):
        print(0)
        return
 
    # Initialize the first & second terms of the Fibonacci series
    first = 0
    second = 1
 
    # Store the third term
    third = first + second
 
    # Iterate until the third term
    # is less than or equal to num
    while (third <= num):
         
        # Update the first
        first = second
 
        # Update the second
        second = third
 
        # Update the third
        third = first + second
 
    # Store the Fibonacci number having smaller difference with N
    if (abs(third - num) >=
        abs(second - num)):
        ans =  second
    else:
        ans = third
 
    # Print the result
    print(ans)
 
def sequenceFibonacci(num):
    
    # first two terms
    n1, n2 = 1, 1
    count = 0

    # check if the number of terms is valid
    if num <= 0:
       print("Please enter a positive integer")
    # if there is only one term, return n1
    elif num == 1:
       print("Fibonacci sequence upto",num,":")
       print(n1)
    # generate fibonacci sequence
    else:
       print("Fibonacci sequence:")
       while count < num:
           print(n1)
           nth = n1 + n2
       # update values
           n1 = n2
           n2 = nth
           count += 1

# Driver Code

count = 0
while count==0:
   a = (input('Type 1 if you want sequence number (n) or type 2 if you want the Fibonacci number closest to given number (F): '))
   if a=='1':
      n = int(input("How many terms? "))  
      sequenceFibonacci(n)
      count += 1
   elif a=='2':
      F = int(input("Please input F: "))
      nearestFibonacci(F)
      count += 1
   else:
      print('Input error.')