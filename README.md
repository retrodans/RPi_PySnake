## About
This game used the snake tutorial from **Raspberry Pi User Guide** as a base.  The basic game loaded directly into the game, using squares for elements, and a 'game over' text when you died which auto exited after 5seconds.
What I wanted to do was run through the tutorial, and then look into adding a bit of extra functionality to the game to allow me to learn a bit more about developing in Python.  To this end, whilst I looked at a few contrib extensions, the only one I used was ktext, deciding to write my own menu navigator.

### The extra features were
* On game over
    + Disable auto exit functionality
    + Display a line of text explaining how you died
    + Display a line of text explaining what to do next
    + Listener for whether user wants to play again or exit
* A Menu system
    + On load display a menu navigable by cursor keys or letter shortcuts
    + Options should be: start, help, quit
* Visual improvements
    + Replace raspberry square with an actual image
    + Insert a circuit board style repeating background image

***

## Why
As part of some personal research time I allocated myself, I wanted to start on some RaspberryPi development.  To do this, I of course need to start to learn Python to at least a very basic degree.  I am a web (PHP) developer by trade, so this was not a huge leap, the logic was similar, so using search engines to get answers was fine as I had the code terminology already in my head.
Ultimately though, this was a means to an end, so I allocated about a day and a half to go through tutorials and write this up, so a shame I don't get to tidy it up any more, but maybe I can come back to it if I have time in the future.

***

## What I learnt
Whilst going from PHP to Python was easier than starting from nowehere, there were still a few areas in particular which I had to learn.  Not only were there coding differences, but also the ecosystem was a complete change of process for me.  With PHP I was spoilt with the depth of information out there, and the knowledge that if I needed trustworthy documentation PHP.net was always there.
* **Code References:** In python, I had a few disparate sites to help, and the pygame site was generally just a group of people like me sharing code which may or may not be to a high standard.
* **Intro to pygame:** http://www.pygame.org/docs/tut/newbieguide.html
* **Variables:** Instead of having a variable which has a value assigned to it, Python variables are simply references to a value stored in memory.  What this means is that if you write some code so that `a=1`, and then go on to set `b=a` all appears fine.  BUT if you later decide to edit b (eg. `b=2`), the pointer of both a AND b will point to 2.  To get around this you can use immutable variables as a set of default (mentioned in a minute) OR use math to set your variables (eg. b=a+1).
* **Mutability:** Mutable v Immutable (http://www.youtube.com/watch?v=1HPC24nIy9E)  Mutability is the potential of a variable to change it's value after it has been created. The general concept of mutability is one not so common to PHP, the only similar item I tend to use in Drupal is `static`, which is why my logic of immutable variables was used to create default variables which never change.  The items below show a mutable list, and an immutable Tuple.  Tuples can be used as a direct alternative to lists (and vice versa) just use a lsit() or tuple() function to convert if required.  I am still unsure if I used this in the right way, but Tuples seemed great for static variables, as they don't break due to the value referencing point when being used as a default Or reset) value - see snakeSegmentsDefault as it's set as type tuple, but then referenced as a list() to convert it ready for use
    + List = mutable (can change values)
    + Tuple = immutable (cant change values)
* **Global variables:** must be set inside each function, but only required for write priviledges (not read)
* **Images:** Images sounded as though they would be one of the more complex elements in Python to implement, in face they were relatively simple within PyGame.   Just look at the examples on the site, as you just declare it to a surface, set some dimensions, and the blit it onto the page.  Text management was much more complicated to get working in the flexible way I have become used to with websites.
* **PiP:** PIP can be seen as similar to RVM or PEAR for getting down Python extensions/libraries http://askubuntu.com/questions/95037/what-is-the-best-way-to-install-python-packages
* **import and from:** xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

***

## Specifics which could be improved upon (code)
* OOP
* More reuseable text render method (build my own?)

***

## Specifics which could be improved upon (UI)
* Do a real design
* High score table
* Audio effects

***

## Glossary
* blit()
* mutability
* tuple
* surface
* PIP
* pygame


