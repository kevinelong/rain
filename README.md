# rain
https://www.youtube.com/watch?v=w4mc2xnIKBY
[![Rain Simulation](https://img.youtube.com/vi/w4mc2xnIKBY/0.jpg)](https://www.youtube.com/watch?v=w4mc2xnIKBY)

This follows a basic game loop.

1. Display 
2. Get Input (only time marching on, as this is a simulation not an interactive game)
3. Update Data based on Input
4. goto 1.

We have a list of rows; each of which has a list of columns (like a spreadsheet or graph paper or battle ship).

We display the integer values as one of eight letters " .,:;|oO" (space through capital O).

We cycle through all the rows and columns. For each we might add a drop of water by adding 1 to the existing value.

If there are enough drops in one position we move some or all of the drops to the position below (row index + 1).




The core of all this is the update() function.
Here it is with some comments:

def update():
  #LOOP THROUGH ALL ROWS
  for ir in range(len(data)-1,-1,-1):
    #LOOP THROUGH ALL COLUMNS
    for ic, c in enumerate(data[ir]):
      #ONCE IN A THOUSAND CHANCE WE WILL 
      if randint(1,1000) > 999:
        #ADD A SINGLE RAINDROP TO THIS ROW/COLUMN POSITION
        data[ir][ic] += randint(1,3)
      #IF THERE AT LEAST 2 RAINDROPS IN THIS POSITION
      if c > 2:
        #REMOVE THE RAIN FROM THIS POSITION
        data[ir][ic] -= c
        #IF NOT ON THE BOTTOM ROW
        if ir < len(data) -1:
          #ADD THE SUBTRACTED AMOUNT OF RAIN TO THE ROW BELOW
          data[ir+1][ic] += c
