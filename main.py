file_path = "books/frankenstein.txt"

with open(file_path) as f:
    file_content = f.read()

words = file_content.split()

# print(words)

def get_letter_count_dict(text):
    letter_counts = {}
    for letter in text:
        if letter.isalpha():
            if letter.lower() in letter_counts:
                letter_counts[letter.lower()] += 1
            else:
                letter_counts[letter.lower()] = 1
    return letter_counts

letter_dict = get_letter_count_dict(file_content)

print(f"--- Begin report of {file_path} ---")
print(f"{len(words)} words found in the documnt\n")

letter_list = {k: v for k, v in sorted(letter_dict.items(), key=lambda item: item[1], reverse=True)}

for letter in letter_list:
    print(f"The '{letter}' character was found {letter_list[letter]} times")

print("--- End report ---")