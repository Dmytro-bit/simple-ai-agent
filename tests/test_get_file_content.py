from functions.get_file_content import get_file_content

if __name__ == "__main__":
    result = get_file_content("calculator", "lorem.txt")
    print(f"lorem.txt length: {len(result)}")
    print(f"lorem.txt truncated: {'truncated' in result}")


    result = get_file_content("calculator", "../main.py")
    print(f"lorem.txt length: {len(result)}")
    print(f"lorem.txt truncated: {'truncated' in result}")
    print(result)

    result = get_file_content("calculator", "pkg/calculator.py")
    print(f"lorem.txt length: {len(result)}")
    print(f"lorem.txt truncated: {'truncated' in result}")
    print(result)

    result = get_file_content("calculator", "/bin/cat")
    print(f"lorem.txt length: {len(result)}")
    print(f"lorem.txt truncated: {'truncated' in result}")
    print(result)

    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print(f"lorem.txt length: {len(result)}")
    print(f"lorem.txt truncated: {'truncated' in result}")
    print(result)