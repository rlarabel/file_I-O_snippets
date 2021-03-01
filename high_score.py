def main():
    list_of_entries = []
    highest_score = 0
    with open('scores.txt', mode='r') as scores_on_file:
        for entry in scores_on_file:
            entry = entry.rstrip('\n')
            name, score = entry.split(',')
            score = int(score)
            list_of_entries.append([name, score])
            if highest_score < score:
                highest_score = score
                winner = name

    print('Total number of entries: ', len(list_of_entries))
    print('With a score of', highest_score, ',', winner, 'is the winner')


main()
