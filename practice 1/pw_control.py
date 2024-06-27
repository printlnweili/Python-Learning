PW = "a559982"

for 次數 in range(5):
    pw = input("請輸入密碼: ")[:10]
    print(pw)
    11
    if  pw == PW:
        print("輸入正確 !")
        break

    elif pw != PW and 次數 < 4:
        print("密碼錯誤，請再輸入一次!")
        print(f"您的次數還剩下{4-次數}次")

    else:
        print("輸入次數達5次，密碼已鎖定")