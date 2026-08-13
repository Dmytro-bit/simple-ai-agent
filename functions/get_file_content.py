import os

from config import MAXIMUM_FILE_READ_LIMIT

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Return file content in a specified path relative to the working directory.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}

def get_file_content(working_directory: str, file_path: str) -> str:
    working_dir_abs = os.path.abspath(working_directory)

    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
    if not os.path.isfile(target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

    if not valid_target_file:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    try:
        with open(target_file, "r") as f:
            content = f.read(MAXIMUM_FILE_READ_LIMIT)
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAXIMUM_FILE_READ_LIMIT} characters]'

        return content
    except Exception as e:
        return "Error:" + str(e)
