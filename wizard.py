# File: text_wizard.py

class text_wizard:

    def word_count(text):
        return len(text.split())

    def char_count(text):
        return len(text)

    def unique_words(text):
        return set(text.lower().split())

    def reverse_text(text):
        return text[::-1]

    def to_upper(text):
        return text.upper()

    def to_lower(text):
        return text.lower()

    def title_case(text):
        return text.title()

    def replace_word(text, old, new):
        return text.replace(old, new)

    def word_frequency(text):
        words = text.lower().split()
        return {word: words.count(word) for word in set(words)}

    def average_word_length(text):
        words = text.split()
        return round(sum(len(word) for word in words) / len(words), 2) if words else 0
