import unittest

from functions.get_files_info import get_files_info


def _call_get_files(dir: str):
    return get_files_info("calculator", dir)

if __name__ == "__main__":
    print(_call_get_files(".."))
    print(_call_get_files("pkg"))
    print(_call_get_files("/bin"))
    print(_call_get_files("../../"))
    print(_call_get_files("../main.py"))
