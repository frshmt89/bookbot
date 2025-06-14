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

def sorted(count):
    characters = []
    for char, num in count.items():
        characters.append({"char": char, "num": num})
    characters.sort(reverse=True, key= lambda d: d["num"])
    return characters