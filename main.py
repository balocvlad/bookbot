book_path = "books/frankenstein.txt"

def main():
    with open(book_path) as f:
        file_contents = f.read()
        report(file_contents)

def count_words_book(book):
    words = book.split()
    return(len(words))

def count_letters(book):
    words = book.lower().split()
    letters = {}
    for word in words:
        for letter in word:
            if letter.isalpha():
                if letter in letters:
                    letters[letter] += 1
                else:
                    letters[letter] = 1
    return letters
def sort_letters_by_count(book):
    list_from_dict = []
    letters = count_letters(book)
    for letter in letters:
        list_from_dict.append(dict([("letter", letter), ("number", letters[letter])]))
    list_from_dict.sort(reverse = True, key = lambda x: x["number"])
    return list_from_dict

def report(dictionary):
    int_words_in_book = count_words_book(dictionary)
    list_letters_ordered_by_count = sort_letters_by_count(dictionary)
    print(f"*** Report of {book_path} ***\n")
    print(f"{int_words_in_book} words in document\n\n")
    for dictionary in list_letters_ordered_by_count:
        print(f"The '{dictionary["letter"]}' character was found {dictionary["number"]} times")


main()