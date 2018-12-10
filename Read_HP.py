#I am using python

# hello world
#control+W: delete word by word (insert mode)
#control+U: delete all the word before insert sign in the same line. (Insert mode)
#Press U in normal mode: undo all the stuff I did before
#control+R: redo (normal mode)
#After esc (normal mode): press capital I, to the cursor goes to the beginning of the line
#PRESS Capital A (normal mode): move the cursor  to the end of the line
#Small i: left to left of character, a: move cursor to right of the character

#Start a new line: capital O
#In non-insert state: K go up, J goes down
#Press zero (normal mode): move the cursor to the very beginning

# means the words are comments, is not code
#Press X delete comment: remove a single character
#Press dot (.): do the thing I just did

#dd (normal mode): delete the whole line
#2 dd delete two lines
#4 x delete 4 characters
#4I  repeat what you typed 4 times after esc
#alt+Shft+e: execute a command, shift to console: single line
#command+shif+A: enter action or option name
#Command shift “ : enlarge console, the code notebook will be not visible
#command+,: go to settings
#Sef-made keyboard shortcut: go to setting-keymap-hide all tool window
#Command 0: hide cosnole
#Normal mode: press b, the cursor back a word, W forward word by word
#cw: change a word
#capital C: change all the words at the right side of cursor
#in esc state: press yy then press p, copy the line to next line, press 3p: paste three times
#command+w: close console In pycharm
#Up arrow can get the previous code back
#The last command python takes it true

x=5
Y=6.5
type(Y)
type(x)

# assign multiple variables at once
z = 1, 2, 3
one, two, three = z
one, two, three = z
# the top two lines command is equal to: one, two, three = 1, 2, 3
# assign multiple variales using a list comprehension
zero, one, two = [y for y in range(3)]
zero, one, two = list(range(3))
# expalin for the top line: y for y means give me back x, the first y is what you return, the second y is what i take from range(3)
# to change a character: press r and then the letter i want
#yt[ and then capital P to past the line into square bracket, yt[ means copying the words between cursor site and [

x = 5
xf = float(x)
#x = 5: x is intger, x = '5', x is s string
# control+j: to show the quick documentation window of the function, such as integer, float, if the cursor is at the float
#to change everthing in quotes, ci' or ci"
name = 'Haiping'
type(name)
#types until now i have done: int, float, str, list, tuple (str is for characters)
#a piece of code: get a list of all capital letters
[chr(65+i) for i in range(26)]

#contro+alter+R: to go to run menue, command+4 to close and reopen the console


#command+shif+P: git clone, or git push, or
