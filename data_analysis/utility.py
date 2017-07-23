def myround(x, prec=2, base=0.5):
    return round(base * round(float(x)/base),prec)

def parse_line(s):
    split_array = s.split(",")
    x, y, z = split_array[0], split_array[1], split_array[2]
    return float(x), float(y), float(z)
