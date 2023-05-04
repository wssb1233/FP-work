# FP-work
This is a README file, please read it before you use any other file.
Both Task1 and 3 can run from terminal

really important:
You should go into both Task1.py, Task3.py, copy your sudoku into my file (at the top just after 'import') in correct structure 
And modify a list named 'grids' which only include name of your sudoku, 'grids' should follow your sudoku at the top.


In the terminal, you should keep your files that contain sudoku you want to solve and my solving file(Task1/3) in same directory or just on the desktop.

Make sure your route of terminal is correct and keep same with files above.

You can use 'cd' in terminal to change your route and 'pwd' to check your current route.

When you try to run my file, there's a structure: 'python --Task1.py --file 'input.txt' 'output.txt' --hint N --explain'

Arguments start with '--' are flags. 'input.txt' is your sudoku file and should into a '', as well as 'output.txt'. 

For output, a new file will be created when you first run my file.
1. If you try another sudoku and use same file name in 'output.txt', the new one will cover the old one.
2. If you use another file name like 'output1.txt', a new one will be created and would not influence the old one.

N is a number followed with '--hint', this is the number of empties you want to skip
and I recommend you do not give a large number, enjoy solving your sudoku step-by-step.

'--explain' will show you how our code work by fill and undo empties with their coordinates.

The last flag we have is '--profile', when you type 'python Task1.py --profile' in your terminal, a graph of 
time spended vs difficulty
will be plotted which includes several points ( dependent on numbers of your sudoku) and a best fit line.

If you do not give any flag, our code will automatically solve all you sudoku and gives time for each solving.

File Task 2 should not be run.
