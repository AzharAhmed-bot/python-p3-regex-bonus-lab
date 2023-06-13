import re


my_regex = re.compile(r"Some weather we're having today, huh\?|It's such a lovely day today.|Maybe today's just not my day.")
text="Some weather we're having today, huh?"
found=re.findall(my_regex,text)
print(found)

