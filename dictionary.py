d={110:"abc",101:"xyz",105:"pqr"}
print(d)
d={}
d["Laptop"]=40000
d["Mobile"]=15000
d["Earphone"]=1000
print(d)
print(d["Mobile"])

c={110:"abc",101:"xyz",105:"pqr"}
print(c.get(101))
print(c.get(125))
print(c.get(125,"NA"))
if 125 in c:
    print(c[125])
else:
    print("NA")

a={110:"abc",101:"xyz",105:"pqr"}
print(len(a))
print(a)
print(a.pop(105))
print(a)
d[108]="cde"
print(a.popitem())
print(a)