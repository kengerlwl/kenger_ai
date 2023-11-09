import os
import openai
# 导入第三方库
from langchain.agents import load_tools
from langchain.llms import OpenAI
# from langchain.agents import tools
from langchain.agents import Tool, initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI
from langchain.chains import LLMMathChain
from qaChain import qa_chain
import langchain
# 开启debug
langchain.debug = True


from langchain.memory import ConversationBufferMemory


from pydantic import BaseModel, Field


os.environ["OPENAI_API_KEY"] = "sk-5aZWtniFibjIru2H2f65596216314f97Aa9c6a54Cf6aA93f"
os.environ["OPENAI_API_BASE"] = "https://api.132999.xyz/v1"


os.environ["SERPAPI_API_KEY"] = '069f1da1a853a348841253778557259abbdc66d906d1576ce8f3cf3a8c22be47'





# 记忆单元
memory = ConversationBufferMemory(memory_key="chat_history")


# 定义输入结构体， Field 可用于提供有关字段和验证的额外信息，如设置必填项和可选，设置最大值和最小值，字符串长度等限制
class CalculatorInput(BaseModel):
    question: str = Field()
    
class WhoAmIInput(BaseModel):
    question: str = Field()

class kengerbotInput(BaseModel):
    question: str = Field()



# 告诉LLM我们的工具是什么
def who_am_i(question: str):
    return "我是你爸爸"



llm = OpenAI()
llm_math_chain = LLMMathChain(llm=llm)
tools = []


# 定义核心prompt的前后缀，可以修改,这里的prompt设置很重要，如果设置不好，会根本没有记忆
prefix = \
"""
Have a conversation with a human(chat_history), answering the following questions as best you can. You have access to the following tools:
"""

suffix = \
"""
Begin!
chat_history：{chat_history}
Question: {input}
Thought:{agent_scratchpad}
"""


"""
导入工具和自定义工具，
注意，工具和chain虽然分别属于不通的概念，但是实际上由很大的交集，tools是为了执行某些task。很多使用我们将chain也当作tools的函数来执行
"""
tools= [
    Tool(
        name="Calculator",
        func=llm_math_chain.run, # 将chain的run函数作为待调用的函数
        description="在需要回答数学问题时非常有用",
        args_schema=CalculatorInput
    ),
    Tool(
        name="我是谁",
        func=who_am_i,
        description="在询问自己是谁时非常有用"
    ),
    Tool(
        name="kengerbot智能AI小助手",
        func=qa_chain.run,
        description="在需要回答普通问题时非常有用，尤其是其接入了我的本地数据库",
        args_schema=kengerbotInput
    )
]
 


# 初始化代理
"""
agent类型选择OPENAI_FUNCTIONS。这个 Agent 是基于 OpenAI 的 Function Calling 实现的，它通过 format_tool_to_openai_function() 
agent_kwargs 用于传递一些额外的变量
"""
agent = initialize_agent(
    agent_type=AgentType.OPENAI_FUNCTIONS,    
    llm=llm,
    tools=tools,
    verbose=True,
    memory=memory,
    agent_kwargs={  
        "prefix": prefix,
        "suffix": suffix,
        "input_variables": ["input", "chat_history", "agent_scratchpad"],
    }
)


# 使用代理回答问题
response = agent.run("1+2=多少呢")
 
# 打印回答
print(response)