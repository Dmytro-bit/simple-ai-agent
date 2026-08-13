import os
import subprocess

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Runs python file in a specified path relative to the working directory.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path, relative to the working directory (default is the working directory itself)",
                },
                "args": {
                    "type": "array",
                    "items": "string",
                    "description": "Optional arguments"
                }
            },
        },
    },
}


def run_python_file(
        working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    working_dir_abs = os.path.abspath(working_directory)

    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

    if not os.path.isfile(target_file):
        return f'Error: "{file_path}" does not exist or is not a regular file'

    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file'

    valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

    if not valid_target_file:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    try:
        command = ["python", target_file]

        if args:
            command.extend(args)

        result = subprocess.run(command, timeout=30, capture_output=True, text=True)

        if result.returncode != 0:
            return f"Process exited with code {result.returncode}"

        match (result.stdout, result.stderr):
            case (None, None):
                return "No output produced"
            case (stdout, None):
                return f"STDOUT: {stdout}"
            case (None, stderr):
                return f"STDERR: {stderr}"
            case _:
                return f"STDOUT: {result.stdout}" + "\n" + f"STDERR: {result.stderr}"


    except Exception as e:
        return f"Error: executing Python file: {e}"
