from stats import wordcount

def get_book_text(filepath):
    with open(filepath) as f:
        book = f.read()
    return book

# def wordcount(text):
#     return len(text.split())

book_name = get_book_text("./books/frankenstein.txt")
num_words = wordcount(book_name)
print(f"{num_words} words found in the document")

# def main():
#     print(get_book_text("./books/frankenstein.txt"))

# main()