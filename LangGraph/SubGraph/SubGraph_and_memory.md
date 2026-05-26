![alt text](image.png)

# Need Of Sub-Graph

![alt text](image-1.png)

# Types of the SubGraph 

1) invoke a graph from a node  :) one node is Reference  to the  other one  

2) Add a graph as a node :) The node is Contain the subGraph !!  


![alt text](image-2.png)


# Important Links of Sub-Graph

https://docs.langchain.com/oss/python/langgraph/use-subgraphs?utm_source=chatgpt.com

# Sample of SubGraph 

https://docs.langchain.com/oss/python/langgraph/use-subgraphs?utm_source=chatgpt.com#stream-subgraph-outputs

# Facts

llm don't have any intrinsic memory 


# function 

y = f@(X)

We have to develop the feature of the memory 

# Context Window 

![alt text](image-3.png)

# In-Context Learning :) 



![alt text](image-5.png)




# The Solution Principle 01



![alt text](image-4.png)



# short term Memory :) 
![alt text](image-6.png)

# Problems with the short term memory 

problem 1 ) this is very fragile  :) can break easily 

u can use the database that is persistance ! 

problem 2 _) The context window problem 
mazimum number of token which is used by the llm while generating the answer 

The solution 
![alt text](image-7.png)
 

3>) short term memory is thread scoped 
STM is thread-scoped

A. Loss of user continuity across conversations
B. Learning never compounds over time
C. Cross-thread reasoning is impossible 

# Solution 

![alt text](image-8.png)
# Types of long term memory 


![alt text](image-9.png)

# How does the Long term memory works 
![alt text](image-10.png)
![alt text](image-11.png)
![alt text](image-12.png)
![alt text](image-13.png)

# Famous Library 

The famous for managing the memory is LangMem 

and the plat-form is mem) and also the super-memory 
and also google research paper is :) titans + meiras helping ai have long term memory 