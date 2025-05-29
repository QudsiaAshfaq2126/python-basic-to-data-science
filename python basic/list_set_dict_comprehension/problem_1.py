integer=[0,1,2,3,4]
binary=["0","1","10","11","100"]
q=zip(integer,binary)
binary_dict = {}
for integer, binary in q:
    binary_dict[integer] = binary
    print(binary_dict)
interger=[1,-1,2,3,5,0,-7]
additive_inverse=[-1*i for i in interger]
print(additive_inverse)
interger=[1,-1,2,-2,3,-3]
s_q={i*i for i in interger}
print(s_q)