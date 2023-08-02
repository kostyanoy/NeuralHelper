import importlib
import os


# import .py file
def import_by_path(file_path: str):
    path_to_module, module_name = os.path.split(file_path)
    module_name.replace(".py", "")

    spec = importlib.util.spec_from_file_location(module_name, file_path)
    test_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(test_module)
    return test_module


# check module attributes
def check_module_vars(module, attrs) -> (str, bool):
    for v in attrs:
        if not hasattr(module, v):
            return f"Chosen file have no {v}", False
        return "Success", True
