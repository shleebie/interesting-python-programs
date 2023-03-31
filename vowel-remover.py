prompt = input("Enter your text: ")

# initiate a list of vowels

vowels = ['a','e','i','o','u','A','E','I','O','U']

# if vowels are present and can be found in the list
# remove vowels!

for if_vowel_is_present in prompt:
    if if_vowel_is_present in vowels:
        prompt = prompt.replace(if_vowel_is_present, '')

# output

print(prompt)
