# data types in python
# 1. Integrers
# 2. Strings
# 3. Float
# 4. Boolean
# 5. None


# name1 = "sk"
# name2 = 'sk'
# name3 = '''sk'''

# print(name1)
# print(name2)
# print(name3)


# age = 23
# old = True
# a = None

# print(type(old))
# print(type(a))
# print(type(age))



# a = 223
# b = 50
# sum = a % b 
# # yha sum variable me +, - , *, /, % ye operators ka use karke value store kar sakte hai.
# print(sum)


# arithmetic operators________________________________________--
# a = 9
# b = 4
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a % b)  #remainder
# print(a ** b) # a^b



# relational oprerators____________________________________
# a = 50
# b = 30
# print(a == b) 
# print(a != b) 
# print(a >= b) 
# print(a <= b)
# print(a < b)
# print(a > b)
# print(a <= b)


# Assignment Operators________________________________________________


# | Operator | Matlab       | Example   | Result |
# | -------- | ------------ | --------- | -----: |
# | `=`      | Assign       | `x = 10`  |     10 |
# | `+=`     | Add          | `x += 5`  |     15 |
# | `-=`     | Subtract     | `x -= 5`  |      5 |
# | `*=`     | Multiply     | `x *= 5`  |     50 |
# | `/=`     | Divide       | `x /= 5`  |    2.0 |
# | `//=`    | Floor Divide | `x //= 3` |      3 |
# | `%=`     | Remainder    | `x %= 3`  |      1 |
# | `**=`    | Power        | `x **= 2` |    100 |


# num = 10
# num ** 3

# num += 10
# num -= 10
# num *= 10
# num %= 10
# num /= 10
# num ** 10
# print("num:" , num)



# Logical Operators_________________________________________
# a = 10
# b = 5
# print(not False)   # jo False hota h o true me badal jata h  aur jo true hota h false me badal jata h
# print(not True)
# print(not (a > b))

# and operator tabhi true hoga jab dono value true ho.
# val1 = True
# val2 = False
# print("and operator:", val1 and val2)


# or operator tabhi true hoga jab koi bhi value true ho.
# print("or operator:", val1 or val2)
# print ("or operator:", (a == b) or (a > b))


# Membership Operators
# in – Check karta hai ki koi value sequence ke andar present hai ya nahi.
# not in – Check karta hai ki koi value sequence ke andar present nahi hai ya nahi.

# name = "Nazir Ansari"

# print("Nazir" in name)
# print("Python" in name)

# print("Python" not in name)
# print("Ansari" not in name)




# Bitwise Operators
# & (AND) – Dono bits 1 hone par 1 return karta hai.
# | (OR) – Koi ek bit 1 hone par 1 return karta hai.
# ^ (XOR) – Dono bits alag hone par 1 return karta hai.
# ~ (NOT) – Bits ko reverse karta hai.
# << (Left Shift) – Bits ko left side shift karta hai.
# >> (Right Shift) – Bits ko right side shift karta hai.

# a = 5
# b = 3

# print(a & b)   # AND
# print(a | b)   # OR
# print(a ^ b)   # XOR
# print(~a)      # NOT
# print(a << 1)  # Left Shift
# print(a >> 1)  # Right Shift

# type conversion ______________________________________

# a = int("2") # yha float bhi kr sakte hain.
# b = 5.5
# print(type(a))
# print(a + b)


# a = float("2") 
# b = 5.5
# print(type(a))
# print(a + b)

# a = 3.14
# a = str(a)
# print(type(a))




# user se input kaise lenge_______________________________

# 1. String input_____________________________
# name = input("Enter your name: ")
# print("Hello", name)

# name = input("Enter your name: ")
# print("Welcome", name)

# work = input("Enter your work: ")
# print("My work is", work)



# 2. Integer input____________________________________
# age = int(input("Enter your age: "))
# print("My age is:", age)


# val = input("Enter your value: ")
# print("My alue is: ", val)


# # 3. Float input____________________________________
# height = float(input("Enter your height:"))
# print("My height is: ", height)

# 4. do number ka addition karna_____________________________
# a = int(input("Enter your num: "))
# b = int(input("Enter your another num: "))
# print("Addition =", a + b)




# name = input("enter name: ")
# age = input("enter age: ")
# marks = input("enter marks: ")

# print("Welcome", name)
# print("Age =", age)
# print("Marks =", marks)




# practice question  _-----------------------------
# 1. kisi do number ko sum krna h

# first = int(input("enter first: "))
# second = int(input("enter second: "))
# print("sum =", first + second)


# 2. 
# side = float(input("enter square side: "))
# print("area =", side * side)


# 3.
# a = float(input("enter first: "))
# b = float(input("enter second: "))
# print("avg =", (a+b)/2)

# 4.
# a= int(input("enter first: "))
# b = int(input("enter second: "))
# print(a >= b)