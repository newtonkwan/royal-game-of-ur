### A project aimed to master the Royal Game of Ur tabula rasa

#### Ways to play 
- Player vs. Player: Run "python play.py"
- Player vs. Computer (random play): Run "python player_vs_random.py"
- Computer (randomly play) vs. Computer (randomly play): Run "python random_play.py"
- Computer (BasicOne) vs. Computer (randomly play): Run "basic1vrandom.py"
- Computer (BasicOne) vs. Computer (BasicOne): Run "basic1vbasic1.py"


##### 2.4.19 
- created BasicOne: an agent that will move a tile to the end tile if possible, playing randomly otherwise. 
- matched up BasicOne vs Random (basic1vrandom.py)
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