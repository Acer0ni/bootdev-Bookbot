


def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
        words = file_contents.split()
        print(f"{len(words)} words found in the document")
        char_dict = count_letters(file_contents)
        for letter in char_dict:
            print(f"{letter} character was found {char_dict[letter]}")

def count_letters(target_string):
    lowered_string = target_string.lower()
    answer_dict = {}
    for letter in lowered_string:
        if letter in  answer_dict:
            answer_dict[letter] += 1
        else:
            answer_dict[letter] = 1
    return answer_dict



main()