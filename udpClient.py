from socket import *
import os

BUFFER_SIZE = 65507
buffer = []
def checkKeyboardInput():
    if os.name == 'nt':  # Windows
        import msvcrt
        if msvcrt.kbhit():
            ch = msvcrt.getwch()  # Get a single character from the input
            print(ch, end='', flush=True)
            if ch == '\r':
                print(flush=True)
                line = "".join(buffer)
                buffer.clear()
                return line            
            elif ch == '\b':
                if len(buffer) > 0:
                    buffer.pop()
                    line = "".join(buffer)
                    print(f"\b  ", end='', flush=True)
                    print(f"\r{line}", end='', flush=True)
            else:
                buffer.append(ch)
                return None

def main():
    clientSock = socket(AF_INET, SOCK_DGRAM)
    serverAddress = ("127.0.0.1", 20000)

    username = input("What's your username? ")
    clientSock.sendto(f"join {username}".encode(), serverAddress)

    print(f"Welcome, {username}! Type 'users', 'to <recipient> msg <message>' or 'leave'.")

    while True:   #Continues until user types leave
        line = checkKeyboardInput()
        
        if line:
            if line == "users":
                clientSock.sendto(line.encode(), serverAddress)
            elif line.startswith("to"):
                clientSock.sendto(f"from {username} {line}".encode(), serverAddress) #sending username as well so recipients know who sent the message
            elif line == "leave":
                clientSock.sendto(f"leave {username}".encode(), serverAddress)
                print("Thank you! Come back soon!")
                break
    
        clientSock.settimeout(0.05)  # 50 ms timeout for recieving stuff from server
        try:
            response, _ = clientSock.recvfrom(BUFFER_SIZE)
            print(response.decode()) #prints server response
        except timeout:
            continue
    
    clientSock.close()

if __name__ == "__main__":
    main()