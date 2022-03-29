text = "The agent's phone number is 408-555-1234. Call soon!!!"
print("phone" in text)

import re

pattern = "phone"
print(re.search(pattern, text))
print(re.search("Hello", text))
match = re.search(pattern, text)
print(match.span())
print(match.start())
print(match.end())
text = "one phone, two phones."
match = re.search(pattern, text)
print(match.span())
matches = re.findall(pattern, text)
print(matches)
for match in re.finditer(pattern, text):
  print(match.span())
text = "My phone number is 870-555-1234"
phone = re.search("\d\d\d-\d\d\d-\d\d\d\d", text)
print(phone.span())
print(phone.group())