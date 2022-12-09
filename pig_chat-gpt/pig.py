# Get the user's input
user_input = input("Enter a word or phrase: ")

# Split the user's input into a list of words
words = user_input.split()

# Loop through each word in the list
for i in range(len(words)):
  # Get the current word
  word = words[i]

  # If the word starts with a consonant, move the first consonant or cluster
  # of consonants to the end of the word and add "ay"
  if not word[0] in "aeiouAEIOU":
    consonant_cluster = ""
    for j in range(len(word)):
      if not word[j] in "aeiouAEIOU":
        consonant_cluster += word[j]
      else:
        break

    word = word[len(consonant_cluster):] + consonant_cluster + "ay"

  # Otherwise, if the word starts with a vowel, add "way" to the end of the word
  else:
    word += "way"

  # Update the current word in the list with the Pig Latin version
  words[i] = word

# Join the list of words back into a single string and print the result
pig_latin = " ".join(words)
print(pig_latin)
