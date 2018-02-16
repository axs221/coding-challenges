import itertools

"""Coding Challenge: Generate all permutations of a list, up to a given number of characters in a string."""
available_items = ['R', 'G', 'B']

def flatten(list_of_lists):
    """Flatten list_of_lists one or more levels into an unnested list"""
    if isinstance(list_of_lists, list) and isinstance(list_of_lists[0], list):
        return [flatten(y) for x in list_of_lists for y in x]
    return list_of_lists

def get_permutations(current_string, items, length):
    """Generate all permutations of the items given."""
    permutations = []

    if length == 0:
        return current_string
    else:
        for item in items:
            string_part = current_string + item
            permutations.append(get_permutations(string_part, items, length - 1))

        return flatten(permutations)

results = get_permutations("", available_items, 5)

print(results)
