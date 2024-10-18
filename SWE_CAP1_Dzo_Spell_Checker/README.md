# SWE_CAP1_Dzo_Spell_Checker


## project overview

My code is too short and easy to understand except for main spelling checker.
Main purpose of this code is to first convert the dictionary.docx to txt and download input file.txt then compare and check for spelling mistake found in input file.

In input file.
1) import requests = to make HTTP download contais from URL
2) url = contains the link to the file that will be downloaded
3) wb = it can write any type of content

In dictionary file.
1) docx2txt = it reads the docx file and extract its text content
2) file.write(doc) = text content extracted from the .docx file(doc) to the newly created .txt file
3) file.close() = closes the txt file ensuring that all data is written to the file

 Clearing.
 1) import re = provides tools for working with regular expression
 2) clear_tex= this replace all occurrence of the pattern in the texts with replacement.
 3) 'w' = the code open the same file in write mode and write the cleared text back to it 

 spelling checker.
 1) load_dictionary(file_path) = The function is defined to load a dictionary from a specified file path.
 2) find_misspelled_words(letter_file, dictionary_file) = The function is defined to find misspelled words in a given letter file based on a dictionary file.
 3) misspelled_words.append((line_number, position + 1, word)) = For each word, it removes non-alphanumeric characters and checks if the cleaned word is in the dictionary

 ## USAGE

 load_dictionary(file_path): Loads the dictionary from the specified file.
find_misspelled_words(letter_file, dictionary_file): Checks the letter file against the dictionary and identifies any misspelled words.

Input Formats
Dictionary File (DZO ORGINAL.txt)
Letter File (358.txt)

Output Formate
line13,word position11,'ཆེན is incorrect

##  Implementation

The code is a Python script for spell checking a text file. It first downloads a text file from a web URL and converts it from a docx file to a txt file. It then defines two functions: load_dictionary() and find_misspelled_words(). The load_dictionary() function takes a file path as input and returns a set of words from the file. The find_misspelled_words() function takes a letter file and a dictionary file as input, and returns a list of misspelled words.

The main part of the code checks if there are misspelled words in the letter file and then prints the output. If there are no misspelled words, it will print a message indicating that no misspelled words were found. The code uses a dictionary file for checking the spelling.

Overall, the script defines a function to load a dictionary file from a file path and another function to find misspelled words. The main part of the code calls these functions and prints the output, which includes the line number, word position, and the misspelled word.

## data structure 

1. set (within load_dictionary function)

Purpose: A set is used to store the words from the dictionary file.
Why: Sets are highly optimized for lookups (checking if a word exists). This is crucial for efficient spell checking. Sets prevent duplicates, ensuring only unique words are stored.

2. list (within find_misspelled_words function)

Purpose: A list is used to store the misspelled words and their context.
Why: Lists are ordered sequences, allowing you to maintain the line number and word position where the misspelled word was found.

3. list (within find_misspelled_words function)

Purpose: A list is used to store the words in a line.
Why: Lists are ordered sequences, preserving the order of words in a line.

4. tuple (inside find_misspelled_words function):

Purpose: To group the line number, word position, and the misspelled word together.
Why a tuple?
Immutability: Tuples are immutable (cannot be changed) once created. This ensures that the information about a misspelled word stays consistent and can be easily processed later.

## Algorithm
 
1. Dictionary Loading and Cleaning:

File Reading: The load_dictionary function reads the dictionary file ("C:\Users\LENOVO\Desktop\/CSF assignment20 ORGINAL.txt") line by line using f.readlines().
Word Stripping: It then processes each line (word) by removing leading and trailing whitespace using word.strip().
Set Conversion: Finally, it converts the list of words into a set (return set(...)), which provides efficient membership testing during lookup. This approach is particularly effective for checking if a word exists in the dictionary.

2. Misspelled Word Detection:

File Reading: Similar to the dictionary loading, the find_misspelled_words function reads the input text file (e.g., "158.txt") line by line.
Word Tokenization: It splits each line into words using line.split("").
Character Cleaning: For each word, it removes non-alphanumeric characters using clean_word.join(char for char in word if char.isalnum()).
Dictionary Lookup: It then checks if the cleaned word is present in the dictionary set using if clean_word and clean_word not in dictionary:.
Misspelled Word Recording: If a word is not found in the dictionary, it is recorded as misspelled along with its line number and position within the line.

3. Output:

The code iterates through the list of misspelled words and prints information about each misspelled word, including the line number, position, and the word itself.

## challanges and soluttion 
 I faced a solution when i try to clear the punctation mark using the re.sub() for number and words it did work like i used re.sub(A-z,a-b,0-9) but for punctation i used unicode u+0000-u+10FFFF but it didnt work so i used chat gpt to find the mistake but the ai is generating a new code to me.

## future improvement 

Through this code i think i will be able to make a dzongkha spelling checker for students and teachers

##  REFERENCE
#https://youtu.be/Mi3j54ZMxOc
https://www.blackbox.ai/chat/expert-python
