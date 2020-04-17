'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
word = 'otherdaythythnfkernfuiealfthnrfaefiuthifo;erth'
def count_th(word, count = 0):
    curent_set = word[:2]
    next_word = ' '
    count = count
    if curent_set == 'th' and len(curent_set) == 2: 
        count += 1
        next_word = word[1 : len(word)]
        return count_th(next_word, count)
    elif curent_set != 'th' and len(curent_set) == 2:
        next_word = word[1 : len(word)]
        return count_th(next_word, count)
    else:  
        return count
    
    
    
    # TBC
    

print(count_th(word))