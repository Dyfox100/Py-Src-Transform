import pytest
import os

from .test_file_utilities import get_all_test_and_result_files

test_dir_name = "integration"


@pytest.fixture()
def test_and_result():
    return list(get_all_test_and_result_files(test_dir_name))


def test_integration_with_script_file(test_and_result):
    absolute_path = os.path.dirname(os.path.realpath(__file__))
    test_dir = os.path.join(absolute_path, "test_files", test_dir_name)
    in_file = os.path.join(test_dir, "testcase_1.py")
    out_file = os.path.join(absolute_path, "result_1.py")
    path_to_script = os.path.join(absolute_path, "..", "pytransformation.py")
    os.system(f"{path_to_script} {in_file} {out_file} -all")

    # read out_file and ensure it matches expected result.
    with open(out_file, "r") as f:
        actual = f.read()
    os.remove(out_file)
    assert (actual.strip() == test_and_result[0][1].strip()
            or actual.strip() == test_and_result[1][1].strip())


def test_integration_with_script_dir(test_and_result):
    absolute_path = os.path.dirname(os.path.realpath(__file__))
    test_dir = os.path.join(absolute_path, "test_files", test_dir_name,
                            "test_dir/")
    out_dir = absolute_path + os.path.sep
    path_to_script = os.path.join(absolute_path, "..", "pytransformation.py")
    os.system(f"{path_to_script} {test_dir} {out_dir} -all")
    files = []
    files.append(os.path.join(out_dir, "testcase_1.py"))
    files.append(os.path.join(out_dir, "testcase_2.py"))
    for out_file in files:
        # read out_file and ensure it matches expected result.
        with open(out_file, "r") as f:
            actual = f.read()
        os.remove(out_file)
        assert (actual.strip() == test_and_result[0][1].strip()
                or actual.strip() == test_and_result[1][1].strip())
