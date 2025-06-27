def get_book_text(filepath):
    """
    Reads the entire contents of a text file and returns it as a string.

    Parameters:
        filepath (str): Relative or absolute path to the text file.

    Returns:
        str: The full contents of the file as a single string.
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()
