##Rounds a float input to a base with specified precision
def myround(x, prec=2, base=0.5):
    return round(base * round(float(x)/base),prec)

def parse_line(s):
    split_array = s.split(",")
    x, y, z = split_array[0], split_array[1], split_array[2]
    return float(x), float(y), float(z)

#Calculates the area of intersection between two hemispheres
#d: distance between the center of two spheres
#R: Radius of sphere 1
#r: Radius of sphere 2
def inter_vol(d, R, r):
    term1 = pow((R+r-d),2)
    term2 = ((pow(d,2))+(2*d*r)-(3*(pow(r,2))) + (2 * d * R) + (6*r*R) - (3*(pow(R,2))))
    term3 = (12 * d)
    return (math.pi * term1 * term2)/(2*term3)
