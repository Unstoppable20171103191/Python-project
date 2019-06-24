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


    latitude = [0,0,0]
    for i in xrange(count):
      byte = f.read(4)
      numerator = byte.encode('hex')

      byte = f.read(4)
      denominator = byte.encode('hex')

      latitude[i] = float(int(numerator, 16)) / int(denominator, 16)


    print( 'Latitude:\t%.2f %.2f\' %.2f\"' % (latitude[0], latitude[1], latitude[2]))
    f.seek(old_pos)  


