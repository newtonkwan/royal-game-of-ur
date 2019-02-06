# The Royal Game of Ur

### A project aimed to master the Royal Game of Ur tabula rasa

#### Ways to play 
- Player vs. Player: Run "python player_vs_player.py"
- Player vs. Computer (Random): Run "python player_vs_random.py"

#### Ways to simulate
- Computer (BasicTwo) vs. Computer (BasicOne): Run "python basic2_vs_basic1.py"
- Computer (BasicTwo) vs. Computer (Random): Run "python basic2_vs_random.py"
- Computer (BasicOne) vs. Computer (Random): Run "python basic1_vs_random.py"
- Computer (BasicTwo) vs. Computer (BasicTwo): Run "python basic1_vs_basic1.py"
- Computer (BasicOne) vs. Computer (BasicOne): Run "python basic1_vs_basic1.py"
- Computer (Random) vs. Computer (Random): Run "python random_vs_random.py"

##### 2.5.19
- created BasicTwo: an agent that will send home an opponent's piece if possible, playing randomly otherwise 
- matched up BasicTwo vs Random (basic2_vs_random.py)
- matched up BasicTwo vs BasicOne (basic2_vs_basic1.py)
- discovered BasicTwo strategy is better than Random (4.4% increased win rate)
- discovered BasicTwo strategy is better than BasicOne (2% increase win rate)

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