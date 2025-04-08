# File: text_wizard.py

class text_wizard:

    @staticmethod
    def word_count(text):
        return len(text.split())

    @staticmethod
    def char_count(text):
        return len(text)

    @staticmethod
    def unique_words(text):
        return set(text.lower().split())

    @staticmethod
    def reverse_text(text):
        return text[::-1]

    @staticmethod
    def to_upper(text):
        return text.upper()

    @staticmethod
    def to_lower(text):
        return text.lower()

    @staticmethod
    def title_case(text):
        return text.title()

    @staticmethod
    def replace_word(text, old, new):
        return text.replace(old, new)

    @staticmethod
    def word_frequency(text):
        words = text.lower().split()
        return {word: words.count(word) for word in set(words)}

    @staticmethod
    def average_word_length(text):
        words = text.split()
        return round(sum(len(word) for word in words) / len(words), 2) if words else 0
