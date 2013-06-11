##About
This game used the snake tutorial from 'Raspberry Pi User Guide as a base.  But then went on to add the below extras:
- Ability to restart with Y or N and explanation copy
- Some instructions for when the game starts aswell as a 'ready' option
- Replaced raspberry square with an actual image
- Give user feedback on HOW they died



##Why
As part of some personal research time I allocated myself, I wanted to start on some RaspberryPi development.  To do this, I of course need to start to lear Python to at least a very basic degree.  I am a web (PHP) developer by trade, so this was not a huge leap, the logic was similar, so using search engines to get answers was fine as I had the code terminology already in my head.



##What I learnt
Whilst going from PHP to Python was easier than starting from nowehere, there were still a few areas in particular which I had to learn.  Not only were some of these in the code, but also the ecosystem.  With PHP I was spoilt with the depth of information out there, and the knowledge that if I needed trustworthy documentation PHP.net was always there.
- Python creates a value and references that (as opposed to settings a value to a variables), this means that if you set a=1, then do b=a, then edit b=2, the pointer of both a AND b will go to 2
- Mutable v Immutable (http://www.youtube.com/watch?v=1HPC24nIy9E)
-- List = mutable (can change values)
-- Tuple = immutable (cant change values)
-- Not sure if I used in right way, but Tuples seemed great for static variables, as they don't break due to the value referencing point when being used as a default Or reset) value - see snakeSegmentsDefault as it's set as type tuple, but then referenced as a list() to convert it ready for use
- PiP = http://askubuntu.com/questions/95037/what-is-the-best-way-to-install-python-packages
- Images
- Intro to pygame: http://www.pygame.org/docs/tut/newbieguide.html
- Global variables must be set inside each function, but only required for write priviledges (not read)



##Specifics which could be improved upon (code)



##Specifics which could be improved upon (UI)




