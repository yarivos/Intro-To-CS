##############################
# FILE:hangman.py
# WRITER:Yariv_Yarmus
# EXERCISE:intro2cs1 ex4 2021
# DESRIPTION: Hangman game
# the standard output(screen).
##############################
import hangman_helper


# function receives a word pattern and letter and puts the letter in the correct
# place in the pattern according to the word
def update_word_pattern(word, pattern, letter):
    counter = 0
    pat_lst = []
    for i in pattern:  # splits the string notes into a list
        pat_lst.append(i)
    for i in word:
        if letter == i:
            pat_lst[counter] = i
        counter += 1
    pattern = "".join(pat_lst)  # assimilates the list to a string
    return pattern


# this function will run a whole game of hangman, it will return the final score
# of the game
def run_single_game(words_list, score):
    msg = 'let the game begin'
    game_word = hangman_helper.get_random_word(words_list)  # chooses a random word for the game
    wrong_guess_lst = []
    word_pattern = '_' * len(game_word)  # builds the initial, empty, pattern
    while not (word_pattern == game_word or score == 0):
        hangman_helper.display_state(word_pattern, wrong_guess_lst, score, msg)  # send the
        msg = ' lets choose again'  # changes the msg for the next round
        # next line calls the input function for the user to choose a word, letter or hint.
        choice_type, choice = hangman_helper.get_input()
        # checks which of the three options the user chose
        if choice_type == hangman_helper.LETTER:
            if len(choice) != 1 or not choice.islower():  # next lines check if input is valid
                msg = 'in order to guess a letter, enter a lowercase letter'
                continue
            if choice in wrong_guess_lst or choice in word_pattern:
                msg = 'you have already chose this letter, choose a different one'
                continue
            score -= 1  # if input is valid, score will change accordingly and the pattern
            if choice in game_word:
                word_pattern = update_word_pattern(game_word, word_pattern, choice)
                score += ((game_word.count(choice) * (game_word.count(choice) + 1)) // 2)
            else:  # if the chosen letter is not in the word
                wrong_guess_lst.append(choice)

        if choice_type == hangman_helper.WORD:
            if not choice.islower() or not choice.isalpha():  # check word vaildity
                msg = 'word must contain only lowercase letters'
                continue
            score -= 1
            if choice == game_word:  # incase the user choice was correct
                score += ((word_pattern.count('_') * (word_pattern.count('_') + 1)) // 2)
                word_pattern = choice
        # next lines take place if user asked for a hint
        if choice_type == hangman_helper.HINT:
            score -= 1
            hint_words = filter_words_list(words_list, word_pattern, wrong_guess_lst)
            new_hint_words = []
            if len(hint_words) > hangman_helper.HINT_LENGTH:  # checks if hint length is valid
                new_hint_words.append(hint_words[0])
                for i in range(1, hangman_helper.HINT_LENGTH):  # assimilates a new hint list
                    new_hint_words.append(hint_words[i * len(hint_words) // hangman_helper.HINT_LENGTH])
                hangman_helper.show_suggestions(new_hint_words)
            else:  # if hint length is valid it will occur
                hangman_helper.show_suggestions(hint_words)
    if score == 0:  # option for win or lose
        msg = 'you have lost the game! the word was: ' + str(game_word)
    else:
        msg = 'well done, you have won!'
    hangman_helper.display_state(word_pattern, wrong_guess_lst, score, msg)
    return score


# the game will initialize in this function

def main():
    # first few lines receives the "Rules" for the game
    score = hangman_helper.POINTS_INITIAL
    game_number = 1
    list_of_words = hangman_helper.load_words('words.txt')
    score = run_single_game(list_of_words, score)  # starts the first game
    while score != 0:
        msg = 'you have played ' + str(game_number) + ' game/s, your score is ' + str(
            score) + ' would you like to keep playing?'
        keep_playing = hangman_helper.play_again(msg)  # uses the function to check if user wants another round.
        if keep_playing:
            game_number += 1
            score = run_single_game(list_of_words, score)
        else:
            break
    if score == 0:  # if the player lost it prints the msg and checks if user wants another round
        msg = 'you have survived ' + str(game_number) + ' games'
        keep_playing = hangman_helper.play_again(msg)
        if keep_playing:
            main()


# function returns a filtered list of words for hints
def filter_words_list(words, pattern, wrong_guess_lst):
    match_words = []
    for current_word in words:  # runs through all words in the list
        bool_letter = True
        # next lines check if the words comply with the current pattern
        if len(current_word) == len(pattern):
            for current_letter in current_word:
                if current_letter in wrong_guess_lst:
                    bool_letter = False
                    break
                for i in range(len(current_word)):
                    if pattern[i] != '_':
                        if pattern[i] != current_word[i]:
                            bool_letter = False
                            break
                    if current_word[i] in pattern:
                        if current_word[i] != pattern[i]:
                            bool_letter = False
                            break
            if bool_letter:  # matching words will enter the new list
                match_words.append(current_word)
    return match_words


if __name__ == "__main__":
    main()
