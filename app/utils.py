def snake_to_camel(snake: str) -> str:
    """
    Convert snake_case to camelCase.
    """
    words = snake.split("_")
    return words[0].lower() + "".join(word.capitalize() for word in words[1:])
