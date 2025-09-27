a, b = 10, "10" # we can change "10" to 10 but not 10.20 to 10, (String to int posible NOT float to int in " " )

c = int(b)

sum = a + c

print(sum)

print(type(sum))

num1 = 50
num2 = "50"

typeCast = int(num2)

strToint = num1 + typeCast
intToFloat = float(num1)

totalSum = strToint + intToFloat

print(totalSum)

