from random import randint

# random_number = randint(1,10)
# trials = 0
# gameIsContinue =  True
# while(gameIsContinue):
#     if trials == 3:
#         print("You reach the max trial limit you loose")
#         break
#     guess_number = int(input("guess a number between 1 to 10 : "))
#     if guess_number == random_number:
#         gameIsContinue = False
#         print("you win")
#     else :
#         if guess_number < random_number:
#             print("too low try again")
#         else:
#             print("too high try again")
#     trials += 1

# def greatest(num1,num2):
#     return num1 if num1>num2 else num2
# # number_1,number_2 = input("entere a number").split(",")
# # print(ifEven(int(number_1),int(number_2)))    

# def greater(a,b,c):
#     return greatest(greatest(a,b),c)  
# print(greater(1,3,7))

# def Ispalindrome(name):
#     return name[::-1] == name
# print(Ispalindrome("madan"))   

# numbers = list(range(1,20))

# max_num = numbers[0]
# min_num = numbers[0]

# def maximum(l):
#     max_num = l[0]
#     for i in range(len(l)):
#         if max_num < l[i]:
#             max_num = l[i]
#     return max_num

# print(maximum(numbers))

# def findingleapYear(y):
#     if y %400 == 0:
#         return True 
#     return True if y % 4 == 0 and y %100 != 0  else False

# for i in range(1900,2110,1):
#     print(f"year : {i} is leap year {findingleapYear(i)}")

n = 24
if n%2== 0 and (n < 6 or n > 20):
    print("Not Weird")
else:
    print("Weird")
   
