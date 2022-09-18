# Marble Gambling
A game where the user starts with £1000 and by random chance, wins or loses money. The user places a bet, size of their choice, and a random marble is pulled from a bag. If the marble is green, the user wins the bet, if red the user loses the bet, if black the user wins 10x the bet and if white, the user loses 5x the bet. There are 5 green marbles, 3 red marbles and one of both white and black.

---

###Technologies
Python 3.10-64
Random module

## Project Status
Complete with room for improvement.

## Example of project function

The program, when run, will initially ask the user to place a bet. The initial purse is £1000. If the purse subceeds £500 or the user inputs a non-integer as their bet, the game will end.

The program will give feedback after every question, discerning whether the solution was correct or not. Once all problems are solved, information about the performance is given i.e. all the questions asked, with their correct solutions, alongside the user answers. Information regarding the time taken to answer each question is then returned. Below is an example:

>Question 1: 10 * 8 = 80.
  >You answered: 80.
 >It took you 1.9 seconds to answer this question


## Room for improvement
- The program fails if a non-integer is input. An improvement can be made to accept non-integer answers and return a message asking for integers only.
- Duplicate questions can be avoided if random.sample() is used.

## Sources 
[Python 3.10.7 documentation](https://docs.python.org/3/)

## Other information
Contact me on Github under the username *Ibra-Zeno*
