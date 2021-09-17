import string
"""
This is work on pythonchallenge 1.  My initial move was to do the rotate_chr function seen below.  After I did the rotation, the text said I should have used maketrans(), so I did it that way too.

Interesting to me that my initial attempt at maketrans() shifted the dictionary backwards.  It was good to learn also that translate() is performed on a string and uses the dictionary that maketrans() generates.  Cool learnings. 

"""
alphabet_string = string.ascii_lowercase
alphabet_string_shift2 = alphabet_string[-2:] + alphabet_string[0:-2]
alpha_dict = dict(zip(alphabet_string_shift2,alphabet_string))
block_of_text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

def rotate_chr(c):
    rot_by = 2
    c = c.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if c not in alphabet:
        return c
    rotated_pos = ord(c) + rot_by
    if rotated_pos <= ord(alphabet[-1]):
        return chr(rotated_pos)
    return chr(rotated_pos - len(alphabet))

new_block = ""
#print("".join(map(rotate_chr, block_of_text)))


new_block = block_of_text.maketrans(alpha_dict)
print(block_of_text.translate(new_block))
print("http://www.pythonchallenge.com/pc/def/map.html".translate(new_block))
