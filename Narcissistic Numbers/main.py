def is_narcissistic(i):
    ls = [int(j) for j in str(i)]
    length = len(str(i))
    ans = []

    for j in range(length):
        tmp = ls[j] ** length
        ans.append(tmp)

    if sum(ans) != i:
        return False
    else:
        return True

def main():
    print(is_narcissistic(int(input("Enter NUM: "))))

if __name__ == '__main__':
    main()