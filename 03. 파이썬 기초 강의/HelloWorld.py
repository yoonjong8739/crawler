print("Hello World")

#%%
a = 5
b = 10
print(a + b)

# %%
# 문자열
string = "Python is one of the programming languages"

print(string.count("o"))  # 'o'의 개수 세기
print(string.count("o", 10)) # 'o'의 개수 세기 (10번째 인덱스 이후)
print(string.find("o")) # 'o'의 첫 번째 인덱스 찾기
print(string.find("x")) # 'x'의 첫 번째 인덱스 찾기 (없으면 -1 반환)

# %%
# 대문자와 소문자 구분
string = "aBc"
print(string.upper())  # 대문자로 변환
print(string.lower())  # 소문자로 변환

# %%
# 분할
string = "one, two, three"
print(string.split(","))  # 쉼표로 분할

# %%
# 결합
a = "Hello"
b = "World"
print(a + b)

array = ["one", "two", "three"]
print(" ".join(array))  # 공백으로 결합

# %%
# 리스트
array = ["one", "two", "three"]
print(array[1])  # 두 번째 요소

array = [0] * 10
print(array)

array = ["one", 2, "three"]
print(len(array))

array = ["one", 2, "three"]
array.append(4)
print(array)

array = ["one", 2, "three"]
array.insert(1, 1.5)
print(array)

# %%
# 튜플
num = (5, 10, 15)
#num[0] = 3 # 튜플은 불변이므로 수정할 수 없음

# %%
# 함수
def plus1(a, b = 0):
    result = a + b
    print(result)
    return result

result = plus1(2, 3)
print(result)

def plus2(a: int, b: int) -> int:
    result = a + b
    print(result)
    return result
result = plus2(2, 3)
print(result)

# %%
# 클래스
class Shop:
    name = ""
    businessHours = ""
    def __init__(self, name, businessHours):
        self.name = name
        self.businessHours = businessHours
    def details(self):
        print(f"가게 이름:{self.name}, 영업 시간:{self.businessHours}")

shop = Shop("구름 국수", "9:00-19:00")
shop.details()

# 클래스 상속
#class Bookstore(Shop)

# %%
