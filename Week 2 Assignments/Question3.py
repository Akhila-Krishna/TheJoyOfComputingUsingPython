#Write a program that takes cost price and selling price as input and displays whether the transaction is a Profit or a Loss or Neither.
#INPUT FORMAT
#The first line contains the cost price.
#The second line contains the selling price.
#OUTPUT FORMAT
#Print "Profit" if the transaction is a profit or "Loss" if it is a loss. If it is neither profit nor loss, print "Neither". (You must not have quotes in your output)

c=int(input())
s=int(input())
if(c<s):
    print("Profit")
if(c>s):
    print("Loss")
if(c==s):
    print("Neither")
