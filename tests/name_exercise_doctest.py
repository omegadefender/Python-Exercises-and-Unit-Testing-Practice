from itertools import dropwhile

def first_vowel(x):
    return x not in 'aeiouy'

def vowel(name):
    """ 
    Finds the first vowel in a name, and removes all chars precediing it.
    If the char is a y, it will be treated as a vowel or consonant.
    >>> vowel("joshua")
    'oshua'
    >>> vowel("chetna")
    'etna'
    >>> vowel("yvonne")
    'yvonne'
    >>> vowel("emma")
    'emma'
    >>> vowel("byron")
    'yron'
    >>> vowel("")
    'noname'
    >>> vowel("byon")
    'on'
    >>> vowel("yolanda")
    'olanda'
    >>> vowel("ng")
    'ng'
    """     
    schop = ''.join(dropwhile(first_vowel, name))
    if len(schop) > 1 and schop[0] == 'y' and schop[1] in 'aeiou':
        return schop[1:]   
    elif len(name) > 0 and schop == '':
        return name
    elif name == '':
        return "noname"
    else:
        return schop    

def name_speller(n):
    n = input("\nYour name please: ").lower()
    ncap = n.capitalize()
    nchop = vowel(n)
    if nchop != "noname":
        return (
            f"\n{ncap}?\n"
            f"{ncap} Fif{nchop} Stickal{nchop} Fif{nchop}\n"
            f"That's how you spell '{ncap}!'\n")
    else:
        return "\nDo you feel lucky?\nWell do you, punk?\n"

if __name__ == '__main__':
    import doctest
    doctest.testmod()