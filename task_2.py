from collections import deque
import re

def is_palindrome(text: str) -> bool:
  transformed_text = re.sub(r"[!.,\s]", "", text)
  d = deque()
  [d.append(char) for char in transformed_text]

  res = True

  while len(d) != 0:
    if len(d) == 1:
      break
    
    left = d.popleft()
    right = d.pop()
    
    if left.lower() != right.lower():
      res = False
      break

  return res
