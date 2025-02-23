from random import randint

def random_lottery_numbers() -> list:
    lottery_numbers=[]
    while len(lottery_numbers)!=6:
        number=randint(1, 49)
        if number not in lottery_numbers:
            lottery_numbers.append(number)
    return lottery_numbers

def main():
    lottery_numbers=random_lottery_numbers()
    print(f"Drawn lottery numbers: {sorted(lottery_numbers)}")

if __name__=="__main__":
    main()