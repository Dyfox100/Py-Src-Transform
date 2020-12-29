import ast
import astor

from .name_utils import _get_all_used_variable_names
from .convert_for_loops_to_while import _make_for_loops_while
from .move_var_decls_to_top_of_scope import _move_var_decls_to_top_of_scope
from .name_function_applications import _name_unnamed_applications


def normalize_to_ANF(source_string=None, source_file_path=None):
    """Entry Point for ANF normalization. Performs ANF Normalization over a
    source string or file.
    Parameters:
        source_string: a string of valid python code
        source_file_path: a file path to a file of valid python code.
    Returns:
        String of ANF Normalized python code."""

    def anf_normalization_helper(ast_node, variables_scoped, names_used):
        """helper function to recur down tree normalizing source code."""
        ast_node, names_used = _make_for_loops_while(ast_node, names_used)
        ast_node, names_used = _name_unnamed_applications(ast_node, names_used)
        ast_node, variables_scoped = \
            _move_var_decls_to_top_of_scope(ast_node, variables_scoped)
        for child_node in ast.iter_child_nodes(ast_node):
            child_node = anf_normalization_helper(child_node,
                                                  variables_scoped,
                                                  names_used)
        return ast_node

    if source_string is not None and source_file_path is None:
        src = source_string
    elif source_file_path is not None and source_string is None:
        with open(source_file_path, 'r') as src_file:
            src = src_file.read()
    else:
        raise ValueError('Exactly One of Source String and Source File Path'
                         + 'must be passed in.')

    ast_root_node = ast.parse(src)
    all_variables_used = _get_all_used_variable_names(ast_root_node)
    anf_normalized_ast = anf_normalization_helper(ast_root_node,
                                                  {},
                                                  all_variables_used)
    anf_normalized_source_string = astor.to_source(anf_normalized_ast)

    return anf_normalized_source_string
