print('Hello World!')

print('What is your name?')

myName = input()



print('It is good to meet you ' +  myName)



import turtle as t
t.speed(1)



a = 50
while 1:
    t.forward(a)
    t.left(360/3)
    a= a+10


      

      

import binascii

class ParseMethod(object):
  @staticmethod
  def parse_default(f, count, offset):
    pass

  @staticmethod
  def parse_latitude(f, count, offset):
    old_pos = f.tell()
    f.seek(12 + offset)
