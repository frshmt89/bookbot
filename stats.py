def wordcount(text):
    return len(text.split())

def convert(book):
    count = {}
    for char in book:
        char = char.lower()
        # print(char)
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count