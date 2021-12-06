# Project 3: Final Project
## Rock, Paper, Scissors Game

For the previous Projects, I decided to do a code that told the user the current time, and then eventually added differing time zones. For this project, I chose to 
do something a bit more fun and do the classic Rock, Paper, Scissors Game.

### code

The code will start by prompting the user, or Player A, to enter in their choice of either Rock (R), Paper (P), or Scissors (S)

<code> playerA = input('Player A, please enter Rock (R), Paper, (P), or Scissors (S): ') </code>

The user will then enter in their choice, and then a random number generator will generate a single number falling between 1 and 3, in which 1 = rock, 
2 = paper, and 3 = scissors for the bot.

It will then compare the rock, paper, or scissors selection between Player A's and the Bot's choice. 

The code will either generate a 'Player A wins!' or 'Bot Wins!' or 'Tie!'

In the event of the user entering in an invalid input, the code will output:

<code> Player A, please enter Rock (R), Paper, (P), or Scissors (S): (invalid input)
You have entered an invalid input </code>
  
<code> Please run program again and enter capital R for Rock, P for Paper, and S for Scissors. </code>

### notes and sources
https://thehelloworldprogram.com/python/python-game-rock-paper-scissors/

https://www.youtube.com/watch?v=8ext9G7xspg&t=1274s

https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html

https://realpython.com/python-rock-paper-scissors/

