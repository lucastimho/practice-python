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
phone = re.search("\d{3}-\d{3}-\d{4}", text)
print(phone.span())
print(phone.group())
phone_pattern = re.compile("(\d{3})-(\d{3})-(\d{4})")
results = re.search(phone_pattern, text)
print(results.group())
print(results.group(2))