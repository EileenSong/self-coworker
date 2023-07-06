

import random

print("로또번호 다섯 개 추첨하기")

for i in range(5):
    lotto = random.sample (range(1,46), 6)
    print(lotto)
