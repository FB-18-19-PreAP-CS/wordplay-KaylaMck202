def palindrome():
    for i in range(1000000):
        num = str(i).zfill(6)
        if num[2:] == num[5:1:-1]:
            
if __name__ == "__main__":
    palindrome()