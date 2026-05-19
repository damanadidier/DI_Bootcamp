# Predict the output of the following code snippets:



# >>> 3 <= 3 < 9

# >>> 3 == 3 == 3

# >>> bool(0)

# >>> bool(5 == "5")

# >>> bool(4 == 4) == bool("4" == "4")

# >>> bool(bool(None))

# x = (1 == True)
# y = (1 == False)
# a = True + 4
# b = False + 10

# print("x is", x)
# print("y is", y)
# print("a:", a)
# print("b:", b)
print(3 <= 3 < 9) #True 
print(3 == 3 == 3) #True
print(bool(0)) #False
print(bool(5 == "5")) #False
print(bool(4 == 4) == bool("4" == "4")) #True
print(bool(bool(None))) #False
x = (1 == True) #True
y = (1 == False) #False
a = True + 4 #5
b = False + 10 #10


# Exercise 2 : Longest word without a specific character


# Keep asking the user to input the longest sentence they can without the character “A”.
# Each time a user successfully sets a new longest sentence, print a congratulations message.

longest_sentence = ""
while True:
    user_sentence = input("Enter the longest sentence you can without the character 'A': ")
    if 'A' in user_sentence or 'a' in user_sentence:
        print("The sentence contains the character 'A'. Please try again.")
    elif len(user_sentence) > len(longest_sentence):
        longest_sentence = user_sentence
        print("Congratulations! You've set a new longest sentence without the character 'A'.")
    else:
        print("That's not longer than the current longest sentence. Try again.")

    
# Exercise 3: Working on a paragraph


# Find an interesting paragraph of text online. (Please keep it appropriate to the social context of our class.)
# Paste it to your code, and store it in a variable.
# Let’s analyze the paragraph. Print out a nicely formatted message saying:
# How many characters it contains (this one is easy…).
# How many sentences it contains.
# How many words it contains.
# How many unique words it contains.
# Bonus: How many non-whitespace characters it contains.
# Bonus: The average amount of words per sentence in the paragraph.
# Bonus: the amount of non-unique words in the paragraph.
paragraph = """In the heart of the bustling city, there was a small, hidden park that offered a tranquil escape from the chaos. The park was filled with vibrant flowers, towering trees, and a serene pond that reflected the clear blue sky. People from all walks of life would come to this oasis to relax, read a book, or simply enjoy the beauty of nature amidst the urban landscape."""
num_characters = len(paragraph)
num_sentences = paragraph.count('.') + paragraph.count('!') + paragraph.count('?')
num_words = len(paragraph.split())
unique_words = set(paragraph.split())
num_unique_words = len(unique_words)
num_non_whitespace_characters = len(paragraph.replace(" ", ""))
average_words_per_sentence = num_words / num_sentences
num_non_unique_words = num_words - num_unique_words
print(f"The paragraph contains {num_characters} characters.")
print(f"The paragraph contains {num_sentences} sentences.")
print(f"The paragraph contains {num_words} words.")
print(f"The paragraph contains {num_unique_words} unique words.")
print(f"The paragraph contains {num_non_whitespace_characters} non-whitespace characters.")
print(f"The average amount of words per sentence in the paragraph is {average_words_per_sentence:.2f}.")
print(f"The amount of non-unique words in the paragraph is {num_non_unique_words}.")
