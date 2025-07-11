from langchain_openai import ChatOpenAI 
from langchain.agents import AgentExecutor, create_react_agent
from langchain.prompts import PromptTemplate
from llm.tools import tools_list

TEMPLATE = """You are a highly intelligent and diligent deep research agent. Your goal is to conduct comprehensive research on the provided topic, extract relevant information from various sources, and finally generate a detailed and well-structured report.

Here are the tools you have access to:
{tools}

Use the following format:

Question: the question you must answer
Thought: you should always think about what you will do
Action: the action to be executed, must be one of {tool_names}[input]
Observation: the result of the action
... (this Thought/Action/Observation can repeat multiple times)
Thought: I have finished researching and now I know the final answer.
Final Answer: the final, detailed report.

Your research should be iterative. Start with a broad search, identify relevant URLs, read the content of those URLs, summarize what you found, and, if necessary, conduct more specific searches or read more URLs to deepen your knowledge.

Ensure you cover the main aspects of the topic and present the information clearly and concisely. If the research requires, include different perspectives or viewpoints.

Begin!

Question: {input}
{agent_scratchpad}"""

def create_executor(model: str, api_key: str):
    llm = ChatOpenAI(model=model, temperature=0.7, api_key=api_key) 


    prompt = PromptTemplate.from_template(TEMPLATE)

    agent = create_react_agent(llm, tools_list, prompt)

    agent_executor = AgentExecutor(agent=agent, tools=tools_list, verbose=True, handle_parsing_errors=True)

    return agent_executor

def invoke_agent(executor: AgentExecutor, prompt: str):
    if not executor:
        return
        
    result = executor.ainvoke({'input': prompt})

    return result['output']
    