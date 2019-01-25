import random
import subprocess as sp
from time import sleep
import sys
sys.setrecursionlimit(150000)
w = v = s = r = c = q = h = z = None

def do_cls():
  sp.call('clear',shell=True)

def call1200():
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

def call1020():
  global w, v, s, r, c, q, h, H, V
  w[r+1][s] = c
  c+=1
  if v[r][s]==0:
    v[r][s]=2
  else:
    v[r][s]=3

  r+=1
  if c==H*V+1:
    call1200()
  else:
    call600()

def call1090():
  global w, v, s, r, c, q, h, H, V
  if q==1:
    z=1
    if v[r][s]==0:
      v[r][s]=1
      q=0
      r=1
      s=1
      if w[r][s]==0:
        call210()
      else:
        call270()
    else:
      v[r][s]=3
      q=0
      call210()
  else:
    w[r][s+1]=c
    c+=1
    if v[r][s]==0:
      v[r][s]=1
    else:
      v[r][s]=3
    s = s+1
    if c==V*H+1:
      call1200()
    else:
      call270()

def call980():
  global w, v, s, r, c, q, h, H, V
  w[r][s-1]=c
  c+=1
  v[r][s-1]=1
  s-=1
  if c==H*V+1:
    call1200()
  else:
    q=0
    call270()

def call600():
  global w, v, s, r, c, q, h, H, V
  if s-1==0 or w[r][s-1]!=0:
    if r==H or w[r+1][s]!=0:
      if s!=V:
        if w[r][s+1]!=0:
          call210()
        else:
          call1090()
      elif z==1:
        call210()
      else:
        q=1
        call1090()
    elif s!=V:
      if w[r][s+1]!=0:
        call1020()
      else:
        x=random.randint(1, 2)
        if x==1:
          call1020()
        elif x==2:
          call1090()
    elif z==1:
      call1020()
    else:
      q=1
      c+=1
      v[r][s-1]=1
      s-=1
      if c==H*V+1:
        call1200()
      else:
        q=0
        call270()
  elif r==H or w[r+1][s]!=0:
    if s!=V:
      if w[r][s+1]!=0:
        call980()
      else:
        x=random.randint(1, 2)
        if x==1:
          call980()
        elif x==2:
          call1090()
    elif z==1:
      w[r][s-1]=c
      c+=1
      v[r][s-1]=1
      s-=1
      if c==H*V+1:
        call1200()
      else:
        q=0
        call270()
    else:
      q=1
      x=random.randint(1,2)
      if x==1:
        w[r][s-1]=c
        c+=1
        v[r][s-1]=1
        s-=1
        if c==H*V+1:
          call1200()
        else:
          q=0
          call270()
      elif x==2:
        call1090()
  elif s!=V:
    if w[r][s+1]!=0:
      x = random.randint(1, 2)
      if x==1:
        w[r][s-1]=c
        c+=1
        v[r][s-1]=1
        s-=1
        if c==H*V+1:
          call1200()
        else:
          q=0
          call270()
      elif x==2:
        call1020()
    else:
      x=random.randint(1, 3)
      if x==1:
        w[r][s-1]=c
        c+=1
        v[r][s-1]=1
        s-=1
        if c==H*V+1:
          call1200()
        else:
          q=0
          call270()
      elif x==2:
        call1020()
      else:
        call1090()

  elif z==1:
    x = random.randint(1, 2)
    if x==1:
      w[r][s-1]=c
      c+=1
      v[r][s-1]=1
      s-=1
      if c==H*V+1:
        call1200()
      else:
        q=0
        call270()
    elif x==2:
      call1020()
  else:
    q=1
    x=random.randint(1, 3)
    if x==1:
      w[r][s-1]=c
      c+=1
      v[r][s-1]=1
      s-=1
      if c==H*V+1:
        call1200()
      else:
        q=0
        call270()
    elif x==2:
      call1020()
    else:
      call1090()


def call270():
  global w, v, s, r, c, q, h, H, V
  if r-1==0:
    call600()
  elif w[r-1][s]!=0:
    call600()
  elif s-1==0 or w[r][s-1]!=0:
    if r==H or w[r+1][s]!=0:
      if s!=V:
        if w[r][s+1]!=0:
          call940()
        else:
          x=int(random.random()*2+1)
          if x==1:
            call940()
          elif x==2:
            call1090()
      elif z==1:
        call940()
      else:
        q=1
        x=int(random.random()*2+1)
        if x==1:
          call940()
        elif x==2:
          call1090()
    elif s!=V:
      if w[r][s+1]!=0:
        x = random.randint(1,2)
        if x==1:
          call940()
        elif x==2:
          call1020()
      else:
        x = random.randint(1, 3)
        if x==1:
          call940()
        elif x==2:
          call1020()
        elif x==3:
          call1090()
    elif z==1:
      x = random.randint(1,2)
      if x==1:
        call940()
      elif x==2:
        call1020()
    else:
      q=1
      x = random.randint(1, 3)
      if x==1:
        call940()
      elif x==2:
        call1020()
      elif x==3:
        call1090()

  elif r==H or w[r+1][s]!=0:
    if s!=V:
      if w[r][s+1]!=0:
        x = random.randint(1,2)
        if x==1:
          call940()
        elif x==2:
          call980()
      else:
        x=random.randint(1, 3)
        if x==1:
          call940()
        elif x==2:
          call980()
        elif x==3:
          call1090()
    elif z==1:
      x = random.randint(1,2)
      if x==1:
        call940()
      elif x==2:
        w[r][s-1]=c
        c+=1
        v[r][s-1]=1
        s-=1
        if c==H*V+1:
          call1200()
        else:
          q=0
          call270()
    else:
      q=1
      x=random.randint(1, 3)
      if x==1:
        call940()
      elif x==2:
        call980()
      elif x==3:
        call1090()
  else:
    x = random.randint(1, 3)
    if x==1:
      call940()
    elif x==2:
      w[r][s-1]=c
      c+=1
      v[r][s-1]=1
      s-=1
      if c==H*V+1:
        call1200()
      else:
        q=0
        call270()
    elif x==3:
      call1020()

def call210():
  global w, v, s, r, c, q, h, H, V
  if r!=H:
    r+=1
    if w[r][s]==0:
      call210()
    else:
      call270()
  elif s!=V:
    r = 1
    s+=1
  else:
    r=1
    s=1
  if w[r][s]==0:
    call210()
  else:
    call270()

def call940():
  global w, v, s, r, c, q, h, H, V
  w[r-1][s]=c
  c=c+1
  v[r-1][s]=2
  r-=1

  if c==H*V+1:
    call1200()
  else:
    q=0
    call270()

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
  call270()

main()


