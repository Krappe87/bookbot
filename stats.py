def get_num_words(document):
    count = 0
    listed_doc = document.split()
    for word in listed_doc:
        count += 1
    return f"Found {count} total words"

def get_letter_count(word_list):
    listed_doc = word_list.split()
    letters = {}
    for words in listed_doc:
        for letter in words:
            letter = letter.lower()
            if letter not in letters:
                letters[letter] = 1
            else:
                letters[letter] += 1
    nested_letters = [{"char": char, "num": num} for char, num in letters.items()]    
    nested_letters.sort(reverse=True, key=sort_data)
    return nested_letters

def sort_data(data):
    return data["num"]