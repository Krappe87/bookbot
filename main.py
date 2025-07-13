from stats import get_num_words, get_letter_count
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        book_text = f.read()
        num_words_string = get_num_words(book_text)
        letter_data = get_letter_count(book_text)
        return num_words_string, letter_data
        
def main(book_path):
    num_words, data = get_book_text(book_path)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {book_path}...\n----------- Word Count ----------")
    print(num_words)
    print("--------- Character Count -------")
    for each in data:
        #print(each["char"])
        if each["char"].isalpha() is True:
            print(f"{each["char"]}: {each["num"]}")
    print("============= END ===============")

try:            
    book_path = sys.argv[1]
except Exception as e:
    print("Usage: python3 main.py <path_to_book>")
    exit(1)
        
main(sys.argv[1])

        