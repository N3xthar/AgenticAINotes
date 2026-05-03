Tools which is used to add the functionality to the programs or the agntic ai




                    start 
                    |
                    chat node 
                    |
            ------------------|
            |               Tool Node                
            |                  |
            ---------|----------
                    |
                    end 




🔧 Tool Node (Clear Definition)

A Tool Node is a processing unit (node) in a workflow/graph system that:

encapsulates one or more tools (functions/APIs) and executes them when triggered.

✔️ Key Characteristics
Contains predefined tools (functions, APIs, models, etc.)
Responsible for executing tool logic
Takes input → processes via tool → returns output
Often used in:
AI agents
Workflow engines
LangGraph / LangChain pipelines



Tool Condition (Clear Definition)

A Tool Condition is a control mechanism that:

decides which tool should be executed based on input, state, or logic.

✔️ Key Characteristics
Works like a decision layer
Evaluates:
Input
Context/state
Rules or conditions
Selects the appropriate tool dynamically