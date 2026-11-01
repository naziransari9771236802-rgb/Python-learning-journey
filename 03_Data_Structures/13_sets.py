#  set = unique values ka collection.
#  set = unorder collection hai.

# number = {1, 2, 3, 4, 5}
# print(number)

# numbers = {1, 2, 3, 4, 4, 2, 5}  # yha dublicate gaayb ho ja rha h
# print(numbers)

# .add()
# numbers = {10, 20, 30}
# numbers.add(40)  # set unordered collection h isliye kahi bhi add ho jayega.
# numbers.add(50)
# print(numbers)

# fruits = {"apple", "banana", "mango"}
# fruits.add("orange")
# print(fruits)


#  .remove()____element remove , na mile to error
# numbers = {20, 30, 40, 50}
# numbers.remove(40) # yha remove kr deta  h , agr value na mile to error deta h 
# print(numbers)

# colors = {"red", "blue", "green", "yellow"}
# colors.remove("green")
# colors.remove("black")  # yha blaack nhi h isliye error batayega.
# print(colors)


# .discard()________agr value mile to remove aur na mile to error nhi 
# numbers = {70, 32, 45, 63}
# numbers.discard(45)
# numbers.discard(31)
# print(numbers)


# fruits = {"apple", "banana", "mango"}
# fruits.discard("banana")
# print(fruits)
# fruits.discard("orange")
# print(fruits)


# .pop()____set se yek element remove krta h . lekin hme pta nhi h kon remove kr sakta h 
# numbers = {10, 20, 30, 40}
# numbers.pop()
# print(numbers)


# numbers = {10, 20, 30, 40}
# removed = numbers.pop()
# print("Removed:", removed)
# print("Remaining:", numbers)


# numbers = {10, 20, 30}
# x = numbers.pop()  # yhA PTA CHAL jayega kon remove hua h kon nhi
# print(x)  


# fruits = {"apple", "banana", "mango"}
# removed = fruits.pop()
# print("Removed:", removed)
# print("Remaining:", fruits)


# set()_____pura set empty karta hai
# s = {10, 20, 30}
# s.clear()
# print(s)


# copy()____set ki yek seperate copy banane ke liye hota hai
# s1 = {10, 20, 30}
# s2 = s1.copy()
# print(s2)


# s1 = {10, 20, 30}
# s2 = s1.copy()
# s2.add(40)
# print(s1)
# print(s2)

 
# union____do ya do se jyada sets ke saare unique elements ko ek sath laane ke liye hota hai
# a = {1, 2, 3}
# b = {3, 4, 5}
# c = a.union(b)
# print(c)
# print(a | b) 
    


# Intersection___________do sets me jo common hai , unhe nikalne ke liye 
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# c = a.intersection(b)
# print(c)
# print(a & b)
 

# defference ______phle set me jo element hain, lekin dusre set me nhi hian, unhe nikalne ke liye hota h .
a  = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.difference(b))
print(a - b)
# print(b - a)


# symmetric_difference()______dono sets ke woh element deta h jo common nhi h 
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# print(a.symmetric_difference(b))
# print(a ^ b)