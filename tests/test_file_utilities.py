from os import listdir
from os.path import isfile, join

def get_all_test_and_result_files(dir_path):
    """Reads content of all test and result files in the dir at dir_path into
    2d array of strings. All files should be named test_<number> or
    result_<number>. Each test file should have a result file.
        Parameters:
            dir_path: path of directory to look in.
        Returns:
            2d array of strings with test and result file content.
    """

    file_names = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]
    test_files = filter(lambda f: "test" in f, file_names)

    def get_number_from_test_file(file_name):
        file_without_dot_py = file_name.split(".py")[0]
        file_without_test_prefix = file_without_dot_py.split("_")[1]
        return int(file_without_test_prefix)
    try:
        list_of_test_numbers = map(get_number_from_test_file, test_files)
    except ValueError as e:
        print("File Not Understood! Ensure that files are named test_<number>")
        raise(e)

    test_strings = []
    result_strings = []
    try:
        for test_num in sorted(list_of_test_numbers):
            files_to_close = []
            test_file = "test_" + str(test_num) + ".py"
            result_file = "result_" + str(test_num) + ".py"
            test = open(join(dir_path, test_file), "r")
            files_to_close.append(test)
            result = open(join(dir_path, result_file), "r")
            files_to_close.append(result)
            test_strings.append(test.read())
            result_strings.append(result.read())

    except IOError as e:
        print("File not found!")
        print("Do all of your test files have properly named result files?")
        raise(e)
    finally:
        for file in files_to_close:
            file.close()

    return zip(test_strings, result_strings)
