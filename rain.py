from time import sleep
from random import randint
import fcntl, termios, struct

def render():
  print('\033[2J')
  for r in data:
    for c in r:
      v = states[c] if c < len(states) else states[-1]
      print(v,end='')
    print('')

def update():
  for ir in range(len(data)-1,-1,-1):
    for ic, c in enumerate(data[ir]):
      if randint(1,1000) > 999:
        data[ir][ic] += randint(1,3)
      if c > 2:
        data[ir][ic] -= c
        if ir < len(data) -1:
          data[ir+1][ic] += c

def terminal_size():
    th, tw, hp, wp = struct.unpack('HHHH',
        fcntl.ioctl(0, termios.TIOCGWINSZ,
        struct.pack('HHHH', 0, 0, 0, 0)))
    return tw, th

width,height = terminal_size()

data = []
states = list(' .,:;|oO')

for _ in range(height):
  row = []
  for __ in range(width):
    row.append(0)
  data.append(row)

while True:
  render()
  update()
  sleep(0.075)

