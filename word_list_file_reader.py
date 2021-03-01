def main():
    list_of_words = []
    total_length = 0
    longest_word_id = 0
    with open('word_list.txt', mode='r') as file_reader:
        for entry in file_reader:
            entry = entry.rstrip('\n')
            entry = entry.replace(' ', '')
            list_of_words.append(entry)
            total_length += len(entry)
            if longest_word_id < len(entry):
                longest_word_id = len(entry)
                longest_word = entry

    print('Total number of words: ', len(list_of_words))
    print('Longest word on file: ', longest_word)
    print('Average length of all words on file: ', total_length/len(list_of_words))


main()
