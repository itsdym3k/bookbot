def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_count = {}  
    text = text.lower() 
    
    for char in text:  
        if char in char_count:
            char_count[char] += 1 
        else:
            char_count[char] = 1 
            
    return char_count  

def sorted_character_counts(char_count):
    sorted_counts = [{char: count} for char, count in char_count.items() if char.isalpha()]
    
    sorted_counts.sort(key=lambda x: list(x.values())[0], reverse=True)
    
    return sorted_counts  
