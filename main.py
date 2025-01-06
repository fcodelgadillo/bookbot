def main(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return(file_contents)

def word_count(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return len(file_contents.split())

def character_count(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        all_words = file_contents.split()
        words = [s.lower() for s in all_words]
        chars = {}
        for word in words:
            for c in word:
                if c in chars.keys():
                    chars[c] += 1
                else:
                    chars[c] = 1
    return chars

def print_report(path_to_file):
    print("--- Begin report of books/frankenstein.txt ---")
    print(str(word_count(path_to_file)) + " words found in the document")
    print()
    chars = character_count(path_to_file)
    for key, value in chars.items():
        print(f"The '{key}' character was found {value} times")
    
    print()
    print("--- End report ---")



print_report("books/frankenstein.txt")