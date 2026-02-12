def count_words(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}

    words = [word.lower().strip(", . !") for word in text.split()]

    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts

def find_user(user_id: int, users: dict[int, str]) -> str | None:
    return users.get(user_id)

def process_input(value: int | str) -> str:
    if isinstance(value, int):
        return f'Number: {value}'
    elif isinstance(value, str):
        return f'Text: {value}'

def get_unique_tags(posts: list[dict[str, list[str]]]) -> set[str]:
    unique_tags: set[str] = set()

    for post in posts:
        tags_list = post.get('tags', [])
        
        for tags in tags_list:
            unique_tags.add(tags)
    
    return unique_tags