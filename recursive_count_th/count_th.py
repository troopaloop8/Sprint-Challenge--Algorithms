'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # filter out words where "th" is not possible
    if len(word) < 2:
        return 0
    # tests to see if word starts with th and then slices part of the word to test later parts of the string
    elif word[:2] == "th":
        return 1 + count_th(word[1:])
    # "th" is not in the word -- return
    else:
        return count_th(word[1:])
