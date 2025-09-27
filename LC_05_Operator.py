num1 = 10
num2 = 20

num3 = 100
num4 = 200

num6 = 1
num7 = 2

num8 = 5
num9 = 5

num10 = 6

# 1. > Arithmetic Operators (+, -, *, /, %, **)
print("Arithmetic Operators:")
print("num1 + num2 =", num1 + num2)    # 10 + 20 = 30
print("num1 - num2 =", num1 - num2)    # 10 - 20 = -10
print("num1 * num2 =", num1 * num2)    # 10 * 20 = 200
print("num1 / num2 =", num1 / num2)    # 10 / 20 = 0.5
print("num1 % num2 =", num1 % num2)    # 10 % 20 = 10
print("num1 ** num6 =", num1 ** num6)  # 10 ** 1 = 10
print()

# 2. > Relational Operators (==, !=, >, <, >=, <=)
print("Relational Operators:")
print("num8 == num9:", num8 == num9)   # 5 == 5 → True
print("num8 != num6:", num8 != num6)   # 5 != 1 → True
print("num8 > num10:", num8 > num10)   # 5 > 6 → False
print("num8 < num10:", num8 < num10)   # 5 < 6 → True
print("num8 >= num6:", num8 >= num6)   # 5 >= 1 → True
print("num9 <= num6:", num9 <= num6)   # 5 <= 1 → False
print()

# 3. > Assignment Operators (=, +=, -=, *=, /=, %=, **=)
print("Assignment Operators:")
x = num1  # x = 10
print("Initial x =", x)

x += 5   # x = x + 5 → 15
print("x += 5 →", x)

x -= 3   # x = x - 3 → 12
print("x -= 3 →", x)

x *= 2   # x = x * 2 → 24
print("x *= 2 →", x)

x /= 4   # x = x / 4 → 6.0
print("x /= 4 →", x)

x %= 5   # x = x % 5 → 1.0
print("x %= 5 →", x)

x **= 3  # x = x ** 3 → 1.0
print("x **= 3 →", x)
print()

# 4. > Logical Operators (not, and, or)
print("Logical Operators:")
print("not(num6 > num7):", not(num6 > num7))     # not(1 > 2) → True
print("(num6 < num7) and (num8 == num9):", (num6 < num7) and (num8 == num9))  # True and True → True
print("(num6 > num7) or (num8 == num9):", (num6 > num7) or (num8 == num9))    # False or True → True
