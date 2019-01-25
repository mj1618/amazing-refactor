import random
import subprocess as sp
from time import sleep
import sys
sys.setrecursionlimit(150000)
w = v = s = r = c = q = h = z = None

def do_cls():
  sp.call('clear',shell=True)

def call760():
  x=random.randint(1,2)
  if x==1:
    call980()
  elif x==2:
    call1090()

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

def call480():
  global w, v, s, r, c, q, h, H, V
  if w[r][s+1]!=0:
    call510()
  else:
    call490()

def call490():
  global w, v, s, r, c, q, h, H, V
  x = random.randint(1, 3)
  if x==1:
    call940()
  elif x==2:
    call1020()
  elif x==3:
    call1090()

def call780():
  call980()

def call410():
  global w, v, s, r, c, q, h, H, V
  x = random.randint(1,2)
  if x==1:
    call940()
  elif x==2:
    call980()

def call250():
  global w, v, s, r, c, q, h, H, V
  r+=1
  if w[r][s]==0:
    call210()
  else:
    call270()

def call350():
  global w, v, s, r, c, q, h, H, V
  if s!=V:
    call380()
  elif z==1:
    call410()
  else:
    q=1
    call390()

def call240():
  global w, v, s, r, c, q, h, H, V
  r = 1
  s+=1
  call260()

def call260():
  if w[r][s]==0:
    call210()
  else:
    call270()

def call430():
  global w, v, s, r, c, q, h, z, H, V
  if r==H or w[r+1][s]!=0:
    call530()
  elif s!=V:
    call480()
  elif z==1:
    call510()
  else:
    q=1
    call490()

def call790():
  global w, v, s, r, c, q, h, z, H, V
  if r==H:
    call880()
  elif w[r+1][s]!=0:
    call880()
  elif s!=V:
    call840()
  elif z==1:
    call870()
  else:
    q=1
    call990()

def call990():
  global w, v, s, r, c, q, h, H, V
  c+=1
  v[r][s-1]=1
  s-=1
  if c==H*V+1:
    call1200()
  else:
    q=0
    call270()



def call840():
  global w, v, s, r, c, q, h, H, V
  if w[r][s+1]!=0:
    call870()
  else:
    x=random.randint(1, 2)
    if x==1:
      call1020()
    elif x==2:
      call1090()

def call1020():
  global w, v, s, r, c, q, h, H, V
  w[r+1][s] = c
  c+=1
  if v[r][s]==0:
    call1050()
  else:
    v[r][s]=3
    call1060()

def call1050():
  global w, v, s, r, c, q, h, H, V
  v[r][s]=2
  call1060()

def call1060():
  global w, v, s, r, c, q, h, H, V
  r+=1
  if c==H*V+1:
    call1200()
  else:
    call600()

def call1150():
  global w, v, s, r, c, q, h, H, V
  z=1
  if v[r][s]==0:
    call1180()
  else:
    v[r][s]=3
    q=0
    call1190()

def call920():
  call1090()

def call1180():
  global w, v, s, r, c, q, h, H, V
  v[r][s]=1
  q=0
  r=1
  s=1
  call260()

def call570():
  global w, v, s, r, c, q, h, H, V
  x=int(random.random()*2+1)
  if x==1:
    call940()
  elif x==2:
    call1090()

def call1090():
  global w, v, s, r, c, q, h, H, V
  if q==1:
    call1150()
  else:
    w[r][s+1]=c
    c+=1
    if v[r][s]==0:
      # call1120
      v[r][s]=1
      call1130()
    else:
      v[r][s]=3
      call1130()

def call980():
  global w, v, s, r, c, q, h, H, V
  w[r][s-1]=c
  call990()

def call910():
  if w[r][s+1]!=0:
    call930()
  else:
    call1090()

def call1130():
  global w, v, s, r, c, q, h, H, V
  s = s+1
  if c==V*H+1:
    call1200()
  else:
    call270()

def call880():
  global w, v, s, r, c, q, h, H, V
  if s!=V:
    call910()
  elif z==1:
    call930()
  else:
    q=1
    call920()

def call720():
  global w, v, s, r, c, q, h, H, V
  if s!=V:
    call750()
  elif z==1:
    call780()
  else:
    q=1
    call760()

def call670():
  global w, v, s, r, c, q, h, H, V
  if w[r][s+1]!=0:
    call700()
  else:
    call680()

def call700():
  global w, v, s, r, c, q, h, H, V
  x = random.randint(1, 2)
  if x==1:
    call980()
  elif x==2:
    call1020()

def call680():
  global w, v, s, r, c, q, h, H, V
  x=random.randint(1, 3)
  if x==1:
    call980()
  elif x==2:
    call1020()
  else:
    call1090()

def call600():
  global w, v, s, r, c, q, h, H, V
  if s-1==0:
    call790()
  elif w[r][s-1]!=0:
    call790()
  elif r==H:
    call720()
  elif w[r+1][s]!=0:
    call720()
  elif s!=V:
    call670()
  elif z==1:
    call700()
  else:
    q=1
    call680()


def call270():
  global w, v, s, r, c, q, h, H, V
  if r-1==0:
    call600()
  elif w[r-1][s]!=0:
    call600()
  elif s-1==0:
    call430()
  elif w[r][s-1]!=0:
    call430()
  elif r==H:
    call350()
  elif w[r+1][s]!=0:
    call350()
  else:
    x = random.randint(1, 3)
    if x==1:
      call940()
    elif x==2:
      call980()
    elif x==3:
      call1020()

def call590():
  call940()

def call380():
  global w, v, s, r, c, q, h, H, V
  if w[r][s+1]!=0:
    call410()
  else:
    call390()

def call930():
  call1190()

def call750():
  global w, v, s, r, c, q, h, H, V
  if w[r][s+1]!=0:
    call780()
  else:
    x=random.randint(1, 2)
    if x==1:
      call980()
    elif x==2:
      call1090()

def call210():
  global w, v, s, r, c, q, h, H, V
  if r!=H:
    call250()
  elif s!=V:
    call240()
  else:
    r=1
    s=1
    call260()

def call1190():
  call210()

def call510():
  global w, v, s, r, c, q, h, H, V
  x = random.randint(1,2)
  if x==1:
    call940()
  elif x==2:
    call1020()

def call870():
  call1020()

def call390():
  global w, v, s, r, c, q, h, H, V
  x=random.randint(1, 3)
  if x==1:
    call940()
  elif x==2:
    call980()
  elif x==3:
    call1090()

def call560():
  global w, v, s, r, c, q, h, H, V
  if w[r][s+1]!=0:
    call590()
  else:
    call570()

def call530():
  global w, v, s, r, c, q, h, H, V
  if s!=V:
    call560()
  elif z==1:
    call590()
  else:
    q=1
    call570()

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


