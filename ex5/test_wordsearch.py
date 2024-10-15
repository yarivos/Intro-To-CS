import os
import sys
import tempfile
import inspect

import wordsearch
from wordsearch import *

EX_DIR = 'Ex5-Examples'
OUTPUT_FILE = 'output.txt'


def get_python_path():
    for path in sys.path:
        if os.path.isfile(os.path.join(path, 'python.exe')):
            return os.path.join(path, 'python.exe')
    raise FileNotFoundError("python.exe not found")


def test_main(capsys):
    with tempfile.TemporaryFile() as words_file:
        with tempfile.TemporaryFile() as matrix_file:
            out = main(
                [words_file.name, matrix_file.name, OUTPUT_FILE, 'l'])
            assert out is None, f"args are OK but check_input_args returned " \
                                f"a value {out}"
            out = main(
                [words_file.name, matrix_file.name, OUTPUT_FILE, 'l', 1])
            assert type(
                out) is str, f"5 args but check_input_args didn't " \
                             f"return str {out}"
            out = main(
                [words_file.name, matrix_file.name, OUTPUT_FILE])
            assert type(
                out) is str, f"3 args but check_input_args didn't " \
                             f"return str {out}"

    captured = capsys.readouterr()
    assert not captured.out and not captured.err, (f"No prints allowed!\nGot: "
                                                   f"out: {captured.out}\n"
                                                   f"err: {captured.err}\n")


def test_check_input_args_files(capsys):
    with tempfile.TemporaryFile() as matrix_file:
        pass
    with tempfile.TemporaryFile() as words_file:
        out = check_input_args(
            [words_file.name, matrix_file.name, OUTPUT_FILE, 'l'])
        assert type(out) is str, f"matrix_file not found but " \
                                 f"check_input_args didn't return str {out}"

    with tempfile.TemporaryFile() as matrix_file:
        out = check_input_args(
            [words_file.name, matrix_file.name, OUTPUT_FILE, 'l'])
        assert type(out) is str, f"words_file not found but " \
                                 f"check_input_args didn't return str {out}"

    with tempfile.TemporaryFile(suffix='טקסט') as words_file:
        with tempfile.TemporaryFile() as matrix_file:
            out = check_input_args(
                [words_file.name, matrix_file.name, OUTPUT_FILE, 'l'])
            assert out is None, f"words_file name is in hebrew but " \
                                f"check_input_args returned str {out}"

    with tempfile.TemporaryFile() as words_file:
        with tempfile.TemporaryFile() as matrix_file:
            out = check_input_args([words_file.name, os.path.relpath(
                matrix_file.name), OUTPUT_FILE, 'l'])
            assert out is None, f"matrix_file name is in relative path but " \
                                f"check_input_args returned str {out}"

            out = check_input_args([words_file.name, os.path.realpath(
                matrix_file.name), OUTPUT_FILE, 'l'])
            assert out is None, f"matrix_file name is in absolute path but " \
                                f"check_input_args returned str {out}"

    with tempfile.TemporaryDirectory() as words_file:
        with tempfile.TemporaryFile() as matrix_file:
            out = check_input_args([words_file, matrix_file.name,
                                    OUTPUT_FILE, 'l'])
            assert type(
                out) is str, f"words_file name is a directory path but " \
                             f"check_input_args didn't return str {out}"

    captured = capsys.readouterr()
    assert not captured.out and not captured.err, (f"No prints allowed!\nGot: "
                                                   f"out: {captured.out}\n"
                                                   f"err: {captured.err}\n")


def test_check_input_args_directions(capsys):
    with tempfile.TemporaryFile() as words_file:
        with tempfile.TemporaryFile() as matrix_file:
            out = check_input_args([words_file.name, matrix_file.name,
                                    OUTPUT_FILE, 'lrlww'])
            assert out is None, f"directions contain duplicated letters but " \
                                f"check_input_args returned a value {out}"

            out = check_input_args(
                [words_file.name, matrix_file.name, OUTPUT_FILE, 'L'])
            assert type(out) is str, f"directions contain capital letters but " \
                                     f"check_input_args didn't return str {out}"

            out = check_input_args(
                [words_file.name, matrix_file.name, OUTPUT_FILE, 'l!'])
            assert type(
                out) is str, f"directions contain forbidden letters but " \
                             f"check_input_args didn't return str {out}"

            out = check_input_args(
                [words_file.name, matrix_file.name, OUTPUT_FILE, 'lj'])
            assert type(
                out) is str, f"directions contain forbidden letters but " \
                             f"check_input_args didn't return str {out}"

            out = check_input_args(
                [words_file.name, matrix_file.name, OUTPUT_FILE, 'Lע'])
            assert type(out) is str, f"directions contain forbidden " \
                                     f"letters but check_input_args " \
                                     f"didn't return str {out}"

    captured = capsys.readouterr()
    assert not captured.out and not captured.err, (f"No prints allowed!\nGot: "
                                                   f"out: {captured.out}\n"
                                                   f"err: {captured.err}\n")


def test_read_wordlist_file(capsys):
    words_dict = {
        ("agsgsa", "AGDSR4", "!$#WDS"): "read_wordlist_file sanity failed.",
        ('123',): "read_wordlist_file with one line failed.",
        tuple(): "read_wordlist_file with no lines failed."
    }
    for words, message in words_dict.items():
        words = list(words)
        content = ''.join(map(lambda r: r + '\n', words))
        fd, words_file = tempfile.mkstemp()
        open(words_file, 'w').write(content)
        words2 = read_wordlist_file(words_file)
        os.close(fd)
        assert words == words2, message + f"\nExpected: " \
                                          f"{words}.\nActual: {words2}."

    captured = capsys.readouterr()
    assert not captured.out and not captured.err, (f"No prints allowed!\nGot: "
                                                   f"out: {captured.out}\n"
                                                   f"err: {captured.err}\n")


def test_read_matrix_file(capsys):
    words_dict = {
        ("agsgsa", "AGDSR4", "!$#WDS"): "read_matrix_file sanity failed.",
        ('123',): "read_matrix_file with one line failed.",
        ('1', '2', '3'): "read_matrix_file with one letter in line failed.",
        tuple(): "read_matrix_file with no lines failed."
    }
    for words, message in words_dict.items():
        words = list(map(list, words))
        content = ''.join(map(lambda r: ','.join(r) + '\n', words))
        fd, words_file = tempfile.mkstemp()
        open(words_file, 'w').write(content)
        words2 = read_matrix(words_file)
        os.close(fd)
        assert words == words2, message + f"\nExpected: " \
                                          f"{words}.\nActual: {words2}."

    captured = capsys.readouterr()
    assert not captured.out and not captured.err, (f"No prints allowed!\nGot: "
                                                   f"out: {captured.out}\n"
                                                   f"err: {captured.err}\n")


def test_find_words_in_matrix_wide(capsys):
    for suffix in ['', '0', 'R', 'C', 'Z']:
        _find_words_in_matrix_wide(suffix)

    captured = capsys.readouterr()
    assert not captured.out and not captured.err, (f"No prints allowed!\nGot: "
                                                   f"out: {captured.out}\n"
                                                   f"err: {captured.err}\n")


def test_write_output_file(capsys):
    for result in [[('a', 2), ('b', 3)], [('a', 2)], []]:
        fd, filename = tempfile.mkstemp()
        write_output(result, filename)
        content = open(filename).read()
        expected = ''.join([','.join(map(str, i)) + '\n' for i in result])
        os.close(fd)
        assert content == expected, f"write_output_file failed!\n" \
                                    f"Actual: {content}\n" \
                                    f"Expected: {expected}"

    try:
        fd, filename = tempfile.mkstemp()

        result = [('a', 2), ('b', 3)]
        write_output(result, filename)
        content = open(filename).read()
        expected = ''.join([','.join(map(str, i)) + '\n' for i in result])
        assert content == expected, f"write_output_file failed!\n" \
                                    f"Actual: {content}\n" \
                                    f"Expected: {expected}"

        result = [('a', 3), ('b', 4)]
        write_output(result, filename)
        content = open(filename).read()
        expected = ''.join([','.join(map(str, i)) + '\n' for i in result])
        assert content == expected, f"write_output_file failed!\n" \
                                    f"Actual: {content}\n" \
                                    f"Expected: {expected}"
    finally:
        os.close(fd)

    captured = capsys.readouterr()
    assert not captured.out and not captured.err, (f"No prints allowed!\nGot: "
                                                   f"out: {captured.out}\n"
                                                   f"err: {captured.err}\n")


def _find_words_in_matrix_wide(suffix):
    directions = [filename[4:-4] for filename
                  in os.listdir(EX_DIR) if
                  filename.startswith('out_')]
    words = read_wordlist(os.path.join(EX_DIR, f'words{suffix}.txt'))
    matrix = read_matrix('os.path.join(EX_DIR, f'matrix{suffix}.txt'))
    for direction in set(directions):
        pairs = find_words(words, matrix, direction)
        actual = sorted(pairs)
        content = open(os.path.join(EX_DIR,
                                    f'out{suffix}_{direction}.txt'),
                       'r').read()
        expected = content[:-1].split('\n') if content else []
        expected = [i.split(',') for i in expected]
        expected = [(i[0], int(i[1])) for i in expected]
        expected = sorted(expected)
        assert actual == expected, f"SUFFIX: {suffix}\n" \
                                   f"DIRECTION: {direction}\n" \
                                   f"ACTUAL {actual}\n" \
                                   f"EXPECTED: {expected}"
    for direction1 in directions:
        for direction2 in directions:
            for direction3 in directions:
                direction_str = ''.join(set(
                    direction1 + direction2 + direction3))
                pairs = find_words_in_matrix(words, matrix, direction_str)
                actual = sorted(pairs)
                expected_dict = {}
                for direction in direction_str:
                    content = open(
                        os.path.join(EX_DIR, f'out{suffix}_{direction}.txt'
                                     ), 'r').read()
                    partial_exp = content[:-1].split('\n') if content else []
                    for word_count in partial_exp:
                        word, count = word_count.split(',')
                        if word in expected_dict:
                            expected_dict[word] += int(count)
                        else:
                            expected_dict[word] = int(count)
                expected = sorted([(word, count) for word, count in
                                   expected_dict.items()])
                assert actual == expected, f"SUFFIX: {suffix}\n" \
                                           f"DIRECTION: {direction_str}\n" \
                                           f"ACTUAL {actual}\n" \
                                           f"EXPECTED: {expected}"


def test_main_wide(capsys):
    directions = [filename[4:-4] for filename
                  in os.listdir(EX_DIR) if
                  filename.startswith('out_')]
    python_path = get_python_path()
    script = inspect.getsource(wordsearch)
    for direction in directions:
        sys.argv = [sys.argv[0],
                    os.path.join(EX_DIR, "words.txt"),
                    os.path.join(EX_DIR, "matrix.txt"),
                    OUTPUT_FILE,
                    direction]
        __name__ = '__main__'
        ret = exec(script)
        assert not ret, f"Return value of program is {ret} instead " \
                        f"of 0"
        actual = sorted(open(OUTPUT_FILE).read().split('\n'))
        expected = sorted(open(
            os.path.join(EX_DIR, f'out_{direction}.txt'),
            'r').read().split('\n'))
        assert actual == expected, f"DIRECTION: {direction}\n" \
                                   f"ACTUAL {actual}\n" \
                                   f"EXPECTED: {expected}"
    for direction1 in directions:
        for direction2 in directions:
            for direction3 in directions:
                direction_str = direction1 + direction2 + direction3
                sys.argv = [sys.argv[0],
                            os.path.join(EX_DIR, "words.txt"),
                            os.path.join(EX_DIR, "matrix.txt"),
                            OUTPUT_FILE,
                            direction_str]
                __name__ = '__main__'
                ret = exec(script)
                assert not ret, f"Return value of program is {ret} instead " \
                                f"of 0"
                actual = sorted(open(OUTPUT_FILE).read().split('\n'))
                expected_dict = {}
                for direction in set(direction_str):
                    content = open(
                        os.path.join(EX_DIR, f'out_{direction}.txt'), 'r'
                    ).read()
                    partial_exp = content[:-1].split('\n') if content else []
                    for word_count in partial_exp:
                        word, count = word_count.split(',')
                        if word in expected_dict:
                            expected_dict[word] += int(count)
                        else:
                            expected_dict[word] = int(count)
                expected = sorted([f'{word},{count}' for word, count in
                                   expected_dict.items()] + [''])
                assert actual == expected, f"DIRECTION: {direction_str}\n" \
                                           f"ACTUAL {actual}\n" \
                                           f"EXPECTED: {expected}"

    captured = capsys.readouterr()
    assert not captured.out and not captured.err, (f"No prints allowed!\nGot: "
                                                   f"out: {captured.out}\n"
                                                   f"err: {captured.err}\n")


'''
def test_wordsearch():
    directions = [filename[8:-4] for filename
                  in os.listdir('Ex5-Example Files') if
                  filename.startswith('outfile_')]
    for direction in directions:
        main(['Ex5-Example Files\\word_list.txt',
              'Ex5-Example Files\\mat.txt',
              'output.txt',
              direction])
        assert sorted(open('output.txt').read().split('\n')) == \
               sorted(open(f'Ex5-Example Files\\outfile_{direction}.txt',
                           'r').read().split('\n')), \
            "DIRECTION: {0}\nMINE {1}\nTHEIR: {2}".format(
                direction,
                sorted(open('output.txt').read().split('\n')),
                sorted(open(f'Ex5-Example Files\\outfile_{direction}.txt',
                            'r').read().split('\n'))
            )
'''
