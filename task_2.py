from collections import deque
import re

def is_palindrome(text: str) -> bool:
  d = deque(re.sub(r"[!.,\s]", "", text))

  while len(d) > 1:
    if d.popleft().lower() != d.pop().lower():
      return False

  return True

palindrome = input("Введіть текст: ")

print(f'is_palindrome - {is_palindrome(palindrome)}')
