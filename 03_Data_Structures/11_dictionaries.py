# info = {
#     # "key" : "value",
#     "name" : "apnanazir",
#     "subject" : ["python", "C", "javascript"],
#     "topic" : ["dict", "set"],
#     # "learning" : "coding",
#     "age" : "32",
#     "is adult" : True,
#     "marks" : 98.23
 
# }
# # print( type(info))

# # print(info["name"])
# # print(info["marks"])

# # info["name"] = "sadhna" # yha name change hua h , 
# # info["age"] = "30"    # yha bhi age change hua h
# # print(info)



# null_dict = {}
# null_dict["name"] = "apnacollege"
# print(null_dict)



# nested dictionary ________________

student = {
    "name" : "Nazir Ansari",
    "subjects" : {
        "math" : 89,
        "english" : 85,
        "computer" : 78
    }
}
# print(student)
# print(student["subjects"]["english"])


# dict method_______________________
# dict.keys _______________
# print(student.keys())
# print(len(student.keys()))
# print(list(student.keys()))


# dict.value______________________




student = {
    "name" : "Nazir",
    "age" : 22,
    "course" : "BCA"
}
# print(student)
# print(student["age"])
# print(student["name"])

# agr mujhe isme add krni h kuch extra enformation to ye karein_____________
student["age"] = 23   # yha student age change hogyi
student["city"] = "kushinagar"
student["village"] = "Tinbardaha"
student["city"] = "khadda" 
student.pop("course")  #yha course gayab ho gya h_______
# course gayab krne ke do syntax hain 
 #1 . student.pop("course")
 #2.  det student["course"]

 
print(student)