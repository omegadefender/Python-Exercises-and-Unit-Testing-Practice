from collections import Counter

poem = """
I'm nobody! Who are you? 
Are you nobody, too? 
Then there's a pair of us - don't tell! 
They'd banish us, you know. 

How dreary to be somebody! 
How public, like a frog 
To tell your name the livelong day 
To an admiring bog! 
"""

def char_remover(str):
    chars = ['!', '?', ',', '-']
    low_str = str.lower()
    for char in chars:
        low_str = low_str.replace(char, "")
    return low_str

def unique_words(str):
    word_set = set(char_remover(str).split())
    return word_set

def word_counter(str):
    low_str = char_remover(str).split()
    word_count = dict(Counter(low_str).most_common())    
    for key in list(word_count):
        if word_count[key] == 1:
            del word_count[key]
    return word_count

print("\nThis is a list of the unique words in your string...\n", unique_words(poem))
print("\nHere are the counts of words that appear multiple times in your string...\n", word_counter(poem))