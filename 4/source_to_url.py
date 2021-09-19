import urllib.request

nothing_value = str(12345)
for i in range(400):
    with urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + nothing_value) as f:
        page_source = f.read(100).decode('utf-8')
        #nothing_value = page_source[-5:] #4 digit number happened. Broke solution.
        #Next need to try matching number.
        if page_source == "Yes. Divide by two and keep going.":
            nothing_value = int(nothing_value)/2
        new_nothing = ""
        for i in page_source.split():
            if i.isdigit():
                new_nothing+=str(i)
        nothing_value = new_nothing
        print(nothing_value)
