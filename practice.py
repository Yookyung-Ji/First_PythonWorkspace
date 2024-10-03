# 2-1. 숫자 자료형
# 파이썬을 실행할 때는 무조건 저장하고 실행하기! ctrl + s: 저장

print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))


# 2-2. 문자열 자료형

print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*9)


#2-3. boolean 자료형
# 참 / 거짓

print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5 > 10))


#2-4. 변수

#애완동물을 소개해 주세요~

animal = "강아지"
name = "코코"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 "+ animal + "의 이름은 "+ name +"입니당")
hobby = "공놀이 하는 것"
# print(name +"는 "+ str(age) +"살이며, " + hobby + "을 엄청 좋아해용")
print(name ,"는 ", age ,"살이며, " , hobby , "을 엄청 좋아해용")
print(name +"는 어른일까용? " + str(is_adult))


# 주석
# 코드 안에 포함은 되지만, 실제로 실행이 안되는 문장 (무시되는 문장)

#개발자와의 소통, 복잡한 프로그램 만들 시 적용한다.

# 한 문장 주석처리
'''이렇게 하면 
여러문장 주석처리 가능
작은 따옴표 3개 앞뒤로 둘러싸기'''

#주석 편하게 하고 싶으면 ctrl+ /  (쉬프트 옆에 있는 기호)



# 2-6 퀴즈

# 변수를 이용하여 다음 문장 출력
# 변수명: station
# 변수값: "사당", "신도림", "인천공항" 순서대로 입력
# 출력 문장: xx 행 열차가 들어오고 있습니당.

#나의 답변 ㅇㅋ

station = "사당"
print(station + "행 열차가 들어오고 있습니당.")

station = "신도림"
print(station + "행 열차가 들어오고 있습니당.")

station = "인천공항"
print(station + "행 열차가 들어오고 있습니당.")


# 3-1. 연산자

print(1+1) #2
print(3-2) #1
print(5*2) #10
print(6/3) #2

print(2**3) #2^3 (2의 3제곱): 8 
print(5%3) # 5를 3으로 나눴을 때 나머지 구하기: 2
print(10%3) # 1
print(5//3) # 5를 3으로 나눴을 때 몫 구하기: 1
print(10//3) # 3

print(10 > 3) # True 10은 3보다 크다
print(4 >= 7) # False 4는 7보다 크거나 같다
print(5 <= 5) # True 5는 보다 작거나 같다

print(3 == 3) # True # 3은 3과 똑같다 (등호 두개로 앞과 뒤가 똑같음)
print( 4 == 2 ) # False
print(3 + 4) == 7 # True

print(1 != 3) # True  #  !=  앞뒤가 같지 않다!
print(not(1 != 3)) #false    #not은 앞의 값과 반대

print((3 > 0) and (3 < 5)) # True # 3은 0보다 크고 3은 5보다 작기 때문에
print((3 > 0) & (3 < 5)) # True  # &: and

print((3 > 0) or (3 < 5)) # True  # or: 둘 중에 하나라도 true면 true
print((3 > 0) | (3 < 5)) # True  # or: | (Backspace 바로 왼쪽 위)
                        #3이 0보다 크거나, 3이 5보다 작으면 True
print(5 > 4 > 3) # True
print(5 > 4 > 7) # False


# 3-2. 간단한 수식

print(2 + 3 * 4) # 14
print((2 + 3) * 4) #20

number = 2 + 3 * 4 # 14
print(number)

number = number + 2 # 16 # number가 14니까 14 => 14 + 2 = 16
print(number)

number += 2 # 18 
# number = number + 2와 완전 똑같은 문장, 그냥 줄여서 쓴거임
print(number)

number *= 2 # 36 
# number = number * 2와 완전 똑같은 문장, 그냥 줄여서 쓴거임
# 18 * 2 = 36
print(number)

number /= 2 # 18
print(number)

number -= 2 # 16
print(number)

number %= 5 # 1    # 16을 5로 나누면 1
print(number)


# 3-3. 숫자 처리 함수

print(abs(-5)) # 5     # abs: 절댓값
print(pow(4, 2)) # 16 # pow(4, 2) -> 4^2 -> 4의 2 제곱 = 4*4 = 16
                      # pow: 제곱

print(max(5, 12)) # 12   # max: 최댓값 5랑 12중 더 큰 거 
print(min(5, 12)) # 5   # min: 최솟값 5랑 12중 더 작은 거 

print(round(3.14)) # 3 # round: 반올림
print(round(4.99)) # 5

from math import *
print(floor(7.99)) # 7  # floor: 내림
print(ceil(3.14)) # 4   # ceil : 올림 (천장을 생각하자~)
print(sqrt(25)) # 5     # sqrt : 제곱근(루트)


# 3-4. 랜덤 함수

from random import * 

#주석 편하게 하고 싶으면 ctrl+ / (쉬프트 옆에 있는 기호)

print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성

print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성 # int: 정수
print(int(random() * 10) + 1 ) # 1 ~ 10 이하의 임의의 값 생성 

print(int(random() * 45) + 1 ) # 1 ~ 45 이하의 임의의 값 생성
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성 (윗문장이랑 똑같음)

print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성 
# 1도 포함, 45도 포함 # randint: 다 포함




# 3-5. 퀴즈
''' 
Quiz) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니당
월 4회 스터디를 하는데, 3번은 온라인으로 하고, 
1번은 오프라인으로 하기로 했습니당. 
아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하세용~

조건 1 : 랜덤으로 날짜를 뽑아야 함
조건 2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
조건 3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외 

< 출력문 예제 >
오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다. '''


# 나의 답변

# print("오프라인 스터디 모임 날짜는 매월 "randint(4, 28) "일로 선정되었습니다.")

# 정답

from random import *
date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + "일로 선정되었습니다.")


# 4-1. 문자열
# 파이썬 코딩 무료 강의 (기본편) - 6시간 뒤면 여러분도 개발자가 될 수 있어요 [나도코딩]
# 내일 해야징~ 