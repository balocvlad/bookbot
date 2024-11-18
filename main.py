def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(count_words_book(file_contents))

def count_words_book(book):
    words = book.split()
    return(len(words))


main()