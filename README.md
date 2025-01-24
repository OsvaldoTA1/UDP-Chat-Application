# UDP-Chat-Application
## Overview
This project implements a client-server chat application using the UDP protocol. The server manages client connections, routes messages, and keeps track of online users. Clients can communicate with each other by sending messages through the server.
## Features
- Centralized server for managing multiple client connections.
- Single-threaded program
- Commands for Client
  - users (View all online users)
  - to <username(s)> msg <message> (Send message to one or more users)
  - to all msg (Send message to everyone online)
  - leave (exit the chat session)
 
## How it works
1. Start the server application (must be run first) on command prompt
2. Start the client application (also on command prompt)
3. Enter a username to join the chat session
4. Use the supported commands to interact with other clients
