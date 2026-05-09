MCP Architecture
![alt text](image.png)




The more simpler architecture  is this 
![alt text](<WhatsApp Image 2026-05-09 at 6.16.13 PM (1).jpeg>)

PRIMITIVES IN MCP 

The things server can offer to host 

Example git hub server 




tools  :) Actions the ai ask the server to perform  
Resource :)  Structured data sources that the ai can read    and it is dynamic in  nature 
prompts  primptive :)   predefined prompts templated or instruction that the server offers to help shape the ai Behavious 


The Standard operation on the Mcp server through the client is these 
![alt text](<WhatsApp Image 2026-05-09 at 6.16.12 PM.jpeg>)


MCP DATA  LAYER 

the data layer is the language and grammer of the mcp ecosystem that everyone agrees upon to communicate 


in the mcp JSON RPC 2.0  serve as the foundation of the data layer 

java script object notation -Remote procedure call 

RPC :)   RPC (Remote Procedure Call) is a protocol that allows a program to execute a procedure on another computer over a network as if it were a local function call

                        json 
                        |
            ----------------------------
            |                           |
            rpc                        json 


we can also  send the request also dude 
in mcp for every request there is must every response 

but in 
Notification :) fire and forgot [No response u got ] [server to client]

WHY JSON RPC  FOR DATA LAYER 

A. Its light weight 

B. support bi directional communication 

C. it is transport agnostic [ operate seamlessly across different communication mediums it supports api , web sockets ]

D. Support batching [handled simultaneously rather than individually]
E. its support notification 


Transport layer :) mechanism that moves json-rpc message the between the client and server 

The choice of transport depends on the type of server 

There are two types or servers 

                                  Servers
                                    | 
                        -----------------------------
                        |                            |
                    Remote server               Local Server 


Local server :) server running in the same as the host is running 

if the transport layer happens between the local server called  the stdio [standard input and standard output ]

Hows does the stdio works 
1. The host launches the server as a subprocess on the same machine 
 establish parent child relationship 

2. the host client writes json-rpc messages into the servers stdin 

3. the server reads those messahes processes  them and writes back responese to it stdout 

BENEFITS 

FAST 
SECURE 
EASY TO IMPLEMENT 

remote server :) running on  the remote server ! 

THE transport which is used to communicate to the remote server that is http + sse 
`