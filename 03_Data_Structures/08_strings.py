# str1 = "This is a string.\nwe are creating it in python."
# print(str1)

# str2 = 'ApnaCollege'
# str3 = """this is a string"""
# this is apnacollege

# str1 = "Nazir"
# str2 = "Ansari"
# final_str = str1 + " " + str2
# print(final_str)
# # print(str1 + str2)
# print(len(final_str))

# str = "Sandeep"
# print(len(str))
# len1 = len(str)
# print(len1)

# str = "Nazir ansari"
# char = str[0]
# char = str[5]
# print(char)

# str = "javascript"
# print(str[1:4])
# print(str[0:6])
# print(str[0:10])
# print(str[3:len(str)])
# print(str[3:])  # yeh index 3 ke baad aage last tk chalegi 
# print(str[:2])


# str = "sultan"
# print(str[-3:-1])
# print(str[-5:-1])
# print(str[-6:])


# string function _____________________________________
# endswith() 
# str = "I am studing python from apnacollege"
# print(str.endswith("ege"))  # str.endswith("") result true false deta h agr last ki value jo print kra rhe usme match ho gyi to
# print(str.endswith("abe"))

# #capitalize()
# str = "i am Nazir Ansari"
# print(str.capitalize())  # yeh suru ka letters capital kr deta h

# str = "neha ji"
# str = str.capitalize()  # yha str ko capitalize hi print krega
# print(str.capitalize())
# print(str)


#replace()

# str = "i am from apnacollege"
# print(str.replace("o", "b"))  #yha o k jagah b replace ho jayega.
# print(str.replace("from", "learning"))


#find()

# str = "i am from apnacollege"
# print(str.find("o")) #ye find krta h aur index khoj kr deta h
# print(str.find("from"))
# print(str.find("q")) # yha -1 dega kyuki q exist hi m=nhi krta hai


#count 

# str = "I am from uttar pradesh from india"
# print(str.count("from"))
# print(str.count("a"))


# some prqactice question
#1.
# str = input("Enter your name:")
# print("Length of your name is:",len(str))

#2.
# str = "hello!, $i am the $ symbol $99.99"
# print(str.count("$"))