for implementing the short term memory we use the 

1. check pointer 
2. threads 

see the reference 

# Context OverFlow problem 
an error that occurs when the total data (input prompt, system instructions, and generated output) exceeds a Large Language Model's (LLM) maximum token limit

# OverCome methods 

1. TRiming  :) Remove the un neccessary message 

set max token count and max token count exceed to the set remove the oldest messages 
![alt text](image.png)

function  by langGraph :) trim_message 

![alt text](image-1.png)

Flaws they delete the old messages 
and the old messages not deleted 
only the context is trimmed 

2. Summarization 

:) summarise the old message and  send the latest messages  adn the old messages were deleted 
![alt text](image-2.png)

imports 

from lang-chain.messages import RemoveMessages 