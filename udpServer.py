from socket import *

usersOnline = {}

def udp_server():
    # Create a UDP socket
    sock = socket(AF_INET, SOCK_DGRAM)

    # Bind the socket to the port
    server_address = ('', 20000)
    sock.bind(server_address)

    print('UDP server is up and listening on port 20000')

    BUFFER_SIZE = 65507
    while True:
        # Receive message
        data, address = sock.recvfrom(BUFFER_SIZE)
        message = data.decode()
        
        if message.startswith("join "):
            #only gets the username part and not the join part
            username = message.split(" ")[1] 
            #saves username and the address
            usersOnline[username] = address
            print(f"{username} joined the chat. Hello!")
        elif message == "users":
            #Makes usersOnline keys into a one big string joined together
            usersList = ", ".join(usersOnline.keys())
            sock.sendto(f"People online: {usersList}".encode(), address)
        elif message.startswith("from "):
            #Separates the sender from the actual command. 2 makes sure only 3 max splits.
            start, sender, command = message.split(" ", 2)
            
            #will make a list of size 2. index 1 contains the actual message
            #index 0 contains the to and recipients
            parts = command.split(" msg ", 1)
            recipientPart, msg = parts

            #only gets recipients in a list and not "to "
            recipients = recipientPart[3:].split()
            
            if "all" in recipients:
                for user, userAddress in usersOnline.items():
                    #makes sure we aren't sending to ourselves
                    if user != sender:
                        sock.sendto(f"<{sender}> {msg}".encode(), userAddress)
            else:
                for recipient in recipients:
                    #makes sure we aren't sending to ourselves
                    if recipient != sender:
                        if recipient in usersOnline:
                            sock.sendto(f"<{sender}> {msg}".encode(), usersOnline[recipient])
                        else:
                            sock.sendto(f"Error Message: <{recipient} is not online!>".encode(), address)
        elif message.startswith("leave"):
            username = message.split(" ")[1]
            #removes the username key and value from the dictionary
            del usersOnline[username]
            print(f"{username} left the chat. Goodbye!")

if __name__ == "__main__":
    udp_server()