def ArrayCreator(n):
    Arr = []

    for i in range(0, n):
        tmp = int(input(f"Enter your {i + 1} number: "))
        Arr.append(tmp)

    return Arr

def average(Nums):
    return sum(Nums) / len(Nums)

def main():
    print(f"Array Middle = {average(ArrayCreator(int(input('N = '))))}")

if __name__ == '__main__':
    main()