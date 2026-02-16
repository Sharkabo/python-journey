def connection_leak_test( content: str):
    file_ref = None
    try:
        with open("crash_test.txt", "w", encoding='utf-8') as file:
            file_ref = file
            file.write(content)
    except ValueError as e:
        print(f"The error is {e}")
    
    if file_ref:
        print(f"The file is closed: {file_ref.closed}")