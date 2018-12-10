#two ways to import, a module and a function from a module
#if you import a module, you need to use as a namespace, dot notation
import math
math.sqrt(36)

#another way to do the top command
from math import sqrt
sqrt(36)

lst = [1, 2, 3]
list()
#after define the list as a interger with the first line, the list function (second line) is no longer a function
#I need to delete the intger list as following

from math import pi
pi
del list
list()
#use 'as' to alias a package name, e.g. import pandas as pd
#surround: ysw' to add single quote to add one side ' to a single word, yse' to add two side single quotes, ys$' to surround the rest line with ', css ' " change single quote to double quotesu
#gg to go to top, capital G to go to bottome, 9gg or 9G to go to line9, 50% takes to midway through a file
#ideavimrc: space is to run current line
#capital V select a line, 4j to select the following 4 lines, then you can alt+shift+E to run multiple lines

from pandas import DataFrame
#if change dataframe into *, all modules will be imported, be careful, because it will account too much space
import this

import __hello__
__hello__
#import __hell0__ is eaqual to print("hello word")
from __future__ import braces
    print(i)