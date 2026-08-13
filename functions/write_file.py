import os

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Overwrites file content in a specified path relative to the working directory.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path, relative to the working directory (default is the working directory itself)",
                },
                "content": {
                    "type": "string",
                    "description": "Updated file content"
                }
            },
        },
    },
}


def write_file(working_directory: str, file_path: str, content: str) -> str:
    working_dir_abs = os.path.abspath(working_directory)

    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
    if os.path.isdir(target_file):
        return f'Error: Cannot write to "{file_path}" as it is a directory'

    valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

    if not valid_target_file:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        with open(target_file, "w") as f:
            f.write(content)
    except Exception as e:
        return "Error: " + str(e)

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
