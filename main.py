


print("hello")

import random

print("로또번호 다섯 개 추첨하기")

for i in range(5):
    lotto = random.sample (range(1,46), 6)
    print(lotto)


y = input("다시 추첨하기를 원하면 y를 누르셍")

if y == "y":
    lotto = random.sample(range(1,46), 6)
    print(lotto)
