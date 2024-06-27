"""
數字 = int(input("請輸入一個整數: "))
if 數字 <= 100:
    if 數字 % 2.0 == 0:
        print("偶數")
    else:
        print("奇數")
else:
    print("數字超過100!!")
"""
def 奇偶數判斷(數字):
    if 數字 <= 100:
        if 數字 % 2.0 == 0:
            return("偶數")
        else:
            return("奇數")
    else:
        return("數字超過100!!")
輸入 = int(input("請輸入一個整數: "))
結果 = 奇偶數判斷(輸入)
print(結果)