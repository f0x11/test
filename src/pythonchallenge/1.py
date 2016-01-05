from string import maketrans

a = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. " \
    "bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. " \
    "lmu ynnjw ml rfc spj."\
    .replace("a", "c")\
    .replace("y", "a")\
    .replace("w", "y")\
    .replace("u", "w")\
    .replace("s", "u")\
    .replace("q", "s")\
    .replace("o", "q")\
    .replace("m", "o")\
    .replace("k", "m")\
    .replace("i", "k")\
    .replace("g", "i")\
    .replace("e", "g")\
    .replace("c", "e")\
    .replace("r", "t")\
    .replace("p", "r")\
    .replace("n", "p")\
    .replace("l", "n")\
    .replace("j", "l")\
    .replace("f", "h")\
    .replace("d", "f")\
    .replace("b", "d")\
    .replace("z", "b")\
    .replace("v", "s")\

inctab = "abcdefghijklmnopqrstuvwxyz"
outtab = "cdefghijklmnopqrstuvwxyzab"
trantab = maketrans(inctab, outtab)

str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. " \
    "bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. " \
    "lmu ynnjw ml rfc spj."
print str.translate(trantab)

print 'http://www.pythonchallenge.com/pc/def/map.html'.translate(trantab)
