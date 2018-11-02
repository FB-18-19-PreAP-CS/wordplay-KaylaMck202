import re
def at_least():
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                if len(word) >= 20:
                    print(word)
                
def has_no_e(word):
    if 'e' not in word.lower():
        return True
    else:
        return False
#        print(float(count_e/count_word)*100)
def no_e():
    count_word = 0
    count_e = 0
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                count_word += 1
                if has_no_e(word) == True:
                    count_e += 1
                pct = float(count_e/count_word)
        print(f"{pct*100:.3f} %")
    

        
#    with open("words.txt") as file:
#        count_the = 0
#        for line in file:
#            for word in line.strip().split():
#                    count_the += 1
#        print(count_the)
    
#    with open("island.txt") as file:
#        count_the = 0
#        for line in file:
#            for word in line.strip().split():
#                if 'the'in word.lower():
#                    count_the += 1
#        print(count_the)
    
#    with open("island_short.txt") as file:
#        count_the = 0
#        for line in file:
#            for word in line.strip().split():
#                if 'the'in word.lower():
#                    count_the += 1
#                    print(word)
    
#    with open("island_short.txt") as file:
#        count_the = 0
#        for line in file:
#            for word in line.split(' '):
#                if 'the'in word.lower():
#                    count_the += 1
#        print(count_the)
        
#    with open("island_short.txt") as file:
#        count_the = 0
#        for line in file:
#            for word in line.split(' '):
#                if word.lower() == 'the':
#                    count_the += 1
#        print(count_the)
    
#    with open("island_short.txt") as file:
#        for line in file:
#            for word in line.split(' '):
#                print(word)


if __name__ == "__main__":
    no_e()
    #at_least()