import math


# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
# print('moshe')
# print(math.ceil(-7.9))
# print(math.floor(7.99))
# print(round(7.99))ֹ
# print(math.sqrt(169))
# print(math.pow(13,2))
# print(math.factorial(5))
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
#

# a = 55
# b = 4
# c = 19
#
# if a > b:
#     if a > c:
#         print(f'{a} is bigger then {b} & {c}')
#     else:
#         print(f'{c} is bigger then {a} & {b}')
# elif b > c:
#     print(f'{b} is bigger then {a} & {c}')
# else:
#     print(f'{c} is bigger then {a} & {b}')
#
# if a > b >= c:
#     print(f'{a} is bigger then {b} & {c}')
#
#
#

# pin = input("Enter a 4-digit PIN: ")
#
# if pin.isdigit() and len(pin) == 4:
#     print("Success! Valid PIN.")
# else:
#     print("Invalid PIN. Please enter a 4-digit PIN consisting only of digits.")


########################## 22 - 05 - 2023 ##########################
# write a pythin code to calc the powers of 2 using the while loop

# power = int(input('enter the power : '))
# temp = 1
# while power > 0:
#     temp = temp *2
#     power -= -1
#
# print(temp)

# write a code to receive from the user number till the user insert
# negative value then print adios and close the appliction

# userInput = 0
# while userInput >= 0:
#     userInput = int(input('Enter a number'))
#     print(f'the number {userInput} is positive')
# print('adios')


#write a python code to receive 4 number from the user if the number where odd stop the loop

# for i in range(4):
#     userInput = int(input('enter a number '))
#     if userInput % 2 != 0:
#         break

#ask the user to insert the arrat length that he need create an empty list and fill it with the user input

# length = int(input("Enter the length of the array: "))
# array = []

# for i in range(length):
#     array.append(input(f"Enter element {i+1}: "))

# print("The array you entered is:", array)


#################################################### 23 - 05 - 2023 #################################################


# number_matrix = [
#     [12, 87, 5],
#     [-1, 3000, 4],
#     [200, 8, 3]]

# print(number_matrix[1][1])

# avg = []
# for list in number_matrix:
#     avg.append(sum(list) / len(list))

# print(avg)

################################################## 29 - 05 - 2023 ###############################################

# l1 = [5,-22,-9,0,55,-88.8,-15]
# new_list=[x for x in l1 if x < 0]
# print(new_list)



############################################### 30 - 05 - 2023 ##############################################
import requests

url = r'https://jsonplaceholder.typicode.com/users'
res = requests.get(url)
if 200 <= res.status_code <400:
    print (f' {res.status_code} this is the code ')
    users = res.json()
    for user in users:
        for k,v in user.items() :
            print(f' {k} -> {v}')
    print('-'*100)
else:
    print(f'naaaaaah {res .status_code}')

# print the body of all the comments with postId of 2 from this urd
# urt = https://isonplaceholder. typicode.com/comments

res = requests.get('https://jsonplaceholder.typicode.com/comments')
comments = res.json()
for comment in comments:
    if comment['postId'] in [2, 3, 5]:
# post id 2 or 3 or 5
        print[comment['body'] in 1]
        print('*' * 100)