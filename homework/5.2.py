def is_prime(num: int) -> bool:
    for i in range(2, num):
        if not num % i:
            return False
    return True


if __name__ == '__main__':
    while True:
        num = int(input('Input a number: '))
        if is_prime(num):
            print(str(num)+' is a prime')
        else:
            print(str(num)+' is not a prime')
