# The Royal Game of Ur

### A project aimed to master the Royal Game of Ur tabula rasa

#### Ways to play 
- Player vs. Player: Run "python player_vs_player.py"
- Player vs. Computer: Run "python player_vs_computer.py"

#### How to simulate
- Computer vs. Computer: Run 'python computer_vs_computer.py'

##### 2.7.19
- added 'computer_vs_computer.py', which allows simulations of any combination of agents 
- moved old test / obselete files into old_test_files folder 
- discovered BasicThree strategy is better than Random (7% win rate increase)
- discovered BasicThree strategy is better than BasicOne (4% win rate increase)
- discovered BasicThree stretegy is better than BasicTwo (2.5% win rate increase)

##### 2.6.19 
- created BasicThree: an agent that is a combination of BasicOne and BasicTwo, prioritizing BasicOne strategy
- add 'player_vs_computer.py', allowing player to choose which agent to play
- add ability to play against BasicOne and BasicTwo 

##### 2.5.19
- created BasicTwo: an agent that will send home an opponent's piece if possible, playing randomly otherwise 
- matched up BasicTwo vs Random (basic2_vs_random.py)
- matched up BasicTwo vs BasicOne (basic2_vs_basic1.py)
- discovered BasicTwo strategy is better than Random (4.5% increase in win rate)
- discovered BasicTwo strategy is better than BasicOne (2% increase in win rate)

##### 2.4.19 
- created BasicOne: an agent that will move a tile to the end tile if possible, playing randomly otherwise. 
- matched up BasicOne vs Random (basic1_vs_random.py)
- discovered BasicOne strategy is better than random (2.5% increase win rate)
- discovered going first is always beneficial (1.5% increase win rate)

##### 2.2.19
- completed a player vs computer mode (player_vs_random.py) for '3x4, no flowers, 0-2 die' version where you can play against a computer that plays randomly. 
- added the option to replay at the end of each game for pvp and player vs computer
- added time delays for the player vs. random to give a smoother experience and simulate computer 'thinking'.

##### 2.1.19
- completed a simplified '3x4, no flowers, 0-2 die roll' version. Run 'python play.py'
- added ability to simulate games with agents that play randomly. Run 'python random_play.py' 
- conducted analysis in discoveries.txt

##### 1.31.19
- start version 2.0