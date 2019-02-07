#!/usr/bin/python

class Animal():
 def __init__(self, name, weight, height):
  self.name = name
  self.weight = weight
  self.height = height
 def who(self):
  return self.name
 def wxh(self):
  return self.weight * self.height
