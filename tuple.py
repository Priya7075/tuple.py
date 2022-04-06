# y="a"
# print(y,type(y))#'tuple'
# h=(3,6.8,'vI',None)
# print(type(h))#tuple
# print(h[0])#3
# h[0]=5#TypeError:tuple object does not support item assignment
# c=print('hi')#hi
# d=print(c)#None
# print(c,type(c))#NoneType
# x=(1)
# print(x,type(x))#int
# pr=('vamsi','indu','kaveri','chinna','nani')
# pr[1]='sindhu'#TypeError:'tuple' object does not support item assignment
# n="vamsi",   "indu"
# print(n,type(n))#tuple
# print(n[2])#indexError:tuple index outof range
# v=(1,4.2,'hey',[4,5],('v','I'),None,True)
# print(v,type(v))#(1,4.2,'hey',[4,5],('v','I'),None,True) tuple
# v=(1,4.2,'hey',[0,7],('v','I'))
# v[0]=21#tuple
# v=(1,4.2,'hey',[2,7],('v','I'))
# print(v.count(4.2))#1
# print(v.index([26,7]))#valueError:tuple.index x is not in tuple
# print(v.index([2,7]))#3