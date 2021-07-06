# CreditInterestRate.py
**This program takes a credit card balance and its annual interest rate to find the lowest monthly payment to pay it off in a year.**

Let's start off with a credit card that has a balance of $5,000 and a 20% annual interest rate. we can define two values: `balance = 5000` and `annualInterestRate = 0.2`. 

Using a method called bisection search, we can quickly find the lowest monthly payment to pay off that balance within the year. 

**What is bisection search?**

### Bisection Search

We know that the square root of x lies between 1 and x, from mathematics. Rather than exhaustively trying things starting at 1,
suppose instead we pick a number in the middle of a range from 1 to x. We'll call it g.

Now if we're lucky, g is close enough. But if it's not close enough, is the guess too big or too small?

If `g**2 > x`, then we know that g is too big. We can eliminate the entire range from g to x. Now the "new g" is in the middle of 1 and g.

And if, for example, this "new g" is such that `g**2 < x`, then we know that it's too small. Now we can search only from "new g" to g, with a "next g" in the middle.

Eventually we will find the approximate answer to the square root of x.

The bisection search method is so much faster than the linear search method because it can eliminate half the range of guesses with each iteration,
while the linear method runs through every possible guess until the answer is found.

### Variables

Let's define some variables for the bisection search.

`newBalance = balance` - this will allow us to use the balance variable without changing the starting balance itself.

`monthIntRate = (annualInterestRate) / 12.0` - this provides our monthly interest rate.

`epsilon = 0.01` - this acts as our margin of error. Let's make it within the nearest cent.

`low = newBalance / 12.0` - our lowest possible monthly payment.

`high = (newBalance * (1 + monthIntRate)**12) / 12.0` - our highest possible monthly payment.

`monthlyPayment = (high + low) / 2.0` - The midpoint between high and low variables, and our eventual answer.

### The Program

    while abs(high - low) >= epsilon:

      for month in range(12):
    
        newBalance -= monthlyPayment
        
        newBalance += monthIntRate * newBalance
        
As long as the absolute value of our highest guess - our lowest guess is greater than or equal to our margin of error, our program will run.

For every month in a year, we update our newBalance to reflect a monthly payment and a monthly interest rate charged to the card.

    if newBalance > 0:
    
      month = 0
      
      newBalance = balance
        
      low = monthlyPayment
        
Once the for loop is ran for all 12 months, check if the newBalance is completely paid off. If newBalance is above 0, reset the month and 
newBalance variables and make the lowest point the monthlyPayment variable, which was the previous midpoint. The for loop will start again.

    else:
    
      month = 0
      
      newBalance = balance
      
      high = monthlyPayment
      
If newBalance is below 0, we're still resetting the month and newBalance variables, but the monthlyPayment variable, which was previously the midpoint,
is now the highest point. The for loop will start again.

Eventually the program will find an approximate answer within our margin of error and the while loop will stop. We use

    print('Lowest Payment: ' + str(round(monthlyPayment, 2)))
    
to print out our results. In this case, our answer should be `Lowest Payment: 455.58`.
