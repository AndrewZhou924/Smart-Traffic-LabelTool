import glob
count = 0
valid = len(glob.glob("./output/VALID/*"))
invalid = len(glob.glob("./output/INVALID/*"))
others = len(glob.glob("./output/OTHERS/*"))
count = valid + invalid + others

print("==> total count: ", count)
print("==> valid:{}  invalid:{}  others:{}".format(valid, invalid, others))
