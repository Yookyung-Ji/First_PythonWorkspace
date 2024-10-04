#20241003 

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



# 2-6 퀴즈 # 1

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




# 3-5. 퀴즈 # 2
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





#20241004


# 4-1. 문자열

sentence = '나는 소녀입니당' #sentence: 문자열
print(sentence)

sentence2 = "파이썬은 접근하기 쉽습니당"
print(sentence2) 

sentence3 = """
나는 소녀이고, 
파이썬은 접근하기 쉽습니당
"""
print(sentence3)



# 4-2. 슬라이싱

jumin = "241004-1234567" # 예제: 주민등록번호 (존재 X)

print("성별 : " + jumin[7])
#index는 항상 0부터 시작 - 2는 0번째!
print("연도 : " + jumin[0:2])
# :(콜론) - 0번째부터 2번째 직전까지 (0, 1의 값만 가져옴)
print("월 : " + jumin[2:4]) # 2 부터 4 직전까지 (2, 4) 
print("일 : " + jumin[4:6]) # 4 부터 6 직전까지 (4, 6)

print("생년월일 : " + jumin[:6]) # :6   # 처음부터 6 직전까지

#print("뒤 7자리 :" + Jumin[7:14]) 
print("뒤 7자리 :" + jumin[7:]) # 7:   # 7 부터 끝까지 #윗문장이랑 동일

print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) # 맨 뒤에 7번째부터 끝까지



# 4-3. 문자열 처리 함수

python = "Python is Amazing"

print(python.lower()) # lower: 모든 문자 다 소문자
print(python.upper()) # upper: 모든 문자 다 대문자

print(python[0].isupper())
# isupper: 파이썬의 첫 문자가 대문자인지 알려줌
# 맞으면 true, 틀리면 false
# 맞으니까 답은 true 나옴

print(len(python))
# len : 전체 문자열의 길이 

# "Python is Amazing"에서 Python 이라는 글자를 찾아서 바꾸고 싶을때
print(python.replace("Python", "Java"))
# replace : 값을 다른 값으로 쉽게 바꿔줌

index = python.index("n")
print(index)
# index: 어떤 문자가 어느 위치에 있는지 알 수 있음


# index를 찾는데 그 다음 위치부터 찾을 때
index = python.index("n", index + 1) 
# 앞에서 찾은 5라는 위치에서 + 1 => 6번째 위치부터 쭉 n을 찾음
print(index)

print(python.find("n"))
print(python.find("Java"))
# find: 원하는 문자 찾기 
# find에서는 내가 원하는 값이 없을 때 -1 반환 / 프로그램은 계속 진행됨

'''
# print(python.index("Java")) 
# Print("hi")

# index에서는 오류 - 파이썬이라는 변수에 자바가 없음
# index에서는 뒤에 문장이 있어도 뒷문장이 출력이 안됨
'''

print(python.count("n"))
# count : 총 몇번 등장하는지 세어줌 



# 4-4. 문자열 포맷


print("a" + "b")
# + : 합쳐줌

print("a", "b")
# ,(콤마): 띄어쓰기 해줌 

# 방법 1: % 이용하기

print("나는 %d살입니당." % 21) # d는 정수
print("나는 %s을 좋아해용." % "파이썬") # s: string - 문자열
print("Apple 은 %c로 시작해요." % "A") # c: 캐릭터 - 한글자만 출력

# %s 정수, 하나의 문자 상관없이 각 출력을 잘 할 수 있음
print("나는 %s살입니당." % 21)

# 값을 2개를 넣고 싶을 때 / 괄호로 감싸기
print("나는 %s색과 %s색을 좋아해용" % ("연분홍", "연보라"))



# 방법 2: {}, fomat 이용하기
print("나는 {}살입니당.".format(21))

# 값을 2개를 넣고 싶을 때 / 괄호로 감싸기
print("나는 {}색과 {}색을 좋아해용".format("연분홍", "연보라"))

#중괄호: 연속적 / # 중괄호 안의 숫자: 순번에 맞게 나옴
print("나는 {0}색과 {1}색을 좋아해용".format("연분홍", "연보라"))
print("나는 {1}색과 {0}색을 좋아해용".format("연분홍", "연보라"))


# 방법 3: 설정한 변수를 중괄호 안에 넣기 
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 21, color = "연보라"))

print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "연보라", age = 21)) # 순서 바꾸기


# 방법 4: 직접 변수 선언 하고, print에서 f로 시작 
# f 다음 ""문장의  중괄호 값은 실제 변수에 저장된 값을 그대로 쓸 수 있음 

age = 21
color = "연분홍"
print(f"나는 {age}살이며, {color}색을 좋아해용.")


# 4-5. 탈출 문자 

print("백문이 불여일견 백견이 불여일타")

# 백번 보는 것보다 한번 보는게 낫고, 
# 백번 보는 것보다 한번 직접 처보는게 낫다.


# \n (역슬러쉬 n) : 줄바꿈
print("백문이 불여일견\n백견이 불여일타")

# 저는 "지유경"입니당.
# print("저는 "지유경"입니당.") 이러면 오류!

print("저는 '지유경'입니당.")
print('저는 "지유경"입니당.')

# 이렇게 해도 괜찮지만 탈출문자 \ (역슬러쉬)를 앞에 넣어주자!

# \" \' : 문장 내에서 따옴표
print("저는 \"지유경\"입니당.")
print("저는 \'지유경\'입니당.")

# \\ : 문장 내에서 하나의 \로 바뀜
# print("C:\Users\user>") : 오류
print("C:\\Users\\user>")

# \r : 커서를 맨 앞으로 이동
# 커서: 깜빡깜빡이는거, 내 위치
print("Red Apple\rPine")

# \b : 벡스페이스 (한 글자 삭제)
print("Redd\bApple")

# \t : 탭
print("Red\tApple")


# 4-6. 퀴즈 # 3

'''
Q. 사이트 별로 비밀번호를 만들어 주는 프로그램을 작성하시오

예) http://naver.com
규칙1 : http:// 부분은 제외 => naver.com
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성

ex) (nav) (5) (1) (!)
예) 생성된 비밀번호 : nav51!
'''
#나의 답변
'''
naver = "naver.com"
Print(naver)
Print((naver[0, 2])+(naver.len("naver"))+(naver.count("e"))+"!")

모르겠당 난 할 수 있는 최선을 다했당....
'''

# 정답

url = "http://naver.com"
my_str = url.replace("http://", "") # 규칙 1
# print(my_str)
my_str = my_str[:my_str.index(".")] # 규칙 2
# my_str[0:5] -> 0 ~ 5 직전까지. (0, 1, 2, 3, 4)
#print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1} 입니다.".format(url, password))

# 다음, 구글, 유튜브 링크를 했을때도 다 다른 비밀번호가 나옴!



# 5-1. 리스트

# 파이썬 코딩 무료 강의 (기본편) - 6시간 뒤면 여러분도 개발자가 될 수 있어요 [나도코딩]
# 내일 해야징~ 