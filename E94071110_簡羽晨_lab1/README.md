This folder contents five files of lab1:  

## RockPaperScissors
Name the file __*RockPaperScissors.ipynb*__.  
Write a program to play Rock, Paper, Scissors game. The game will  
(1) Ask you to enter Rock, Paper, or Scissors.  
(2) Randomly generates Rock, Paper, or Scissors.  
(3) Determine whether it is a win, tie or loss. The game will quit when you hit the first win.  

## ReverseNumber
Name the file __*ReverseNumber.ipynb*__.  
Write a function `def reverse(number)` to display an integer in reverse order and a test script that prompts the user to enter an integer and displays its reversal. For example, `reverse(3456)` displays `6543`.  
  
Hint and Note: The main reversal logic can be solved in multiple ways. For example, you can convert the number into a string and reverse the string. You can also store all the numeric values into a list (covered in the later module) and reverse the contents. For now, please try to solve the problem at its most naïve and algorithmic way. Think of the combo usage of `while loop, %, // `.  
  
## RemoveOutliers
Name the file __*RemoveOutliers.ipynb*__.  
When analyzing data collected as part of a science experiment it may be desirable to remove the most extreme values before performing other calculations.  
1. Write a function `remove_outliers` that takes a list of values and a non-negative integer, n, as its parameters. The function should return a list with the n largest elements and the n smallest elements removed and a list of outliers.  
2. Write a Python program that demonstrates your function. It should prompt the user to input the number n, a few data, signify the end of input with ‘q’ or ‘Q’, and remove the n largest and n smallest values from it by calling the function described previously. Display the original list, the list with the outliers removed, and the outliers.
  
## Nine_Coins
A coin has two states: 0 (head) and 1 (tail).  
Name the module __*nine_coins.py*__ and inside the module, write `class Nine_Coins` to represent states of nine coins. Since there are a total of 512 (2^9) possibilities, we can use the decimal numbers 0, 1, 2, 3, ..., and 511 to represent all states of the nine coins. The initial states of these nine coins can thus be set by a decimal number. For example, 7 represents the binary number 000000111 and corresponds to the states of HHHHHHTTT. In addition, when the client calls the toss *method* of an *object* of the Nine_Coins class, all the coins will be flipped randomly and all the states shall be updated.  
Use the client codes to test your implementation (the client codes are included in the __*Nine_Coins_Client.ipynb*__).
