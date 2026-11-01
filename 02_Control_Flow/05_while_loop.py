# Loop are used to repeat instruction
# count = 1
# while count <= 5 :
#     print("hello")
#     count += 1
    

# i = 1
# while i <= 100000:
#     print("Nazir", i)
#     i+= 1


# print numbers from 1 to 5

# i = 1
# while i <=5:
#     print(i)
#     i +=1


# i = 5
# while i >= 1:
#     print(i)
#     i -= 1

# print("Loop ended")


# some prctice question
# qus1
# i = 1
# while i <= 100:
#     print(i)
#     i += 1

# qus2
# i = 100
# while i >= 1:
#     print(i)
#     i -= 1

#qus3
# n = int(input("enter number : "))
# i = 1
# while i <= 10:
#     print(n*i)
#     i += 1


#qus 4
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
while idx < len(nums):
    print(nums[idx])  #nums[0], nums[1], nums[2]...
    idx+=1


# ques 5
# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# heros = ["ironman", "thor", "superman", "batman"]

# i = 0
# while i < len(heros):
#     print(heros[i])
#     i += 1


nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 36
i = 0
while i < len(nums):
    if(nums[i] == x):
        print("FOUND at index", i)
    else:
        print("finding..")
    i += 1       