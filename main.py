# Import the functions from stats.py
import sys
from stats import wordcount
from stats import convert
from stats import sorted

# What to do with the filepath that will be given further down.
def get_book_text(filepath):
    with open(filepath) as f:
        book = f.read()
    return book

# Assign the input from the CLI to a variable.
args = sys.argv

# If the length of the input isn't 2 (which it needs to be when the path is given) error out and show proper usage.
if len(args) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# Define variables
book_name = get_book_text(args[1]) # Get the filepath with the second index in the args list.
num_words = wordcount(book_name) # Count the words in the book.
sorted_words = sorted(convert(book_name)) # Sort words.
filepath = args[1] # Assign the second index in the list (the filepath) to the variable.

# Print report
print("============ BOOKBOT ============")
print(f"Analyzing book found at {filepath}...")
print("----------- Word Count ----------")
print(f"Found {num_words} total words")
print("--------- Character Count -------")
for entry in sorted_words:
    if entry["char"].isalpha():
        print(f"{entry['char']}: {entry['num']}")
print("============= END ===============")
