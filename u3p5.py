# Accept a sentence from the user
sentence = input("Enter a sentence: ")

# Remove leading and trailing spaces
print("\nOriginal Sentence:", repr(sentence))
print("After lstrip():", repr(sentence.lstrip()))
print("After rstrip():", repr(sentence.rstrip()))
print("After strip():", repr(sentence.strip()))

# Use the cleaned sentence for further operations
sentence = sentence.strip()

# (a) Search for a substring using find() and index()
substring = input("\nEnter a substring to search: ")

position = sentence.find(substring)
if position != -1:
    print("Substring found using find() at index:", position)
else:
    print("Substring not found using find().")

try:
    position = sentence.index(substring)
    print("Substring found using index() at index:", position)
except ValueError:
    print("Substring not found using index().")

# (b) Count occurrences of a specified word
word = input("\nEnter a word to count: ")
print("Occurrences of", repr(word), ":", sentence.count(word))

# (c) Replace a word or character
old = input("\nEnter the word or character to replace: ")
new = input("Enter the replacement: ")
print("After replace():", sentence.replace(old, new))

# (d) Split the sentence and join the words
words = sentence.split()
print("\nWords after split():", words)

joined_sentence = " ".join(words)
print("Sentence after join():", joined_sentence)

# (e) Demonstrate string immutability
print("\nDemonstrating String Immutability:")
if len(sentence) > 0:
    try:
        sentence[0] = 'X'
    except TypeError as error:
        print("Error:", error)
        print("Strings are immutable; characters cannot be changed by indexing.")
else:
    print("The sentence is empty, so no character can be modified.")

# (f) Sort words alphabetically
sorted_words = sorted(words, key=str.lower)
print("\nWords in Alphabetical Order:", sorted_words)