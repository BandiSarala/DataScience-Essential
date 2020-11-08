#!/usr/bin/env python
# coding: utf-8

# # Questions 1:
# # Given the following jumbled word, OBANWRI guess the correct English word.
# # A. RANIBOW
# # B. RAINBOW
# # C. BOWRANI
# # D. ROBWANI¶

# In[1]:


correctword = "RAINBOW"
lst = ["RANIBOW","RAINBOW","BOWRANI","ROBWANI"]
for i in lst:
    
    if(i == correctword):
        print("RAINBOW")


# # Questions 2:
# # Write a program which prints “LETS UPGRADE”. (Please note that you have to print in ALL CAPS as given)¶

# In[2]:


print("LETSUPGRADE")


# # Questions 3:
# # Write a program that takes cost price and selling price as input and displays whether the transaction is a
# # Profit or a Loss or Neither.
# # INPUT FORMAT
# # The first line contains the cost price.
# # The second line contains the selling price.
# # OUTPUT FORMAT
# # Print "Profit" if the transaction is a profit or "Loss" if it is a loss. If it is neither
# # profit nor loss, print "Neither". (You must not have quotes in your output)

# In[3]:


costprice = int(input())
sellingprice = int(input())

profit = sellingprice - costprice 
loss = costprice - sellingprice

if profit > loss:
    print("Profit")
elif loss > profit:
    print("Loss")
else:
    print("Neither")


# # Questions 4:
# # Write a program that takes an amount in Indian Rupees as input. You need to find its equivalent in Euro and display it. Assume 1 Euro equals Rs. 80.
# # Please note that you are expected to stick to the given input and output format as in sample test cases. Please don't add any extra lines such as 'Enter a number', etc.
# # Your program should take only one number as input and display the output.

# In[4]:


rup = int(input())
eur = rup * 80
print(eur)


# In[ ]:




