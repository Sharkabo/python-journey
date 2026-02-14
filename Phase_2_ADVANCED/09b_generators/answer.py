from typing import Any

def stream_log_data(filename: str)-> Any:
    with open(filename, "r", encoding='utf-8') as file:
        for line in file:
            yield f"Processing: {line.strip()}"