info = {
    "name" : "Nazir",
    "age" : 22,
    "course" : "BCA",
    "city" : "Lucknow"
}

# dictionary methode used krne wale hain
#1. keys() _____info me jitna keys h o sab de deta h 
# print(info.keys())

#2.values()_______dictionary ki saari value deta h
# print(info.values())

#3. items()_________key+ value dono deta h
# print(info.items())

#4. get()__________kisi key ki value nikalta h 
# print(info.get("name"))

#agr koi key nhi h aur use nikalne ki kosis karenge to None print hoke aayegi.
# print(info.get("phone"))
# print(info.get("phone", "not available"))  # default value bhi de sakte hain.

#5. update()________nayi information add ya purani information update karta h.
# info.update({"age" : 23}) # yha age update ho gyi
# print(info)

# info.update({"phone": "7865342342"}) # yha update bhi ho gyi
# print(info)

# info.update({    # agr yek sath dher sara add krni ho to
#     "phone" : "8756875324",
#     "country" : "India"
# })
# print(info)


# 6. pop()____specific key ko remove kr deta h
# info.pop("city")
# print(info)

#7. popitem()___dictionary ka last key-value remopve krtta h .
# info.popitem()
# print(info)

#8. clear()______puri dictionary ko empty kr deta h
# info.clear()  # dectionary delete nhi hoti hai bs empty hoti h.
# print(info) 


# 9. copy()______dictionary ki copy bnata h 
# info2 = info.copy()
# print(info)


# 10. setdefault() ____________age key alreay hai to kuch nhi hoga , warna add ho jayega.
# info.setdefault("name", "Aman") #name phle se hi set h mere me
# print(info)

# # but
# info.setdefault("phone", "78563423788")  # yhjaa agr phonr nhi h to add ho jayega.
# print(info)



# some practice queastion ______________

info = {
    "name": "Nazir",
    "age": 22,
    "course": "BCA",
    "city": "Lucknow"
}
# print(info.keys())
# print(info.values())
# info.update({"phone" : "8756432323"})
# print(info)
# # info.update({"city" : "prayagraj"})
# # print(info)
# print(info.get("age"))
# info.pop("course")
# print(info)

