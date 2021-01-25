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




