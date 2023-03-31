
# initialize

phrase = input(f"Enter your text: ")
target = input(f"Enter the target word: ")

# convert to lowercase

target_lower = target.lower()
phrase_lower = phrase.lower()

# split phrase to a table

phrase = phrase_lower.split()

target_words = 0

# if the word can be found in the phrase, add one to counter

for the_word_can_be_found_in in phrase:
   if the_word_can_be_found_in == target_lower:
      target_words += 1

# outcomes

if target_words == 1:
  print(f"The word '{target}' is found {target_words} time in the text.")
else:
  print(f"The word '{target}' is found {target_words} times in the text.") 
