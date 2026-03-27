# def 더하기(x, y):
#     answer = 0
#     return x + y

# a = 10
# b = 5
# c = 더하기(a, b)
# print(c)


# def 에이():
#     print("짝수")
# for i in range(1,21):
#     if i %2 == 0:
#         에이()
#     else:
#         print(i)

# a = 'python'

# for i in range(len(a)):
#     print(a[0:i+1])

# a = 43

# b = a % 10
# if b == 3 b == 

# for i in range(1,3+1):
#     for j in range(1,5+1):
#         print('*',end= '')
#     print()

# for i in range(1,5+1):
#     for j in range(1,5+1):
#         print('#', end='')
#     print()

# for i in range(1,4+1):
#     print("*"*i)

# for i in range(4,0,-1):
#     for j in range(i):
#         print("*", end= '')
#     print()

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end= "")
#     print()

# for i in range(1,4):
#     for j in range(1,4):
#         print(i,end="")
#     print()

# for i in range(2,3):
#     for j in range(1,10):
#         print(f"{i} * {j} = {i * j}")

# for i in range(1,4):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()
# for k in range(2,0,-1):
#     for l in range(k,0,-1):
#         print("*",end="")
#     print()

# answer = 0

# arr =  [[1,2,3],
#         [4,5,6],
#         [7,8,9]]
# # for i in range(3):
# #         answer += arr[i][0]
# # print(answer)
# for i in range(3):
#     answer += arr[i][2-i]
# print(answer)

# import random
# a = random.randint(1,100)
# for i in range(1,21):
#     c = int(input("수를 입력하시오"))
#     if c == a:
#         print("정답입니다")
#     elif c < a:
#         print("up")
#     elif c > a:
#         print("down")
# print("retire")

# a = int(input("press number"))
# if a %2 == 0:
#     print("짝수")
# elif a %2 == 1:
#     print("홀수입니다")
# else:
#     print("0입니다")

# a = int(input("press number"))
# if a >= 10 and a < 20:
#     print("10대")
# elif a >= 20 and a < 30:
#     print("20대")
# elif a >= 30 and a < 40:
#     print("30대")
# else:
#     print("연령대를 인식 못했습니다")


# a = int(input("press number"))
# if a %3 == 0 and a %5 == 0:
#     print("삼오")
# elif a %5 == 0:
#     print("오")
# elif a %3 == 0:
#     print("삼")

# a = input("press word")
# if len(a) >= 5:
#     print("true")
# else:
#     print("false")

# answer = []
# for i in range(1,21):
#     if i %2 == 0:
#         answer.append(i)
# print(answer)

# a = int(input())
# for i in range(1,10):
#     print(f'{a} x {i} = {a * i}')

# import random
# a = random.randint(1,50)
# b = 0
# while b != a:
#     b = int(input())
#     if b == a:
#         print("answer")
#     elif b < a:
#         print("up")
#     elif b > a:
#         print("down")

# a = []
# for i in range(1,51):
#     if i %7 == 0:
#         a.append(i)
# print(a)

# a = 'kira'
# print(a[::-1])

# list = [10,59,29,34,72,19]
# print(max(list))

# a = "다가져가다"
# if a[::-1] == a:
#     print("True")
# else:
#     print("false")

# l = []
# a = int(input())
# l.append(a)
# b = int(input())
# l.append(b)
# c = int(input())
# l.append(c)
# l.sort()
# print(l[1])

# a = int(input())
# if a >= 10000 and a < 50000:
#     print(int(a - (a * (5 / 100))))
# elif a >= 50000 and a < 100000:
#     print(int(a - (a * (10 / 100))))
# elif a >= 100000:
#     print(int(a - (a * (20 / 100))))

# a = 123
# b = 0
# for i in str(a):
#     b += int(i)
# print(b)

# answer = 0
# scores = [
#     [80, 90, 85],
#     [70, 60, 75],
#     [100, 95, 90]
# ]
# for i in range(3):
#     for j in range(3):
# #         answer += scores[i][j]
# # print(answer // 9)
#         if scores[i][j] > answer:
#             answer = scores[i][j]
# print(answer)

# m = [
#     [50, 60, 70],
#     [80, 90, 100],
#     [40, 30, 20]
# ]
# for i in range(3):
#     print(sum(m[i]) // 3)

# k = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# for i in range(2):
#     for j in range(3):
#         if k[i][j] %2 == 0:
#             print(k[i][j])

# for i in range(3):
#     for j in range(3):
#         print('*', end = '')
#     print()

# answer = 0
# board = [
#     [1, 0, 1],
#     [0, 1, 1]
# ]
# for i in range(2):
#     for j in range(3):
#         if board[i][j] == 1:
#             answer += 1
# print(answer)

# numbers = [
# [1, 2],
# [3, 4],
# [5, 6]
# ]
# a = 7
# if a in numbers:
#     print(1)
# else:
#     print(0)

# numbers = [
#     [1, 2],
#     [3, 4]
# ]
# for i in range(2):
#     for j in range(2):
#         print(numbers[i][j] * 2)

# numbers = [
#     [2, 7, 3],
#     [8, 1, 6]
# ]
# for i in range(2):
#     for j in range(3):
#         if numbers[i][j] >= 5:
#             print(numbers[i][j])

# answer = 0
# board = [
#     [0, 1, 0],
#     [1, 0, 1]
# ]
# for i in range(2):
#     for j in range(3):
#         if board[i][j] == 0:
#             answer += 1
# print(answer)

# for i in range(5):
#     for j in range(i):
#         print("*",end = '')
#     print()

# answer = 0
# numbers = [
#     [3, 5, 9],
#     [12, 7, 4]
# ]
# for i in range(2):
#     for j in range(3):
#         if numbers[i][j] %3 == 0:
#             answer += 1
# print(answer)

# numbers = [
#     [5, 6],
#     [7, 8]
# ]
# for i in range(2):
#     for j in range(2):
#         print(numbers[i][j] + 1)

# numbers = [
#     [1, 4, 7],
#     [2, 9, 6]
# ]
# for i in range(2):
#     for j in range(3):
#         if numbers[i][j] %2 == 1:
#             print(numbers[i][j])

# a = 0
# numbers = [
#     [2, 4],
#     [6, 8]
# ]
# for i in range(2):
#     for j in range(2):
#         a += numbers[i][j]
#     if a %2 == 0:
#         print("짝수")
#     else:
#         print("홀수")

# board = [
#     [0, 1, 0],
#     [1, 0, 0]
# ]
# for i in range(2):
#     for j in range(3):
#         if board[i][j] == 1:
#             print(i,j)

# a = 100
# numbers = [
#     [1, 3, 7],
#     [4, 8, 2]
# ]
# for i in range(2):
#     for j in range(3):
#         if a > numbers[i][j]:
#             a = numbers[i][j]
# print(a)

# numbers = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# for i in range(1,-1,-1):
#     for j in range(2,-1,-1):
#         print(numbers[i][j])

# a = 0
# numbers = [
#     [5, 12, 8],
#     [15, 3, 20]
# ]
# for i in range(2):
#     for j in range(3):
#         if numbers[i][j] > 10:
#             a += numbers[i][j]
# print(a)

# a = 0
# numbers = [
#     [10, 20, 30],
#     [5, 7, 8],
#     [25, 15, 5]
# ]
# for i in range(3):
#     if sum(numbers[i]) >= 40:
#         a += 1
# print(a)

# a = int(input())
# for i in range(a):
#     for j in range(a):
#         print('*',end = '')
#     print()

# a = int(input("가로"))
# b = int(input("세로"))
# for i in range(b):
#     for j in range(a):
#         print('*',end = '')
#     print()

# a = int(input())
# for i in range(a,0,-1):
#     for j in range(i):
#         print("*",end = '')
#     print()

# a = int(input())
# for i in range(1,a + 1):
#     for j in range(1,a + 1):
#         print(i,end = "")
#     print()


# a = int(input())
# for i in range(1,a + 1):
#     for j in range(1,a + 1):
#         print(j,end = "")
#     print()


# a = int(input())
# for i in range(1,a + 1):
#     for j in range(1,a + 1):
#         if i == j:
#             print(1,end = '')
#         else:
#             print(0,end = "")
#     print()


# a = int(input())
# for i in range(1,a + 1):
#     for j in range(1,i + 1):
#         print(j,end = "")
#     print()

# answer = 2
# a = int(input())
# for i in range(a):
#     for j in range(a):
#         print(answer,end = ' ')
#         answer += 2
#     print()


# a = int(input())
# for i in range(1,a+1):
#     for j in range(1,a+1):
#         if (i + j) %2 == 0:
#             print(0,end = '')
#         else:
#             print(1,end = '')
#     print()


# a = int(input())
# for i in range(a):
#     for j in range(a):
#         if i == 0 or j == 0 or i == a-1 or j == a-1:
#             print(1,end = "")
#         else:
#             print(0, end = '')
#     print()

# answer = 0
# a = int(input())
# b = 0
# for i in range(1,a + 1):
#     for j in range(1,a + 1):
#         b += 1
#         answer += b
# print(answer)

# answer = 0
# n = int(input())
# m = 1
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if m %2 == 0:
#             answer += 1
#         m += 1
# print(answer)


# answer = 0
# n = int(input())
# m = 1
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if m %3 == 0:
#             print(m, end = ' ')
#         else:
#             print('', end = ' ')
#         m += 1
#     print()


# answer = 0
# n = int(input())
# m = 1
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if m %5 == 0:
#             answer += 1
#         m += 1
# print(answer)


# answer = 0
# n = int(input())
# m = 1
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if m > 7:
#             answer += 1
#         m += 1
# print(answer)

# n = int(input())
# m = 9
# for i in range(n,0,-1):
#     for j in range(n,0,-1):
#         print(m,end = '')
#         m -= 1
# #     print()


# n = int(input())
# m = 1
# for i in range(n):
#     for j in range(n):
#         if i == 1 and j == 1:
#             print(0,end = '')
#         else:
#             print(m,end = '')
#         m += 1
#     print()


# n = int(input())
# m = 1
# for i in range(n):
#     for j in range(n):
#         if m %2 == 0:
#             print('*',end = '')
#         else:
#             print(m,end = '')
#         m += 1
#     print()

# def add(a,b):
#     answer = a + b
#     return answer

# a = int(input())
# b = int(input())
# print(add(a,b))


# def add(a,b,c):
#     answer = max(a,b,c)
#     return answer

# a = int(input())
# b = int(input())
# c = int(input())
# print(add(a,b,c))


# def add(a):
#     answer = 0
#     if a %2 == 0:
#         return "Yes"
#     else:
#         return "no"
#     return answer

# a = int(input())
# print(add(a))


# def add(a):
#     answer = a ** 2
#     return answer

# a = int(input())
# print(add(a))


# def add(a):
#     answer = 0
#     for i in range(a,0,-1):
#         print(i)

# a = int(input())
# add(a)


# def add(a):
#     answer = 0
#     for i in range(1,a + 1):
#         answer += i
#     return answer

# a = int(input())
# print(add(a))


# def add(a,b):
#     answer = 0
#     for i in range(a,b+1):
#         answer += i
#     return answer

# a = int(input())
# b = int(input())
# print(add(a,b))


# def add(a):
#     answer = 0
#     for i in range(a,a+1):
#         for j in range(1,10):
#             print(f'{i} x {j} = {i * j}')
#         print()

# a = int(input())
# add(a)


# def add(a):
#     answer = 0
#     return str(a)[::-1]

# a = int(input())
# print(add(a))


# def add(a):
#     answer = 0
#     for i in str(a):
#         answer += int(i)
#     return answer

# a = int(input())
# print(add(a))


# def add(a):
#     answer = 0
#     for i in range(1,a+1):
#         if a %i == 0:
#             print(i)

# a = int(input())
# add(a)


# def add(a):
#     answer = 0
#     for i in range(a):
#         for j in range(a):
#             print('*',end = '')
#         print()

# a = int(input())
# add(a)


# def add(a,b,c):
#     answer = (a + b + c) // 3
#     return answer

# a = int(input())
# b = int(input())
# c = int(input())
# print(add(a,b,c))


# def add(a,b):
#     answer = 0
#     for i in range(a,b+1):
#         if i %a == 0:
#             answer += 1
#     return answer

# a = int(input())
# b = int(input())
# print(add(a,b))


# def add(a):
#     answer = 0
#     for i in str(a):
#         answer = i
#         if i > answer:
#             answer = i
#     return answer

# a = int(input())
# print(add(a))


# def add(a,b):
#     answer = 0
#     for i in range(a, b + 1):
#         if i %2 == 0:
#             answer += i
#     return answer

# a = int(input())
# b = int(input())
# print(add(a,b))


# def add(a,b):
#     answer = 0
#     if str(b) in str(a):
#         return "YES"
#     return "NO"

# a = int(input())
# b = int(input())
# print(add(a,b))


# def add(a):
#     answer = 0
#     for i in range(1,a+1):
#         for j in range(1,i+1):
#             print("*",end = "")
#         print()

# a = int(input())
# add(a)


# def add(a):
#     answer = 0
#     for i in a:
#         answer += 1
#     return answer

# a = input()
# print(add(a))

# for i in range(5):
#     for j in range(5):
#         print('*',end = "")
#     print()


# for i in range(1,5 + 1):
#     for j in range(1,i + 1):
#         print('*',end = '')
#     print()


# for i in range(5):
#     for j in range(5):
#         print('*',end = "")
#     print()

# for i in range(2, 10):
#     for j in range(1, 10):
#         print(f'{i} x {j} = {i * j}')
#     print()

# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print('*',end = "")
#     print()

# for i in range(1,5+1):
#     for j in range(1,5+1):
#         print(i,end = "")
#     print()

# m = 0
# for i in range(1,5+1):
#     for j in range(1,5+1):
#         m += 1
#         print(m,end=" ")
#     print()

# for i in range(0,2+1):
#     for j in range(0,2+1):
#         print(i,j)
#     print()

# for i in range(1,7+1,2):
#     for j in range(1,i+1):
#         print('*',end = "")
#     print()

# l = 0
# a = [[1, 2], 
#      [3, 4], 
#      [5, 6]]
# for i in range(3):
#     for j in range(2):
#         l += a[i][j]
# print(l)

# for i in range(2,10):
#     for j in range(1,10):
#         if i %3 == 0:
#             print(f'{i} x {j} = {i * j}')

# for i in range(1,3 + 1):
#     for j in range(1,i + 1):
#         print(j,end = "")
#     print()

# def add(a):
#     print(f"안녕하세요 {a}님")

# a = (input("이름을 입력하시오"))
# add(a)

# def add(a,b):
#     answer = a + b
#     return answer
# a = int(input())
# b = int(input())
# print(add(a,b))


# def add(a):
#     answer = a ** 2 * 3.14
#     return answer
# a = int(input())
# print(add(a))


# def add(a,b,c):
#     answer = a
#     if a < b:
#         answer = b
#         if b < c:
#             answer = c
#     return answer
# a = int(input())
# b = int(input())
# c = int(input())
# print(add(a,b,c))


# def add(a,b,c):
#     answer = (a + b + c) // 3
#     return answer
# a = int(input())
# b = int(input())
# c = int(input())
# print(add(a,b,c))


# def add(a):
#     answer = 0
#     if len(a) >= 8:
#         return True
#     return False
# a = input()
# print(add(a))


# def add(a):
#     return a[::-1]
# a = input()
# print(add(a))


# def add(a):
#     answer = 0
#     for i in range(1,a+1):
#         if a %i == 0:
#             answer += 1
#     if answer == 2:
#         print(True)
#     else:
#         print(False)
# a = int(input())
# add(a)

# a = 0
# list = []
# while a != 3:
#     a = int(input("번호 입력 ㄱㄱ"))
#     if a == 1:
#         b = input("할일 입력 ㄱㄱ")
#         list.append(b)
#     elif a == 2:
#         print(list)
#     elif a == 3:
#         break

# class 식세븐:
#     def __init__(self,x,y,z):
#         self.국어 = x
#         self.수학 = y
#         self.영어 = z

#     def 평균(self):
#         return (self.국어 + self.수학 + self.영어) // 3
    
# 평균구하기 = 식세븐(100,98,15)
# print(평균구하기.평균())

# a = input("단어를 입력하시오")
# deathnote = {"apple":"사과","boxer":"복서","banana milk":"바나나 우유"}
# if a in deathnote:
#     print(deathnote[a])
# else:
#     print("자세한건 나무위키에서")

# import requests

# 응답 = requests.get("https://dog.ceo/api/breeds/image/random")
# if 응답.status_code == 200:
#     print(응답.json())

