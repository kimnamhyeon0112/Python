# 핸드폰, 서울, 기타를 키 값으로 관리될 수 있도록 한다.

# 핸드폰 번호만 따로 저장
# 서울 전화번호만 따로 저장
# 기타 다른 지역 번호만 따로 저장
# 각각의 전화번호를 구분하여 저장하고 출력하는 프로그램을 작성하세요.

# 출력 형식
# <핸드폰> 목록
# 010-5464-5688
# 010-1199-5678
# 010-2388-1238
# 010-5678-6666
# 010-5678-6666

# <서울> 지역 목록
# 02-1029-1234
# 02-1029-1234
# 02-1029-1234
# 02-1029-1234
# 02-1029-1234

# <기타> 지역 목록
# 042-3456-1290
# 032-3456-1290
# 062-3456-1290
# 062-5555-3490
# 032-8796-1330

sample = ["010-5464-5688",
          "02-1029-1234",
          "042-3456-1290",
          "010-1199-5678",
          "02-1766-5678",
          "032-1456-6578",
          "010-2388-1238",
          "02-8769-1114",
          "062-3456-1290",
          "062-5555-3490",
          "010-5678-6666",
          "02-5432-1234",
          "032-9087-1780",
          "010-5986-6906",
          "02-1243-1876",
          "032-8796-1330"]

tmp = "010-5464-5688"
s1 = tmp.split('-')[0]
s2 = tmp[:tmp.find('-')]
s3 = tmp[:tmp.index('-')]
s4 = tmp.startswith("010")
s4 = tmp.startswith("02")
s5 = tmp[1] == '1'
s6 = tmp[1] == '2'

tmp_phone = []
tmp_seoul = []
tmp_other = []

# 방법 1
for num in sample:
    tmp = num[:num.find("-")]
    if tmp == "010":
        tmp_phone.append(num)
    elif tmp == "02":
        tmp_seoul.append(num)
    else:
        tmp_other.append(num)
print("<핸드폰> 목록", tmp_phone)
print("<서울> 지역 목록", tmp_seoul)
print("<기타> 지역 목록", tmp_other)
print("-"*150)
print()

# 방법 2
phone = []
phone.append(tmp_phone)
phone.append(tmp_seoul)
phone.append(tmp_other)

title = ["핸드폰", "서울", "기타"]
for i in range(len(phone)):
    print("<{}> 목록".format(title[i]))
    for num1 in tmp_phone:
        print(num1)
    print()
print("-"*150)
print()

# 방법 3
phone = {"핸드폰": [], "서울": [], "기타": []}
for num in sample:
    tmp = num[:num.find("-")]
    if tmp == "010":
        tmp_phone.append(num)
    elif tmp == "02":
        tmp_seoul.append(num)
    else:
        tmp_other.append(num)

    for k in phone:
        print("<{}> 목록".format(k))
        for num1 in phone[k]:
            print(num1)
        print()
print("-"*150)
print()

# 방법 4
# 전화번호 분리
def phoneDiv(s, phone):
    for num in s:
        tmp = num[:num.find("-")]
        if tmp == "010":
            phone[0].append(num)
        elif tmp == "02":
            phone[1].append(num)
        else:
            phone[2].append(num)


# 전화번호 출력
def phoneInfo(title, phone):
    for i in range(len(phone)):
        print("<{}> 목록".format(title[i]))
        for num1 in phone[i]:
            print(num1)
        print()

def testFunc(i, j):
    i, j = j, i


# main 함수 이용
def main():
    sample = ["010-5464-5688",
              "02-1029-1234",
              "042-3456-1290",
              "010-1199-5678",
              "02-1766-5678",
              "032-1456-6578",
              "010-2388-1238",
              "02-8769-1114",
              "062-3456-1290",
              "062-5555-3490",
              "010-5678-6666",
              "02-5432-1234",
              "032-9087-1780",
              "010-5986-6906",
              "02-1243-1876",
              "032-8796-1330"]
    title = ["핸드폰", "서울", "기타"]
    phone = [[], [], []]

    print("전", phone)
    phoneDiv(sample, phone)
    print("후", phone)
    phoneInfo(title, phone)

    a = 10
    b = 20
    print("함수 호출 전", a, b)
    testFunc(a, b)
    print("함수 호출 후", a, b)

main()

print("-"*150)
print()