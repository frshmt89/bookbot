def get_book_text(filepath):
    with open(filepath) as f:
        book = f.read()
    return book

def main():
    print(get_book_text("./books/frankenstein.txt"))

main()