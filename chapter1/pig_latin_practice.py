"""
Change a word to Pig Latin format.

1. 判断单词是否以元音开头
2. 如果是元音开头, 在单词末尾加上"way"
3. 如果是辅音开头, 将第一个辅音字母移到单词末尾, 然后加上"ay"
4. 返回转换后的单词
"""

# 定义元音元组
VOWELS = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

def vowels_begin_handler(word: str) -> str:
    """Change a word that begins with a vowel to Pig Latin format."""
    print(f"{word} is a vowel-beginning word.")
    pig_latin_word = word + "way"
    return pig_latin_word

def consonants_begin_handler(word: str) -> str:
    """Change a word that begins with a consonant to Pig Latin format."""
    print(f"{word} is a consonant-beginning word.")
    pig_latin_word = word[1:] + word[0] + "ay"
    return pig_latin_word

def pig_latin_formater(word: str) -> str:
    """Change a word to Pig Latin format."""
    print(f"Received word: {word}")
    first_letter = word[0]
    if first_letter in VOWELS:
        return vowels_begin_handler(word)
    else:
        return consonants_begin_handler(word)

if __name__ == "__main__":
    input_word = input("\nPlease input a word: ")
    pig_latin_word = pig_latin_formater(input_word)
    print(f"\nThe Pig Latin form of the word is: \033[91m{pig_latin_word}\033[0m\n")
