import sys
from stats import get_num_words, count_characters, sorted_character_counts

def get_book_text(filepath):
    with open(filepath, 'r') as f:  
        file_contents = f.read()    
    return file_contents    

def main():
    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1] 
    book_text = get_book_text(filepath)
    
    num_words = get_num_words(book_text)  
    print(f"Found {num_words} total words")  
    
    char_count = count_characters(book_text)  
    sorted_counts = sorted_character_counts(char_count)  
    
    print("Character counts (sorted):")
    for item in sorted_counts:
        for char, count in item.items():  
            print(f"{char}: {count}") 

if __name__ == "__main__":
    main()
