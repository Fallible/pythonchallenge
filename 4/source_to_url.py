import urllib.request

with urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345') as f:
    print(f.read(100).decode('utf-8'))
nothing_value = str(12345)
for i in range(400):
    with urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + nothing_value) as f:
        page_source = f.read(100).decode('utf-8')
        #nothing_value = page_source[-5:] #4 digit number happened. Broke solution.
        #Next need to try matching number.
        print(nothing_value)

