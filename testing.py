#!/usr/bin/env python3 

class User:
  def __init__(self):
    self.user_name = 'bryan'
    self.id = 10
    
  def get_name(self):
    return self.user_name 
  
  def get_id(self):
    return self.id
  
u = User()
print(u.get_name())
print(u.get_id())
