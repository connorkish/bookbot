def main():

    # Define Variables and Call Functions
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    word_count = count_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    # Output Report
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []

    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def get_chars_dict(text):
    chars = {}

    for char in text:
        lowered = char.lower()

        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def count_words(text):
    words = text.split()
    return len(words)

def get_text(path):
    with open(path) as f:
        return f.read()
    
main()
