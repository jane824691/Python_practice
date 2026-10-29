# print("Hello, World!")
# print(2 + 3)
# name =input("Enter your name: ")
# age = input("what's your age: ")
# print("Hello, " + name + "!" + " You are " + age + " years old.")


# tuple 元組
# 元組代表絕對不能改動, 鎖死
# scores = (90, 80, 70, 60)

# list 列表
# 可改動
scores = [90, 80, 70, 60]
students = ["John", "Mary", "Tom", "Jane"]
# print(scores[-2]) # 取倒數第二個元素
# print(scores[1:3]) # 取第二個到第三個元素
# print(scores[:3]) # 取到第三個元素
# scores.extend(students) # 將students列表加入scores列表
# print(scores)

# result = scores.extend(students)

# print("extend 的回傳值：", result) # None
# print("修改後的 scores：", scores) # 修改後的 scores： [90, 80, 70, 60, 'John', 'Mary', 'Tom', 'Jane']

# 各種方法　　是否修改原本的 List？	    回傳值
# extend()	        是	               None
# append()	        是	               None
# sort()	        是	               None
# reverse()	        是	               None
# pop()	            是	               被移除的元素
# copy()	        否（建立淺拷貝）　  新的 List

# 關於 copy() 方法的說明：
# copy() 方法會建立一個新的 List，並將原本的 List 的元素複製到新的 List 中。
# scores = [90, 80, 70]

# new_scores = scores.copy()
# new_scores.append(100)

# print(scores) # [90, 80, 70]
# print(new_scores) # [90, 80, 70, 100]

# 如沒有 copy(), 直接新舊變數相等, 原值會直接被蓋掉修改
# new_scores = scores
# new_scores.append(100)

# print(scores) # [90, 80, 70, 100] # append() 方法會修改原本的 List，因此 scores 也會被修改。
# print(new_scores) # [90, 80, 70, 100]

# 如果需求是把巢狀資料整份獨立複製，就可以使用 deepcopy()：
# import copy

# a = [[[[10, 20]]]]

# b = copy.deepcopy(a)

# b[0][0][0].append(99)

# print(a)  # [[[[10, 20]]]]
# print(b)  # [[[[10, 20, 99]]]]



# 函式組合+ 轉化數字變字串寫法:
# def greet_user(name, age):
#     print("Hello, " + name + "!" + " You are " + str(age) + " years old.")

# greet_user("Janet", 25)


# 函式相加寫法:
# def add(number1, number2):
#     return number1 + number2

# def minus(number1, number2):
#     return number1 - number2

# result = add(5, 10) + minus(20, 5)
# print(result)

# num1 = float(input('Enter first number: '))
# marks = input('Enter your marks: ')
# num2 = float(input('Enter second number: '))


# if/ else 寫法:
# if marks == '+':
#     print(num1 + num2)
# elif marks == '-':
#     print(num1 - num2)
# elif marks == '*':
#     print(num1 * num2)  
# elif marks == '/':
#     print(num1 / num2)
# else:
#     print("無此結果")


# python 的「且」是寫 and, 「或」是寫 or, 「沒有」是寫 not, 或沒有就 or not
# 如果 你考100分 且 今天下雨
#     我給你1000元
# 否則
#    你給我50元

# score = 100
# rainy = True

# if score == 100 and rainy:
#     print("我給你1000元")
# else:
#     print("你給我50元")

# def max_number(num1, num2, num3):
#     if num1 > num2 and num1 > num3:
#         return num1
#     elif num2 > num1 and num2 > num3:
#         return num2
#     else:
#         return num3

# max_num = max_number(10, 20, 30)
# print("最大值是:", max_num)


# while 迴圈
# i = 1
# while i <= 5:
#     print('i = ' + str(i))
#     i += 1

# print('迴圈結束')


# 猜數字遊戲
# secret_number = 77
# guess = None
# guess_chances = 3

# while guess != secret_number and guess_chances > 0: # 每輪都執行的放 while 裡
#     guess = int(input('請猜一個數字: '))
#     guess_chances -= 1

#     if guess < secret_number:
#         print('太小了!')
#     elif guess > secret_number:
#         print('太大了!')
#     else:
#         print('恭喜你猜對了!')

# if guess_chances == 0 and guess != secret_number: # 只需執行一次可分開放, 更好管理
#     print('遊戲結束! 你沒有猜中數字。')



# for 迴圈
# for 變數 in 字串or列表:

# for letter in "Hello":
#     print(letter)

#H
#e
#l
#l
#o

# for number in range(100): # 從 0 到 99
#     print(number)

# +1 +2 +3 +4 +5 = 15
# def calculate_sum(n):
#     total = 0
#     for i in range(1, n + 1):
#         total += i
#     return total
# calculate_sum(5)
# print(calculate_sum(5)) # 15

# 幾次方（寫法1）
# def power(base, exponent):
#     result = base

#     for _ in range(1, exponent):
#         result *= base
#     return result

# power_result = power(2, 3)
# print("2 的 3 次方是:", power_result) # 8

# # 幾次方（寫法2）
# def power_v2(base, exponent):
#     return base ** exponent

# power_result_v2 = power_v2(2, 4)
# print("2 的 4 次方是:", power_result_v2) # 16

# # 幾次方（寫法3）
# def power_v3(base, exponent):
#     result = base
#     for index in range (exponent - 1): # range(4) = 0, 1, 2, 3
#         result = result * base
#         # result = 3 * 3 = 9   # index = 0
#         # result = 9 * 3 = 27   # index = 1
#         # result = 27 * 3 = 81  # index = 2
#         # result = 81 * 3 = 243  # index = 3, 但不會再執行了, 因為 range(4) 只會跑到 3
#     return result
# print("3 的 5 次方是:", power_v3(3, 5)) # 243

# python 的符號寫法
# 簡寫	等同寫法	意義
# x += 2	x = x + 2	加上 2
# x -= 2	x = x - 2	減去 2
# x *= 2	x = x * 2	乘以 2
# x /= 2	x = x / 2	除以 2
# x //= 2	x = x // 2	整數除法後指定
# x %= 2	x = x % 2	取餘數後指定
# x **= 2	x = x ** 2	取平方後指定