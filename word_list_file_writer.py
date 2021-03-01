def main():
    num_words = int(input('How many words do you want to type to a file: '))
    with open('word_list.txt', mode='w', newline='') as file_writer:
        for i in range(num_words):
            input_word = input('What word do you want to write to the file? ')
            file_writer.write(input_word + '\n')


main()
