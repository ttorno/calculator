#say welcome
print("welcome to my tip calculator")
#ask the total bill we need to use input function here
bill = input("what was the total bill? ")
float(bill)
#ask how many people need to split the bill
people = input("how many people need to split this bill? ")
float(people)
#ask the percentage and give options
percentage = input("What percentage would you like to tip? 10, 12, or 15? ")
a = str(10)
b = float(.10)
b = float(a)

c = str(12)
d = float(.12)
d = float(c)

e = str(15)
f = float(.15)
f = float(e)

#math
#get money and divide by people
new_money = float(float(bill)/float(people))
#get new money times by percentage which gives result
result = float(new_money * .10)
result_2 = float(new_money * .12)
result_3 = float(new_money * .15)
#get new money add by result
if percentage == a:
  print(new_money + result)
if percentage == c:
  print(new_money + result_2)
if percentage == e:
  print(new_money + result_3)

#give  result
