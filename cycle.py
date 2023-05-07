from insect import Insect

def enemy_spawn():
  
  insect = Insect('ant')
  print(f"A {insect.name} has appeared!")

  Insect.self_describe(insect)
  return insect
  
  
  