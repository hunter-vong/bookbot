import sys
from stats import get_num_words, sort_on, character_count
from stats import sort_text

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def book_split(text):
    text = text.split()
    return f"{len(text)} words found in the document"

def main():
    if(len(sys.argv) < 2):
    	print("Usage: python3 main.py <path_to_book>")
    	sys.exit(1)

    book_path = sys.argv[1]
    book_contents = get_book_text(book_path)
    word_count = character_count(book_contents)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(get_num_words(book_contents))
    print("--------- Character Count -------")
    sorted_chars = sort_text(word_count)    
    print(sort_text(word_count))    
    print("---- Most Common Alphabet Chars ----")
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]
        if char.isalpha():
            print(f"{char}: {count}")



if __name__ == "__main__":
    main()



