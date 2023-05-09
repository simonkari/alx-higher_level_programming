def uppercase(s):
    uppercase_s = ""
    for c in s:
        uppercase_s += chr(ord(c) - 32) if 'a' <= c <= 'z' else c
    print("{}\n".format(uppercase_s))
   