# marks = 88.2
# marks = 34.6 
# marks = 56.8   
# marks = 64.3  # inko yek sath likhne me bada ho jayega isliye list item use kijiye
# marks = 23.7

# marks = [88.2, 34.6, 56.8, 64.3, 23.7]
# print(marks)
# print(type(marks))


# marks = [87, 64, 33, 95, 76]
# print(marks[3])


# student = ["Karan", "85", "Delhi"]
# print(student[2])
# student[0] = "Nazir"
# print(student)



# marks = [87, 64, 33, 95, 76]
# print(marks[1:4])
# print(marks[2:])
# print(marks[:])
# print(marks[-3:-1])
# print(marks[:-1])


# ________________________List Method___________________

# .append(4) method_________________valuee add krna
# list = [2, 1, 3]
# list.append(4)
# print(list)


# .extend() method___________ek list me dusri list ke multiple element add karne kke liye hota h .
# a = [10, 20, 30]
# b = [40, 50, 60]
# a.extend(b)
# print(a)


# defference between append & extend
# a = [10, 20]
# a.append([30, 40])  # append yha [30, 40] yese print ho rha h
# print(a)

# a = [10, 20]
# a.extend([30, 40])  #extend yha sab yek hi klist ppe print ho rhe hainn
# print(a)



# .sort method ___________________sahi order me arrange kr dena 

# list = [6, 3, 2, 8]
# print(list.append(4))
# print(list.sort())
# print(list)


# .sort(reverse = True)_________________desending order me bna dega
# list = ["Banana", "Apple", "litchi"]
# list = ['a', 'o', 'd', 'l']
# # print(list.append(4))
# print(list.sort(reverse=True))
# print(list)


# .reverse()______________________yek ulta deta h value reverse bna deta h 
# list = ['g', 'h', 'a', 'd']
# print(list.reverse()) yese none dega value
# list.reverse()
# print(list)


# .insert()________specific index par element add karta h

# marks = [3, 4, 5]
# marks.insert(1, 2)
# print(marks)


# .remove() methode__________list se kisi specific value ko delete karne k liye hota h
# list = [2, 4, 5, 6]
# list.remove(2)
# print(list)


# .pop() methode_____________kisi index ko bta kr us value ko gayab krta h, aur ye removed element ko return bhi krta hai

# list = [1, 2, 3, 4]
# list.pop(3)
# print(list)


# yha index nhi  diya hua h 
# a = [10, 20, 30, 40]
# x = a.pop()
# print(x)
# print(a)

# yha index diya gya h
# a = [10, 20, 30, 40]
# a.pop(2)
# print(a)


# clear()_____puri list ko empty karne ke liye  hota h.
# a = [10, 20, 30, 40]
# a.clear()
# print(a)

# a = [10, 20, 30, 40]
# del a[2]
# print(a)



# index()___kisi element ka position find krne ke liye
# a = [10, 30, 40, 50]
# print(a.index(30))

# agr same value multiple baar ho to 
# a = [30,20,10,10,50]
# print(a.index(10))


# count________koi value list me kitni  baar aayi h ye pta krta h
# a = [10, 20, 40, 20, 50]
# print(a.count(20))


# copy()
# a = [20, 30, 40]
# b = a.copy()
# print(b)

# a = [10, 20, 30]
# b = a.copy()

# b.append(40)
# print(a)
# print(b)