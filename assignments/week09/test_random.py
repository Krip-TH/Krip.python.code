import random

def test_random():
    #สุ่มเลขระหว่าง1-10เก็บไว้ในตัวแปรชื่อ random_number
    random_number = random.randint(1, 100)

    #รับค่าการทายเลขจากผู้ใช้ เก็บไว้ในตัวแปรชื่อ guess_number
    guess_number = input("what is your guess number?:")

    if random_number == guess_number:
    print("Congratulations")

    if random_number < guess_number:
    print("Too much")

    if random_number > guess_number:
    print("Too low")

    print(random_number)
    
test_random()