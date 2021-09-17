# pythonchallenge.com/pc/def/0.html

import requests
math_value = 2 ** 38
r = requests.get('http://pythonchallenge.com/pc/def/' + str(math_value) + '.html')
print(r.text)
print(r.status_code)
