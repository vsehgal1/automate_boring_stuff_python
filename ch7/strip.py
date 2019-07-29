# strip.py
# automatetheboringstuff.com Chapter 7
# Vikram Sehgal

import re

def strip(strn, chars):

    if chars == '':
        reg_space = re.compile(r'^(\s*)(\S*)(\s*)$') #regex for whitespace
        new_strn = reg_space.search(strn).group(2)
        return new_strn
    else:
        reg = re.compile(r'(^[%s]+)(.+?)([%s]+)$' % (chars,chars))  #regex for character list
        new_strn = reg.search(strn).group(2)
        return new_strn


if __name__ == '__main__':
    strn = input('Enter string: ')
    chars = input('Enter char to strip (Optional): ')
    print(strip(strn, chars))


