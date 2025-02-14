import inspect

a, pl = a[pl] = {}, (84, 103, 103, 112, 28, 100, 109, 25, 102, 102, 106, 21, 87, 95, 87, 82, 94, 15, 81, 92, 80, 80, 24)
a[pl] = type("m̶̃", (object,), {"n": ...,
                                 "p": ...,
                                 "pl": 0,
                                 "".join([chr(x+i) for i, x in enumerate([95, 94, 103, 107, 101, 111, 89, 88])]):
                                                                  lambda x, y, z, k:
                                 setattr(x, "n", y) or setattr(x, "p", z) or setattr(x, "pl", k)})

f, c = None, None
for i in range(len(pl)):
    cu = a[pl](y=None, z=..., k=pl[i])
    cu.bark = lambda x, d: print(chr(x.pl+d), end="")
    f = cu if not f else f
    if c:
        c.n = cu
        cu.p = c
    c = cu

def OUT(LOL):
    LOL.bark(LOL, len(inspect.stack()) - 2)
    if LOL.n:
         OUT(LOL.n)
OUT(f)
