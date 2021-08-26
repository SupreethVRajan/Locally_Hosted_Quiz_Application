# Locally Hosted Quiz Application

## Aim

The aim of this project is to understand the working and usage of sockets by making a locally hosted quiz application.

## Assumptions

The server supports exactly 3 clients. Random questions are displayed to all the clients. Then if one of the clients presses the buzzer within 10 seconds, and if he/she answers correctly, he/she gets +1 marks. But if he/she answers incorrecty, he/she will recieve -0.5 marks. And if nobody presses the/she buzzer within 10 seconds, no client will recieve any marks. The first client to recieve 5 marks will be declared the winner. But if nobody gets 5 marks from 100 questions or when everyone recieves   -3 marks, then nobody will be declared the winner and the quiz will end.

## Softwares used and extra requirements:

This project has 2 files: Server.py and Client.py. Both these scripts are coded using python3. The host computer needs to have python3 installed in it. The Client.py script also has an additional library called inputimeout which is not preinstalled with python3. This can be installed in the host with commands:  
**$ sudo apt-get install pip3**  
**$ pip3 install inputimeout**

## Working

The server is run first(Command: $ python3 Server.py) and then 3 client programs are run(Command: $ python3 Client.py). The clients are required to give a name and then after all names are given the questions will start appearing after 15 seconds. Then if one of the players presses the buzzer within 10 seconds, an answer query will be displayed on that player’s screen and then he should give the option number of the answer. Then a message will appear on the screen whether the client  answered correctly or not. If nobody presses the buzzer within 10 seconds, then a message will appear on the screen saying nobody pressed the buzzer. After this the scores will be displayed and then the program will wait for a few seconds for the next question to appear. If anyone wins the game, then a message will be sent to the clients about the winner. And if nobody wins the game the reason will be displayed on the screen and then the game will end.

**P.S.** The questions.py file is used to randomly generate questions and store it in the questions.dat file. The contents of this file are then copied to the top of Server.py file and then the application can be run with new questions. The questions can be changed by changing the questions.py file and following the instructions stated before.