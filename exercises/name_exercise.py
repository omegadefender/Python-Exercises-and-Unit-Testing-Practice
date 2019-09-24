from itertools import dropwhile
    
def id_consonants(x):
    return x not in 'aeiouy'

def vowel(name):  
    schop = ''.join(dropwhile(id_consonants, name))
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