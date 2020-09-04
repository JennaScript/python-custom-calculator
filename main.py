#Hello there! Jennalyn here! I hope this program is not too controversial. LOL. I wrote this to help a bit with the confusion between the actual marijuana prices and the taxes. Cannabis is now legal in California. :)

print ("This application was created to compute the amount of your cannabis strain with our dispensary tax, local county tax, and overall state tax. I hope this helps you in any way at all. :)")

print ("Marijuana Strain Price:")

amount = float(input())

print ("Amount of Strain:", amount)

dispensaryTax = amount * 0.05

print ("Dispensary Tax:", format (dispensaryTax, '.2f'))

countyTax = amount * 0.02

print ("County Tax:", format (countyTax, '.2f'))

stateTax = amount * 0.09

print ("State Tax:", format (stateTax, '.2f'))

totalTax = dispensaryTax + countyTax + stateTax 

print ("Total Tax:", format (totalTax, '.2f'))

subtotal = amount + totalTax

print ("Subtotal of Sale:", format (subtotal, '.2f'))

print ("Thank you so much for using this . :D")