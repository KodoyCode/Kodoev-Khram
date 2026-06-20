marks=[4,5,3,4,5]
t1=20
t2=24
print(t1)
print(t2)
t_july=[20,24,30,43,12,23]
a=[True,43,'hello',5.4,[4,5,6]]
b=[]
print(type(b))
print(len([1,2,3]))
print(len(b))
print(len(a))
c=[12,23]+[1,2,3]
print(c)
aa=a+[4]
print(aa)
aaa=['hi']+a
print(aaa)
z=[0]*5
print(z)
t=[1,2,3]*4
print(t)
#[12,3,4] + 4 is unacceptable!
br=[12,3,4]+[4]
print(5.4 in a)
print(False in a)
print([4,5,6] in a) 
print([4,5] in a) 
w=[43,54,65,3,4,65,-43,32]
print(max(w))
print(min(w))
print(sum(w))
print(max([1,2,3,4]))
print(min([1,2,3,4]))
print(sum([1,2,3,4]))
print(sorted(w))
print(sorted(w,reverse=True))
# print(max([1,2,3,'wda'])), print(sum([1,2,3,'wda'])), print(min([1,2,3,'wda'])) is unacceptable!
print([100,54]>[34,543,654,43])
print([100,54]<[34,543,654,43])
print([1,2,3]==[1,2,3])
print([1,2,3]>[1,2,3])
# [1,2,3]>[1,2,'asd'] is inacceptable!
print(max(marks))
print(min(marks))
print(sum(marks))
print(len(marks))
print(sum(marks)/len(marks))
