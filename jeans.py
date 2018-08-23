#!/usr/bin/env python3
#This program is demonstration of Jeans class that has init constructor
# and two member functions put_on and take_off.

class Jeans():
  def __init__(self, color, waist, height ):
      self.color = color
      self.waist = waist
      self.height = height
      self.wearing = False

  def put_on(self):
      self.wearing = True
      print(f"putting on {self.waist}x{self.height} with {self.color}")

  def take_off(self):
      self.wearing = False
      print(f"taking off {self.waist}x{self.height} with {self.color}")

if __name__ == "__main__":
    myjeans = Jeans('blue', '32', '34')
    myjeans.put_on()
    myjeans.take_off()
    myjeans = Jeans('black', '34', '36')
    myjeans.put_on()
    myjeans.take_off()
