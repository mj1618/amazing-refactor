import subprocess as sp
from enum import EnumMeta, Enum, _EnumDict, auto
import time
import sys
import random

f = open("amazing.bas", "r")
lines = {}
class AutoName(Enum):
  def _generate_next_value_(name, start, count, last_values):
    return name
class Types(AutoName):
  STRING = auto()
  KEYWORD = auto()
  NUMBER = auto()
  UNKNOWN = auto()
  EXPRESSION = auto()
  FOR = auto()
  IF = auto()
  ARRAY = auto()
  CLS = auto()
  PRINT_AT=auto()
  PRINT=auto()
  VAR=auto()
  NEXT=auto()
  CONDITIONAL=auto()
  AND=auto()
  GOTO=auto()
  DIM=auto()
  ASSIGN=auto()
  RANDOM=auto()
  LPRINT=auto()
  INT=auto()
  ON = auto()
  END=auto()
  INPUT = auto()
  EQUATION=auto()
  OPERATOR = auto()

def do_cls():
  sp.call('clear',shell=True)

fors = {}
vars = {}
arrs = {}
curr_col = 0
stmts = []

def pull_number(line):
  for i in range(len(line)):
    if not line[i].isdigit():
      return ((Types.NUMBER, int(line[:i])), line[i:].strip())
  return ((Types.NUMBER, int(line)), "")

def pull_string(line):
  line = line[1:]
  s = ""
  i = 0
  for i in range(len(line)):
    if line[i] == "\"":
      return ((Types.STRING, line[:i]), line[i+1:].strip())

def pull_var(line):
  v = ""
  for i in range(len(line)):
    if line[i] == " ":
      return ((Types.VAR, v), line[i:].strip())
    if line[i] == ":":
      raise Exception("error pulling var: "+line)
    if line[i] == "=":
      return ((Types.VAR, v), line[i:].strip())
    if line[i] == "(":
      line = line[i+1:]
      j = line.index(")")
      ls = line[:j].split(",")
      (left, _) = pull_expression(ls[0])
      (right, _) = pull_expression(ls[1])
      return ((Types.ARRAY, v, left, right), line[j+1:].strip())
    v += line[i]
  raise Exception("error pulling var: "+line)

def to_var_or_number(s):
  if s[0].isdigit():
    return (Types.NUMBER, int(s))
  else:
    return (Types.VAR, s)

def pull_lprint(line):
  line = line[len("LPRINT "):]
  (s, line) = pull_string(line)
  carriage = False
  if len(line)>0 and line[0] == ";":
    line = line[1:]
    carriage = True
  return ((Types.LPRINT, s, carriage), line)

def pull_on(line):
  line = line[len("ON "):]
  (v, line) = pull_var(line)
  line = line[len("GOTO "):]
  ns = line.split(",")
  ns = [int(n) for n in ns]
  return ((Types.ON, v, ns), "")

def pull_expression_token(line):
  line = line.strip()
  ops = ["+", "*", "/", "-"]
  v = ""
  if line[0] in ops:
    return ((Types.OPERATOR, line[0]), line[1:])
  i = None
  if line[:2]=="TO":
    return ("", line.strip())
  if line[:4]=="RND(":
    line = line[4:]
    j = line.rindex(")")
    (ex, _) = pull_expression(line[:j])
    return ((Types.RANDOM, ex), line[j+1:])
  if line[:4]=="INT(":
    line = line[4:]
    j = line.rindex(")")
    (ex, _) = pull_expression(line[:j])
    return ((Types.INT, ex), line[j+1:])
  for i in range(len(line)):
    if line[i] in ops:
      return (to_var_or_number(v), line[i:].strip())
    if line[i] == " ":
      return (to_var_or_number(v), line[i:].strip())
    if line[i] == ":":
      return (to_var_or_number(v), line[i:].strip())
    if line[i] == "=":
      return (to_var_or_number(v), line[i:].strip())
    if line[i] == "(":
      line = line[i+1:]
      j = line.index(")")
      ls = line[:j].split(",")
      (left, _) = pull_expression(ls[0])
      (right, _) = pull_expression(ls[1])
      return ((Types.ARRAY, v, left, right), line[j+1:].strip())
    v += line[i]

  return (to_var_or_number(v), line[i+1:].strip())

def pull_input(line):
  line = line[len("INPUT"):]
  (s, line) = pull_string(line)
  return ((Types.INPUT, s, (Types.VAR, "H"), (Types.VAR, "V")), "")

def pull_if(line):
  line = line[len("IF "):]
  i = line.index("THEN")
  cond = get_conditional(line[:i-1])
  line = line[i + len("THEN "):]
  (n, line) = pull_number(line)
  return ((Types.IF, cond, n), line)

def pull_for(line):
  line = line[len("FOR "):]
  (left, line) = pull_var(line)
  line = line[1:].strip()
  (right, line) = pull_expression(line)
  line = line[2:].strip()
  (limit, line) = pull_expression(line)
  return ((Types.FOR, left, right, limit), line)

def do_exp(e):
  operators = ["+","-","*","/"]
  out = []
  ops = []
  ts = []
  if len(e)>0 and e[0] == Types.EXPRESSION:
    ts = e[1]
  elif len(e)>0 and e[0] != Types.EXPRESSION:
    ts = [e]
  else:
    ts = e
  ts = ts[:]
  while len(ts)>0:
    t = ts.pop(0)
    if t[0]==Types.NUMBER:
      out.append(t[1])
    if t[0]==Types.RANDOM:
      n = do_exp(t[1])
      x = None
      if n == 0:
        x = random.random()
      else:
        x = random.randint(1, n)
      out.append(x)
    if t[0]==Types.VAR:
      out.append(vars[t[1]])
    if t[0]==Types.ARRAY:
      out.append(arrs[t[1]][do_exp(t[2])][do_exp(t[3])])
    if t[0] == Types.OPERATOR:
      top = None if len(ops)==0 else ops[0]
      while top is not None and operators.index(top) > operators.index(t[1]):
        out.append(ops.pop())
        top = None if len(ops)==0 else ops[0]
      ops.append(t[1])
    if t[0] == Types.EXPRESSION:
      out.append(do_exp(t))
  while len(ops)>0:
    out.append(ops.pop())
  st = []
  for x in out:
    if x in operators:
      (a, b) = (st.pop(), st.pop())
      if x=="+":
        st.append(a+b)
      if x=="-":
        st.append(a-b)
      if x=="*":
        st.append(a*b)
      if x=="/":
        st.append(a/b)
    else:
      if isinstance(x, int):
        st.append(x)
      elif isinstance(x, float):
        st.append(x)
      elif x[0]==Types.VAR:
        st.append(vars[x[1]])
      elif x[0]==Types.NUMBER:
        st.append(vars[x[1]])
      else:
        raise Exception("unknown literal: "+x)
  return int(st[0]) if len(st)>0 else 0

def pull_expression(line):
  ts = []
  while len(line)>0 and line[0] not in [":", " "]:
    (t, line) = pull_expression_token(line)
    if t=="TO":
      break
    if len(t)==0:
      break
    ts.append(t)
  return ((Types.EXPRESSION, ts), line)

def pull_cls(line):
  line = line[len("CLS"):]
  if line[0] == ":":
    line = line[1:]
  return ((Types.CLS,), line.strip())

def pull_goto(line):
  line = line[len("GOTO "):]
  (n, line) = pull_expression(line)
  return ((Types.GOTO, n), line)

def pull_dim(line):
  line = line[len("DIM "):]
  vs = []
  (v, line) = pull_var(line)
  vs.append(v)
  line = line[2:]
  (v, line) = pull_var(line)
  vs.append(v)
  return ((Types.DIM, vs), line)

def get_single_conditional(line):
  special = ["<", ">", "="]
  i = None
  for s in special:
    if s in line:
      i = line.index(s)
      break

  (left, _) = pull_expression(line[:i].strip())
  if line[i+1] in special:
    op = line[i:i+2]
    line = line[i+2:]
  else:
    op = line[i]
    line = line[i+1:]
  (right, _) = pull_expression(line)
  return (Types.CONDITIONAL, left, op, right)

def get_conditional(line):
  if " AND " in line:
    ls = line.split(" AND ")
    return (Types.AND, get_single_conditional(ls[0]), get_single_conditional(ls[1]))
  else:
    return get_single_conditional(line)

def pull_print(line):
  line = line[len("PRINT "):]
  if line[0] == "@":
    line = line[len("@ "):]
    (n, line) = pull_number(line)
    line = line[1:]
    (s, line) = pull_string(line)
    carriage = False
    if len(line)>0 and line[0] == ";":
      line = line[1:]
      carriage = True
    return ((Types.PRINT_AT, n[1], s[1], carriage), line.strip())
  else:
    (s, line) = pull_string(line)
    carriage = False
    if len(line)>0 and line[0] == ";":
      line = line[1:]
      carriage = True
    return ((Types.PRINT, s[1], carriage), line.strip())

def pull_line(line):
  tokens = ["END", "ON", "DIM", "INPUT", "CLS", "PRINT", "IF", "FOR", "LPRINT", "NEXT", "GOTO", "=", "(", ")", "@", ","]
  for i in range(len(line)):
    if line[:i+1] in tokens:
      word = line[:i+1]
      if word == "FOR":
        return pull_for(line)
      if word == "CLS":
        return pull_cls(line)
      if word == "PRINT":
        return pull_print(line)
      if word == "NEXT":
        line = line[len("NEXT"):]
        j = 0
        for j in range(len(line)):
          if line[j]==":":
            break
        return ((Types.NEXT,), line[j+1:].strip())
      if word == "INPUT":
        return pull_input(line)
      if word == "IF":
        return pull_if(line)
      if word == "GOTO":
        return pull_goto(line)
      if word=="DIM":
        return pull_dim(line)
      if word =="LPRINT":
        return pull_lprint(line)
      if word=="ON":
        return pull_on(line)
      if word=="END":
        return (Types.END, "")
  # must be assignment
  (v, line) = pull_var(line)
  if line[0] != "=":
    raise Exception("Expected = but got ", line)
  line = line[1:]
  (a, line) = pull_expression(line)
  return ((Types.ASSIGN, v, a), line)

def pull_lines(line):
  ls = []
  while len(line)>0:
    if line[0]==":":
      line = line[1:].strip()
    (l, line) = pull_line(line)
    ls.append(l)
  return ls

def parse():
  i = 10
  for line in f:
    print("Parsing line ", i)
    line = line.strip()
    (token, line) = pull_number(line)
    lines[int(token[1])] = pull_lines(line)
    i+=10
  for j in range(10, 1381, 10):
    for l in lines[j]:
      stmts.append((j, l))

def find_for(st, n):
  i = None
  for i in range(len(stmts)):
    if stmts[i][1] == st and stmts[i][0] == n:
      i -= 1
      break

  count = 1
  while i>=0 and count>0:
    if stmts[i][1][0]==Types.NEXT:
      count += 1
    if stmts[i][1][0]==Types.FOR:
      count -= 1
    if count == 0:
      break
    i -= 1

  return stmts[i]

def do_cond(c):
  if c[0] == Types.AND:
    return do_cond(c[1]) and do_cond(c[2])
  elif c[0] == Types.CONDITIONAL:
    first = do_exp(c[1])
    second = do_exp(c[3])
    op = c[2]
    if op == "<>":
      return first != second
    elif op=="=":
      return first == second
    elif op=="<":
      return first < second
    elif op==">":
      return first > second
    else:
      raise Exception("unknown op: "+op)
  else:
    raise Exception('unknown cond: ' + c)

def execute(st, n):
  if st[0] == Types.CLS:
    do_cls()
  elif st[0] == Types.PRINT_AT:
    s = st[2]
    for i in range(st[1]):
      s = " "+s
    print(s, end='')
    if st[3]:
      print("")
  elif st[0] == Types.PRINT:
    s = st[1]
    print(s, end='')
    if st[2]:
      print("")
  elif st[0] == Types.INPUT:
    s = input(st[1][1]+" ").split()
    vars[st[2][1]] = int(s[0])
    vars[st[3][1]] = int(s[1])
  elif st[0] == Types.LPRINT:
    # print(st)
    s = st[1][1]
    print(s, end='')
    if not st[2]:
      print("")
  elif st[0] == Types.FOR:
    sys.stdout.flush()
    if n in fors:
      vars[st[1][1]] += 1
      time.sleep(0.0005)
    else:
      fors[n] = True
      vars[st[1][1]] = do_exp(st[2][1])
  elif st[0] == Types.NEXT:
    (nf, f) = find_for(st, n)
    if vars[f[1][1]] + 1 > do_exp(f[3]):
      del vars[f[1][1]]
      del fors[nf]
      return (False, n)
    else:
      return (True, nf)
  elif st[0] == Types.IF:
    res = do_cond(st[1])
    return (res, st[2][1])
  elif st[0] == Types.GOTO:
    return do_exp(st[1])
  elif st[0] == Types.DIM:
    for x in st[1]:
      a = do_exp(x[2])
      b = do_exp(x[3])
      arrs[x[1]] = []
      for i in range(a+1):
        arrs[x[1]].append([])
        for j in range(b+1):
          arrs[x[1]][i].append(0)
  elif st[0] == Types.ASSIGN:
    if st[1][0] == Types.ARRAY:
      arrs[st[1][1]][do_exp(st[1][2])][do_exp(st[1][3])] = do_exp(st[2])
    else:
      vars[st[1][1]] = do_exp(st[2])
  elif st[0] == Types.ON:
    return st[2][do_exp(st[1])-1]
  else:
    print("unhandled: ", st)
    exit()

def run():
  j = 10
  while True:
    ls = lines[j]
    goto = False
    for l in ls:
      if l == Types.END:
        exit()
      if l[0] == Types.GOTO or l[0] == Types.ON:
        j = execute(l, j)
        goto = True
        break
      elif l[0] == Types.NEXT or l[0] == Types.IF:
        (do_jump, to) = execute(l, j)
        if do_jump:
          j = to
          goto = True
          break
      else:
        execute(l, j)
    if not goto:
      j += 10

parse()
run()
