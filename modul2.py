"""Перевірка паліндрома.

Модуль реалізує функцію для визначення, чи є переданий рядок паліндромом,
використовуючи двосторонню чергу (deque) з модуля collections.
Перевірка нечутлива до регістру та пробілів, коректно працює з рядками
з парною та непарною кількістю символів.
"""

from collections import deque


def is_palindrome(text: str) -> bool:
    """Check whether the given string is a palindrome.

    The check is case-insensitive and ignores spaces.
    Works correctly for both even- and odd-length strings.
    """
    # Normalize: lowercase and remove spaces.
    normalized = text.lower().replace(" ", "")

    # Add all characters to a deque.
    char_deque = deque(normalized)

    # Compare characters from both ends until at most one character remains.
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False

    return True


def main() -> None:
    test_cases = [
        "racecar",       # palindrome (odd length)
        "madam",         # palindrome (odd length)
        "A man a plan a canal Panama",  # palindrome (spaces + mixed case)
        "hello",         # not a palindrome
        "Never odd or even",            # palindrome (spaces + mixed case)
        "abba",          # palindrome (even length)
        "ab",            # not a palindrome
        "",              # empty string — palindrome by definition
    ]

    for text in test_cases:
        result = is_palindrome(text)
        label = "паліндром" if result else "не паліндром"
        print(f'"{text}" -> {label}')


if __name__ == "__main__":
    main()
