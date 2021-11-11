import re


def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


def main():
    dictionary = open("dictionary.txt")

    dictionary_list = []

    for word in dictionary:
        word = word.strip()

        dictionary_list.append(word)

    dictionary.close()

    print("--- Linear Search ---")

    story = open("AliceInWonderLand200.txt")

    line_number = 0
    for line in story:
        word_list = split_line(line)
        line_number += 1
        for word in word_list:
            current_list_pos = 0
            while current_list_pos < len(dictionary_list) and dictionary_list[current_list_pos] != word.upper():
                current_list_pos += 1

                if current_list_pos == len(dictionary_list):
                    print(f"Line: {line_number} possible misspelled word: {word}")

    story.close()

    print("--- Binary Search ---")

    story = open("AliceInWonderLand200.txt")

    line_number = 0
    for line in story:
        word_list = split_line(line)
        line_number += 1
        for word in word_list:
            lower_bound = 0
            upper_bound = len(dictionary_list) - 1
            found = False
            while lower_bound <= upper_bound and not found:
                middle_pos = (lower_bound + upper_bound) // 2

                if dictionary_list[middle_pos] < word.upper():
                    lower_bound = middle_pos + 1
                elif dictionary_list[middle_pos] > word.upper():
                    upper_bound = middle_pos - 1
                else:
                    found = True

            if not found:
                print(f"Line: {line_number} possible misspelled word: {word}")


main()