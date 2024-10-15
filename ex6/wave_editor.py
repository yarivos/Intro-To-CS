##############################
# FILE:'wave_editor'.py
# WRITERS:Yariv_Yarmus
# EXERCISE:intro2cs1 ex6 2021
# DESRIPTION: music composer and editor algorithm
# the standard output(screen).
##############################
from wave_helper import *
import math
import re
import sys


def get_average_2(lst1, lst2):
    """
    gets two lists and returns the average of each position in separate.
    :param lst1:
    :param lst2:
    :return: list of averages
    """
    average_lst = [(lst1[0] + lst2[0]) // 2, (lst1[1] + lst2[1]) // 2]
    return average_lst


def get_average3(lst1, lst2, lst3):
    """
    gets three lists and returns the average of each position in separate.
    :param lst1:
    :param lst2:
    :param lst3:
    :return: list of averages
    """
    average_lst = [(lst1[0] + lst2[0] + lst3[0]) // 3, (lst1[1] + lst2[1] + lst3[1]) // 3]
    return average_lst


def audio_inverse(wav_data: list):
    """
    inverses the audio sound of the edited wav file.
    :param wav_data: :list[int, list].
    :return: reversed list
    """
    inverse_audio_lst = []
    for i in range(len(wav_data[1]) - 1, -1, -1):
        inverse_audio_lst.append(wav_data[1][i])
    wav_data[1] = inverse_audio_lst


def negative_sound(wav_data: list):
    """
    inverts the parameters in side the list to their negatives of the edited wav file.
    :param wav_data:
    :return:
    """
    for i in range(len(wav_data[1])):
        wav_data[1][i][0] = - wav_data[1][i][0]
        wav_data[1][i][1] = - wav_data[1][i][1]
    return wav_data


def fasten_audio(wav_data: list):
    """
    speeds up the audio of the edited wav file.
    :param wav_data:
    :return:
    """
    for i in range(0, len(wav_data[1]) + 1):
        try:
            wav_data[1].pop(i + 1)
        except IndexError:
            break
    return wav_data


def slow_audio(wav_data: list):
    """
    slows down the audio of the edited wav file.
    :param wav_data:
    :return:
    """
    slow_audio_lst = []
    for i in range(0, len(wav_data[1])):
        slow_audio_lst.append(wav_data[1][i])
        try:
            slow_audio_lst.append(get_average_2(wav_data[1][i], wav_data[1][i + 1]))
        except IndexError:
            break
    wav_data[1] = slow_audio_lst
    return wav_data


def volume_up(wav_data: list):
    """
    strengthen the volume of the edited wav file.
    :param wav_data:
    :return:
    """
    for i in range(len(wav_data[1])):
        new_left_value = wav_data[1][i][0] * 1.2
        if new_left_value > 32767:
            new_left_value = 32767
        elif new_left_value < -32768:
            new_left_value = -32768
        new_right_value = wav_data[1][i][1] * 1.2
        if new_right_value > 32767:
            new_right_value = 32767
        elif new_right_value < -32768:
            new_right_value = -32768
        wav_data[1][i][0] = new_left_value
        wav_data[1][i][1] = new_right_value
    return wav_data


def volume_down(wav_data: list):
    """
    weakens the volume of the edited wav file.
    :param wav_data:
    :return:
    """
    for i in range(len(wav_data[1])):
        wav_data[1][i][0] = wav_data[1][i][0] // 1.2
        wav_data[1][i][1] = wav_data[1][i][1] // 1.2
    return wav_data


def dimming_filter(wav_data: list):
    """
    dimming the audio of the edited wav file.
    :param wav_data:
    :return:
    """
    if len(wav_data[1]) <= 1:
        return wav_data
    dimmed_lst = [get_average_2(wav_data[1][0], wav_data[1][1])]
    for i in range(1, len(wav_data[1]) - 1):
        try:
            dimmed_lst.append(get_average3(wav_data[1][i - 1], wav_data[1][i], wav_data[1][i + 1]))
        except IndexError:
            break
    dimmed_lst.append(get_average_2(wav_data[1][len(wav_data[1]) - 2], wav_data[1][len(wav_data[1]) - 1]))
    wav_data[1] = dimmed_lst
    return wav_data


def exit_menu(wav_data):
    """
    saves the edited wav file, user chooses the name of the file.
    :param wav_data:
    :return: NONE
    """
    while True:
        file_name_input = input(MESSAGE_DICT["SAVE_FILE_NAME"])
        if file_name_input == "" or " " in file_name_input or ".":
            try:
                save_value = save_wave(wav_data[0], wav_data[1], file_name_input)
            except AttributeError:
                print("you have entered an invalid file name.")
                continue
        if save_value == -1:
            print("you have entered an invalid file name.")
            continue
        return


def get_text_file():
    """
    opens a text file of choice and sends it to organise_for_compose function
    :return:list of numbers and letters for compose.
    """
    while True:
        file_name = input(MESSAGE_DICT["TEXT_FILE_NAME"])
        try:
            f_compose = open(file_name)
        except IOError:
            print("file name is invalid, please re-enter file name.")
            continue
        return organise_for_compose(f_compose)


def get_file_name():
    """
    opens a wav file of choice.
    :return: list[int, list]. data of the wav file of choice
    """
    while True:
        file_name = input(MESSAGE_DICT["WAV_FILE_NAME"])
        wav_data = load_wave(file_name)
        if wav_data == -1:
            print("file name is invalid, please re-enter file name.")
            continue
        return [wav_data[0], wav_data[1]]


def edit_wav_file(wav_data):
    """
    user chooses options for functions to use on the wav file opened.
    choices pointed in the dictionary below.
    :param wav_data: data of the wav file of choice
    :return:
    """
    while True:
        edit_choice = input(MESSAGE_DICT["EDIT_MENU"])
        if edit_choice < "1" or edit_choice > "8":
            print("you have entered an invalid choice.")
            continue
        WAV_EDIT_FUNC_DICT[edit_choice](wav_data)
        if edit_choice == "8":
            return


def organise_for_compose(compose_str):
    """
    receives the data for composing and sorts it into a list
    :param compose_str: has all the data for composing before sorting it.
    :return: list of numbers and letters for composing.
    """
    letter_lst = []
    for letters in compose_str:
        for letter in letters:
            if letter in "ABCDEFGQ" or letter.isnumeric():
                letter_lst.append(letter)
    letter_str = "".join(letter_lst)
    compose_list = re.split('(\d+)', letter_str)
    compose_list.pop(len(compose_list) - 1)
    return compose_list


def music_composer():
    """
    function opens a txt file of choice and composes the data to sound.
    functions saves the composition to file by user's choice.
    :return:
    """
    text_for_compose: list = get_text_file()
    MAX_VOLUME = 32767
    SAMPLE_RATE = 2000
    composed_lst = []
    for i in range(1, len(text_for_compose), 2):
        sample_per_cycle = SAMPLE_RATE / FREQUENCY_DICT[text_for_compose[i - 1]]
        sample_length = int(SAMPLE_RATE * (int(text_for_compose[i]) / 16))
        for j in range(sample_length):
            music_value = int(MAX_VOLUME * math.sin(math.pi * 2 * j / sample_per_cycle))
            if text_for_compose[i - 1] == "Q":
                music_value = 0
            composed_lst.append([music_value, music_value])
    edit_wav_file([SAMPLE_RATE, composed_lst])


def main():
    """
    user can use 3 options -
    1)edit an existing wav file.
    2)compose audio from text file.
    3)exit the program.
    :return:
    """
    while True:
        user_choice = input(MESSAGE_DICT["MAIN_MENU"])
        if not (user_choice in "123"):
            print("the value you have entered is invalid.")
            continue
        if user_choice == "1":
            wav_data = get_file_name()
            edit_wav_file(wav_data)
            continue
        if user_choice == "2":
            music_composer()
            continue
        if user_choice == "3":
            sys.exit()


FREQUENCY_DICT = {
    "A": 440,
    "B": 494,
    "C": 523,
    "D": 587,
    "E": 659,
    "F": 698,
    "G": 784,
    "Q": 1}

MESSAGE_DICT = {
    "MAIN_MENU":
        "Hello, please choose one of the following options:\n"
        "1) edit a wav file.\n"
        "2) compose a tune in a wav file format.\n"
        "3) exit the program.",

    "EDIT_MENU":
        "please choose one of the following edit options:\n"
        "1) inverse audio.\n"
        "2) negative sound.\n"
        "3) fasten audio speed.\n"
        "4) slow audio speed.\n"
        "5) volume up.\n"
        "6) volume down.\n"
        "7) dimming filter.\n"
        "8) go to edit end menu.\n",

    "WAV_FILE_NAME":
        "please enter the name of the wav file you'd like to edit.\n",

    "TEXT_FILE_NAME":
        "please enter the name of the text file you'd like to compose.\n",

    "SAVE_FILE_NAME":
        "enter a file name of choice to save the current edit.\n"}

WAV_EDIT_FUNC_DICT = {
    "1": audio_inverse,
    "2": negative_sound,
    "3": fasten_audio,
    "4": slow_audio,
    "5": volume_up,
    "6": volume_down,
    "7": dimming_filter,
    "8": exit_menu}

if __name__ == '__main__':
    main()
