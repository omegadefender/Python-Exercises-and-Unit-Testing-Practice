names = ['Emma', 'James', 'Charlotte', 'Christopher']
vowels = 'aeiouAEIOU'
found_names = list()

for name in names:
    for char in vowels:
        if name.startswith(char):
            found_names.append(name)

print(found_names)