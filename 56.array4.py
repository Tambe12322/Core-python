from array import *
a1=array('i',[1,2,3])
as_bytes=a1.tobytes()
print(as_bytes)
a1.frombytes(as_bytes)
print("a1:",a1)