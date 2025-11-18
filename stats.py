def get_num_words(file_content: str) -> int:
    all_words = file_content.split()
    return len(all_words)


def get_dict_of_characters(file_content: str) -> dict[str, int]:
    all_characters = {}
    for word in file_content.split():
        for character in word.lower():
            if character in all_characters:
                all_characters[character] += 1
                continue
            all_characters[character] = 1

    return all_characters


def sort_on(items: dict) -> int:
    return items["num"]


def get_character_count(dict_of_characters: dict[str, int]) -> list[dict[str, int]]:
    dict_of_characters_count = []
    for key, value in dict_of_characters.items():
        if key not in dict_of_characters_count:
            dict_of_characters_count.append({"char": key, "num": value})
            continue

    dict_of_characters_count.sort(reverse=True, key=sort_on)

    return dict_of_characters_count
