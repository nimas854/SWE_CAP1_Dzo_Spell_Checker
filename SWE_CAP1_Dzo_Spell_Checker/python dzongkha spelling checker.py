# From black box and my brother
def load_dictionary(file_path):
    with open(r"C:\Users\LENOVO\Desktop\CSF assignment\DZO ORGINAL.txt", 'r', encoding='utf-8') as f:
        return set(word.strip() for word in f.readlines())

def find_misspelled_words(letter_file, dictionary_file):
    dictionary = load_dictionary(dictionary_file)
    misspelled_words = []

    with open( letter_file, 'r', encoding='utf-8') as f:
        for line_number, line in enumerate(f.readlines(), start=1):
            words = line.split("་")
            for position, word in enumerate(words):
                clean_word = ''.join(char for char in word if char.isalnum())
                if clean_word and clean_word not in dictionary:
                    misspelled_words.append((line_number, position + 1, word))

    return misspelled_words


letter_file = '358.txt'
dictionary_file = 'DZO ORIGINAL.txt'
misspelled = find_misspelled_words(letter_file, dictionary_file)


if misspelled:
    print("misspelled words found:")
    for line, position, word in misspelled:
        print(f"line{line},word position{position},'{word} is incorrect")    

else:
    print("No missplaced word found")


