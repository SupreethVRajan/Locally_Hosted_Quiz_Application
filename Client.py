# IMPORTS
import socket, threading
import multiprocessing
import time
from inputimeout import inputimeout, TimeoutOccurred
from _thread import *

# INITIALISATIONS
PORT = 1590
buzzervalue = False
ackvalue = [True]
ackmsgs = []
flag = []

# CONNECING TO SERVER
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostname(), PORT))
print(client.recv(1024).decode('utf-8'))
clientname = input()
client.send(bytes(clientname, 'utf-8'))
print("Please wait for all the participants to connect.")
msg = client.recv(1024).decode('utf-8')
print(msg)

def recvmsg():
    msg = client.recv(1024).decode('utf-8')
    return msg

    
def sendmsg(msg):
    msg = bytes(msg, 'utf-8')
    client.send(msg)

def buzzer():
    try:
        buzzer = inputimeout(prompt="(Press b and enter for buzzer)\n", timeout=10)
        if ackvalue[0]:
            sendmsg("b")
    except TimeoutOccurred:
        pass

def acknowledgement():
    check = recvmsg()
    ackvalue[0] = False
    ackmsgs.append(check)

def managequiz():

    # TIMING
    for _ in range(2):
        print(recvmsg())

    
    while True:
        # QUESTION DISPLAY
        print(recvmsg())
        q = recvmsg()
        print(q)

        # BUZZER
        b = threading.Thread(target=buzzer)
        b.daemon = True
        a = threading.Thread(target=acknowledgement)
        a.daemon = True
        intime = time.time()
        b.start()
        a.start()

        a.join()
        b.join()

        ack = ackmsgs[0]
        ackmsgs.pop(0)
        ackvalue[0] = True

        if time.time() - intime < 10:
            time.sleep(10 - time.time() + intime)

        if ack == "timeout":
            print("Timeout!!")
        else:
            if ack == "buzz":
                # ACKNOWLEDGEMENT
                print("You have pressed the buzzer.")

                # ANSWER
                ans = input("Answer: ")
                sendmsg(ans)
            else:
                # ACKNOWLEDGEMENT
                print(ack)

            # CHECKING
            print(recvmsg())

        # SCORES
        print(recvmsg())

        time.sleep(0.2)
        # STOP
        if len(flag) != 0:
            for x in flag:
                flag.remove(x)
        x = recvmsg()
        flag.append(x)
        if flag[0] == "stop":
            break

    # WIN/LOSE 
    print(recvmsg())

managequiz()