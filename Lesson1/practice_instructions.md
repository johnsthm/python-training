Practice Instructions
=====================

*File to work in: practice.py*

Use these instructions to complete the practice for Lesson 1.

Now that we've learned how to create and run a Python program, let's create something awesome. We learned how to work with lists, how to `print`, and how to generate random integers.

Your challenge is to use what you learned to make a basic tic-tac-toe game.

## Instructions

Some of the game in file practice.py has already been written for you. Your job is to fill in the blanks. Whenever you see `# TODO` in the code, substitute your code there. These `# TODO` comments will tell you what needs to be done.

The program starts by calling `play_game()` at the bottom of the file. Within the `play_game()` function, a `while loop` executes the code within it until a `break` statement is reached--this is how we end the game.

You will need to implement code wherever `# TODO` is found in the file. These are found in the aforementioned `while loop` as well as within the functions `check_line_for_win(character, pos1, pos2, pos3)`, `check_for_winner(player)`, and  `is_cats_game()`.

Your deliverable is a working tic-tac-toe game that allows a player to place 'X's at chosen positions on the board, and handles player X winning, player O winning, and a Cat's Game. The board should be printed to the screen each time the player makes a move, and the game should end gracefully when done.

## How to Run and Test the File

Since Sublime Text doesn't work well with user input, we will run the program in the Terminal.

First, using Finder, navigate to the file practice.py on your computer. Right click and select *Get Info*. Find *Where:* (under *General*) and copy the text after it. This looks like:

Macintosh HD > Users > etc...

Now open Terminal and type

`cd `

Paste the text after `cd` (dont' forget a space after `cd`).

Part of mine looks like this:

`cd /Users/DavidSchommer/Documents/` ...

Hit enter. This brings you to the directory (folder) that has the file *practice.py*.

To run your program, type

`python practice.py`

and hit enter.

You will get errors now, but as you complete the project you will be able to run and test your program.

If your program doesn't want to end, hit

control d

## Hints:

* Use `int(input_variable)` to convert the `string` from `input_variable = raw_input()` to an `int`.
You could write something like this:
```
input = raw_input('What is your favorite integer?')
input = int(input)
```
* You will see code like this:
```
if check_for_winner('o'):
    # TODO: Print "=== O Won! ===" and print the board
	  break
```
In this code, `check_for_winner()` returns a `Boolean` (True or False) value. Therefore, if 'o' is a winner, `check_for_winner('o')` will return `True` and whatever is in the `if` statement will be executed. You are expected to implement `check_for_winner()` (a template of it is already in the code) and to write code that does what the `TODO` comment asks for.

* Some tasks only require you to call functions. For example, if you are asked to print the game board, call `print_board()` which has already been implemented for you.

## Extra Credit - How to Make the Game Better:
* Handle the case where a user may give invalid input. For example, the letter 'a' instead of a number.
* Include AI opponent player instead of randomly assigning the opponent's position.
