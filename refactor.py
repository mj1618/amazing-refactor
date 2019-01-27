import random
import subprocess as sp
from time import sleep
import sys
sys.setrecursionlimit(150000)
w = v = s = r = c = q = h = z = None

def try_move_down():
  global w, v, s, r, c, q, h, H, V
  if q==1:
    z=1
    q=0
    if v[r][s]==0:
      v[r][s]=1
      r=1
      s=1
      if w[r][s]==0:
        find_next_cell()
      else:
        return
    else:
      v[r][s]=3
      find_next_cell()
  else:
    move_down() 

def compute_next():
  global w, v, s, r, c, q, h, H, V
  if is_wall_up(w, r, s):
    if is_wall_right(w, r, s, V):
      if not is_bottom_most(s, V):
        if is_wall_down(w, r, s):
          find_next_cell()
        else:
          try_move_down()
      elif z==1:
        find_next_cell()
      else:
        q=1
        try_move_down()
    elif not is_bottom_most(s, V):
      if is_wall_down(w, r, s):
        move_right()
      else:
        call_random([lambda: move_right(), lambda: try_move_down()])
    elif z==1:
      move_right()
    else:
      q=1
      move_up()
  elif is_wall_right(w, r, s, V):
    if not is_bottom_most(s, V):
      if is_wall_down(w, r, s):
        move_up()
      else:
        call_random([lambda: move_up(), lambda: try_move_down()])
    elif z==1:
      move_up()
    else:
      q=1
      call_random([lambda: move_up(), lambda: try_move_down()])
  elif not is_bottom_most(s, V):
    if is_wall_down(w, r, s):
      call_random([lambda: move_up(), lambda: move_right()])
    else:
      call_random([lambda: move_up(), lambda: move_right(), lambda: try_move_down()])

  elif find_next_cell():
    call_random([lambda: move_up(), lambda: move_right()])
  else:
    q=1
    call_random([lambda: move_up(), lambda: move_right(), lambda: try_move_down()])

def start_loop( ):
  global w, v, s, r, c, q, h, H, V
  while True:

    moves = [1, 0, 0, 0] # left, right, up, down

    if not is_wall_left(w, r, s) and not is_wall_right(w, r, s, V):
      moves[1] = 1

    if not is_wall_left(w, r, s) and not is_wall_up(w, r, s):
      moves[2] = 1


    if not is_wall_left(w, r, s) and is_wall_up(w, r, s) and not is_bottom_most(s, V) and not is_wall_down(w, r, s):
      moves[3] = 1
    if not is_wall_left(w, r, s) and is_wall_up(w, r, s) and is_bottom_most(s, V) and not find_next_cell():
      moves[3] = 1

    if is_wall_left(w, r, s):
      compute_next()
    elif is_wall_up(w, r, s):
      if is_wall_right(w, r, s, V):
        if not is_bottom_most(s, V):
          if is_wall_down(w, r, s):
            move_left()
          else:
            call_random([lambda: move_left(), lambda: try_move_down()])
        elif find_next_cell():
          move_left()
        else:
          q=1
          call_random([lambda: move_left(), lambda: try_move_down()])
      elif not is_bottom_most(s, V):
        if is_wall_down(w, r, s):
          call_random([lambda: move_left(), lambda: move_right()])
        else:
          call_random([lambda: move_left(), lambda: move_right(), lambda: try_move_down()])
      elif find_next_cell():
        call_random([lambda: move_left(), lambda: move_right()])
      else:
        q=1
        call_random([lambda: move_left(), lambda: move_right(), lambda: try_move_down()])

    elif is_wall_right(w, r, s, V):
      if not is_bottom_most(s, V):
        if is_wall_down(w, r, s):
          call_random([lambda: move_left(), lambda: move_up()])
        else:
          call_random([lambda: move_left(), lambda: move_up(), lambda: try_move_down()])
      elif z==1:
        call_random([lambda: move_left(), lambda: move_up()])
      else:
        q=1
        call_random([lambda: move_left(), lambda: move_up(), lambda: try_move_down()])
    else:
      call_random([lambda: move_left(), lambda: move_up(), lambda: move_right()])

def is_wall_left(w, r, s):
  return r-1==0 or w[r-1][s]!=0

def move_down():
  global w, v, s, r, c, q, h, H, V
  w[r][s+1]=c
  c+=1
  if v[r][s]==0:
    v[r][s]=1
  else:
    v[r][s]=3
  s+=1
  draw_if_finished(c, H, V)

def is_wall_up(w, r, s):
  return s-1==0 or w[r][s-1]!=0

def is_wall_right(w, r, s, V):
  return r==H or w[r+1][s]!=0

def is_wall_down(w, r, s):
  return w[r][s+1]!=0


def call_random(ls):
  x = random.randint(1, len(ls))
  return ls[x-1]()

def draw_if_finished(c, H, V):
  global q
  if is_finished(c, H, V):
    draw_maze()
  else:
    q=0

def is_right_most(r, H):
  return r==H

def is_bottom_most(s, V):
  return s==V

def find_next_cell():
  global w, v, s, r, c, q, h, H, V
  while True:
    if not is_right_most(r, H):
      r+=1
    elif not is_bottom_most(s, V): # is right_most
      r = 1
      s+=1
    else: # is right_most and is bottom_most
      r=1
      s=1

    if w[r][s]!=0:
      return

def move_up():
  global w, v, s, r, c, q, h, H, V
  w[r][s-1]=c
  c+=1
  v[r][s-1]=1
  s-=1
  draw_if_finished(c, H, V)

def move_left():
  global w, v, s, r, c, q, h, H, V
  w[r-1][s]=c
  c+=1
  v[r-1][s]=2
  r-=1
  draw_if_finished(c, H, V)

def do_cls():
  sp.call('clear',shell=True)

def draw_maze():
  global w, v, s, r, c, q, h, H, V
  for j in range(1, V+1):
    print("I", end='')
    for i in range(1, H+1):
      if v[i][j] < 2:
        print("  I", end='')
      else:
        print("   ", end='')
    print(" ")
    for i in range(1, H+1):
      if v[i][j]==0 or v[i][j]==2:
        print(":--", end='')
      else:
        print(":  ", end='')
    print(":")
  exit()

def is_finished(c, H, V):
  return c==H*V+1

def move_right():
  global w, v, s, r, c, q, h, H, V
  w[r+1][s] = c
  c+=1
  if v[r][s]==0:
    v[r][s]=2
  else:
    v[r][s]=3

  r+=1
  if is_finished(c, H, V):
    draw_maze()
  else:
    compute_next()

def main():
  global w, v, s, r, c, q, h, H, V
  do_cls()
  print("AMAZING")
  print("COPYRIGHT BY")
  print("CREATIVE COMPUTING  MORRISTOWN, NEW JERSEY")
  sleep(1)
  H=V=1
  while True:
    # (H, V) = (input("WHAT ARE YOUR WIDTH AND LENGTH")).split()
    (H,V)=(20,20)
    (H, V) = (int(H), int(V))
    if H!=1 and V!=1:
      break
    else:
      print("MEANINGLESS DIMENSIONS. TRY AGAIN")
      sleep(0.5)
  print("PRINTOUT IS IN PROGRESS, PLEASE BE PATIENT")
  w = [[0]*(H+1) for _ in range(V+1)]
  v = [[0]*(H+1) for _ in range(V+1)]

  q=z=0
  x = random.randint(1, H)
  for i in range(1, H+1):
    if i==x:
      print(":  ", end='')
    else:
      print(":--", end='')
  print(":")

  c=1
  w[x][1] = c
  c += 1
  r = x
  s=1
  start_loop()

main()


