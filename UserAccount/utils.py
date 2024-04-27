def sanitize_integer_values(data_dict):
    """
    Sanitizes the values in a dictionary, ensuring they are integers or set to 0.
    Args:
        data_dict (dict): The dictionary to be sanitized.
    Returns:
        dict: The sanitized dictionary with integer values or 0.
    """
    sanitized_dict = {}
    for key, value in data_dict.items():
        if isinstance(value, int):
            sanitized_dict[key] = value
        else:
            sanitized_dict[key] = 0
    return sanitized_dict


def values_list_to_values(source: list, key_list: list[str]):
    """
    Transforms a list of values into a list of dictionaries using the provided key list.

    Args:
        source (list): The source list of values.
        key_list (list): The list of keys for the resulting dictionaries.

    Returns:
        list: The transformed list of dictionaries.

    Raises:
        ValueError: If the source, key list, or their lengths do not match.

    Example:
        source = [[1, 'John'], [2, 'Jane']]
        key_list = ['id', 'name']
        result = values_list_to_values(source, key_list)
        # Output: [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]
    """
    if len(source) == 0:
        return []
    if not source or not key_list:
        raise ValueError("Source or key list cannot be empty.")
    if len(source[0]) != len(key_list):
        raise ValueError("Source and key list lengths do not match.")

    return [{key: value for key, value in zip(key_list, item)} for item in source]


def get_usertypes():
    return (1, 2, 3, 4)
