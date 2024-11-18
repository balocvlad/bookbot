def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(count_words_book(file_contents))
        print(count_letters(file_contents))

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


main()