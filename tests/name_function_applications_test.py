import ast
import astor

from pytransformation import _name_unnamed_applications

def test_name_function_applications_names_functions():
    src_string = \
"""
func()
"""

    test_ast, test_names_used = _name_unnamed_applications(ast.parse(src_string), {})

    result_string = \
"""app0 = func()
"""

    assert(astor.to_source(test_ast) == result_string)
    assert(test_names_used == {'app0': 1})
