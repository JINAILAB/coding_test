def eq(a, b, c, d, e, f):
    denominator = a * e - b * d
    x = (c * e - b * f) / denominator
    y = (a * f - c * d) / denominator
    
    return str(int(x)), str(int(y))

a,b,c,d,e,f = map(int, input().split())
print(' '.join(eq(a,b,c,d,e,f)))
