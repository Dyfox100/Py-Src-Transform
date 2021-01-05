import pytest

import pytransformation
from pytransformation import Source_Code_Transformer
from .test_file_utilities import get_all_test_and_result_files


test_dir_name = "source_code_transformer"


@pytest.fixture(params=get_all_test_and_result_files(test_dir_name))
def test_and_result_strings(request):
    return request.param


@pytest.fixture(scope="function")
def transformer_and_mocks(mocker):
    mock1 = mocker.spy(pytransformation, "_move_var_decls_to_top_of_scope")
    mock2 = mocker.spy(pytransformation, "_make_for_loops_while")

    transformer = Source_Code_Transformer([
        pytransformation._move_var_decls_to_top_of_scope,
        pytransformation._make_for_loops_while
    ])
    return (transformer, (mock1, mock2))


def test_SCT_calls_transfroms_correct_num_times(mocker,
                                                transformer_and_mocks,
                                                test_and_result_strings):

    transformer = transformer_and_mocks[0]
    transformer.transform(test_and_result_strings[0])
    mocks = transformer_and_mocks[1]
    # First test file has 4 functions in one module, so 5 scope opening
    # objects, so all transforms should be called 5 times.
    for mock in mocks:
        assert mock.call_count == 5


def test_SCT_resets_name_dict_after_transforming(transformer_and_mocks,
                                                 test_and_result_strings):
    transformer = transformer_and_mocks[0]
    assert transformer._names_in_use == {}
    transformer.transform(test_and_result_strings[0])
    assert transformer._names_in_use == {}
