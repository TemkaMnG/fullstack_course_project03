import random
your_name = input("Та нэрээ оруулна уу? ")
print("Тоо таах тоглоомонд тавтай морилно уу")
print("Тоглоомын түвшинг сонгоно уу:")
print("1. Амархан (1-50 хооронд тоо)")
print("2. Дунд (1-100 хооронд тоо)")
print("3. Хэцүү (1-150 хооронд тоо)")
print("4. Тусламж")
print("3. Гарах")
level = input("1, 2, 3 ,4, 5 аас сонгоно уу: ")

if level == "1":
    max_number = 50
    max_attempts = 8
    score_base = 10
elif level == "2":
    max_number = 100
    max_attempts = 6
    score_base = 20
elif level == "3":
    max_number = 150
    max_attempts = 4
    score_base = 30
else:
    print("Буруу сонголт!")
    exit()


random_num = random.randint(1, max_number)

attempts = 0
while attempts < max_attempts:
    try:
        input_num = int(input("Enter number? "))
        attempts += 1
        if input_num < 1 or random_num > max_number:
            print(f"Алдаа: Та 1-ээс {max_number} хооронд тоо оруулна уу!")
        elif input_num < random_num:
            print("Таны тоо бага байна!")
        elif input_num > random_num:
            print("Таны тоо их байна!")
        else:
            final_score = score_base * (max_attempts - attempts + 1)
            print(f"Баяр хүргэе! Та {attempts} оролдлогоор зөв таалаа.")
            print(f"Таны оноо: {final_score}")
            break
    except ValueError:
        print("Алдаа: Зөвхөн тоо оруулна уу!")

if attempts == max_attempts:
    print("Таны оролдлого дууслаа! Зөв тоо:", input_num)
