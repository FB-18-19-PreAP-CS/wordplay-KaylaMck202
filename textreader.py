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

def avoids(word, forbidden_letters):
    for letter in word:
        for ele in forbidden_letters:
            if ele in word.lower():
                return False
        else:
            return True
            
    
def count_avoids():
    count_avoid = 0
    forbidden_let = input(str("Enter the forbidden letters: "))
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                if avoids(word,forbidden_let)== True:
                    count_avoid +=1
        print(count_avoid)

def uses_only(word, lett):
    for letter in word:
        for ele in lett:
            if ele not in word.lower():
                return False
    else:
        return True
def words_with_only():
    lett = input(str("Enter a string of letters: "))
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                if uses_only(word,lett)== True:
                    print(word)
                    
def uses_all(word, req_lett):
    for letter in word:
        for ele in req_lett:
            if ele not in word.lower():
                return False
        else:
            return True
def how_many_uses_all():
    count_all = 0
    req_let = input(str("Enter a string of required letters: "))
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                if uses_all(word,req_let) == True:
                    count_all +=1
        print(count_all)
        
def is_abecedarian(word):
    for i in range(len(word)-1):
        if word[i] > word[i+1]:
            i +=1
            return False
    else:
        return True
    
def count_abecedarian():
    count = 0
    with open("words.txt") as file:
        for line in file:
            for word in line.strip().split():
                if is_abecedarian(word) == True:
                    count += 1
        print(count)
    
   #pass
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
    import doctest
    doctest.testmod()
    count_abecedarian()
    #how_many_uses_all()
    #words_with_only()
    #count_avoids()
    #no_e()
    #at_least(