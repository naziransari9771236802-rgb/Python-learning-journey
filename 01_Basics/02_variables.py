name = "Nazir Ansari"
age = 25
price = 25.80

age2 = age
print("My name is :", name)
print("my age is :", age)
print("my price is :", price)
print("my age2 is :", age2)

print(type(name))
print(type(age))
print(type(price))


# ===============================================================
                        #  Practice Exercise
# ==================================================                      
# Example 1: String Variable
name = "Nazir"
print(name)

# Example 2: Integer Variable
age = 21
print(age)

# Example 3: Float Variable
price = 99.50
print(price)

# Example 4: Boolean Variable
is_student = True
print(is_student)

# Example 5: Multiple Variables
name = "Nazir"
age = 21
city = "Lucknow"

print(name)
print(age)
print(city)

# ========================================================================

# Multipkle variable Assignment__________________

name, age, city = "Nazir", 21, "Lucknow"
print(name)
print(age)
print(city)


# ===========================================================
                #   Rules of Naming Variables
# =============================================================
# This is Valid Name Variable________________

# name = "Nazir"
# user_age = 21
# _marks = 85
# student1 = "Ali"

# This is Invalid Names______________________
# 1name = "Nazir"  # Cannot start with a number
# user age = 21    # Spaces are not allowed
# class = "BCA"    # 'class' is a Python keyword

# Practice_____________
name = "Nazir Ansari"
age = 21
city = "Lucknow"
course = "BCA"
print(name)
print(age)
print(city)
print(course)


# Practice____________
student_name = "Nazir Ansari"
mathematics_marks = 89
english_marks = 90
python_marks = 95

print(student_name)
print(mathematics_marks)
print(english_marks)
print(python_marks)


# Practice_____________
name = "Nazir"
age = 21
city = "Lucknow"

print(f"My name is {name}. I am {age} Year old and I live in {city}.")


# Practice________________
a = 10
b = 20
c = 30
total = a + b + c
print(total)


# Practice_________________
x = 50
y = 100

x, y = y, x

print("x =", x)
print("y =", y)