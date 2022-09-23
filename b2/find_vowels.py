a_string = input('Enter String: ')
lowercase = a_string.lower()

vowel_conts = {}

for vowel in 'aeiou':
    count = lowercase.count(vowel)
    vowel_conts[vowel] = count
    
counts = vowel_conts.values()
total_vowels = sum(counts)
print(f'total vowels in string, {total_vowels}')
