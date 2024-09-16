s1={10,20,30}
print(s1)
s2=set([20,30,40])
print(s2)
s3={}
print(type(s3))

s4=set()
print(type(s4))
print(s4)

s5={10,20}
s5.add(30)
print(s5)
s5.add(30)
print(s5)
s5.update([40,50])
print(s5)
s5.update({60,70},[80,80])
print(s5)

s={10,30,20,40}
s.discard(30)
print(s)
s.remove(20)
print(s)
s.clear()
print(s)
s.add(50)
print(s)

s6={2,4,6,8}
s7={3,6,9}
print(s6|s7)
print(s6&s7)
print(s6-s7)
print(s6^s7)

s8={2,4,6,8}
s9={4,8}
print(s8.isdisjoint(s9))
print((s8)<=s9)
print(s8<s9)
print(s8>=s9)
print(s8>s9)