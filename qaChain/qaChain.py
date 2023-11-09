import os
import openai
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
import chromadb
from langchain import OpenAI

from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
import langchain
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain import OpenAI


os.environ["OPENAI_API_KEY"] = "sk-5aZWtniFibjIru2H2f65596216314f97Aa9c6a54Cf6aA93f"
os.environ["OPENAI_API_BASE"] = "https://api.132999.xyz/v1"


    



embeddings = OpenAIEmbeddings()

#指定chroma持久化的目录，当我们不知道目录时,chroma会将数据存储在内存中，随着程序的关闭就会删除
persist_directory = "./chroma_public"
# 将 document 通过 openai 的 embeddings 对象计算 embedding 向量信息并临时存入 Chroma 向量数据库，用于后续匹配查询

# docsearch = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
client = chromadb. PersistentClient(path=persist_directory)

docsearch = Chroma(client=client, embedding_function = embeddings)
print("加载向量数据库完成！共{}条数据".format(len(docsearch.get()['documents'])))




# 开启debug
# langchain.debug = True

# 提示词模板定义
template ="""你是我的AI小助手kengerbot，性格：冲动，暴躁。请你根据下面上下文（context）的知识内容回答做出回答。
要求：
1. 你应该回答对方的发言，对方的发言并不一定是一个问题，也可能是一些吐槽，你应该做出妥善回答
2. 提供的（content）中包含大量的梗知识，你在回答的过程中应该灵活的运用这些梗的说话风格来回答对方的发言。
2.1 千万不要去解释这些词语，更不要去解释词语的来源
3. 运用这些梗，并不是原封不动的用梗来回答，而是应该结合应用场景，可以适当的替换一些字词
4. 可以不用严格遵循标点符号的正确性，适当的错误标点符号，或者不输入
5. 你的回答应该具有一定逻辑性，不要上下文完全不一致。语句要流畅
5. 回答请不要太长，尽量像真是人类一样
context：\"\"\"{context}\"\"\"
问题：{question}
答案："""

# 创建模板
QA_CHAIN_PROMPT = PromptTemplate.from_template(template)


#定义系统角色

llm = OpenAI(model_name="gpt-3.5-turbo", temperature=0.5)



#通过chain_type_kwargs参数设置提示词模板
qa_chain = RetrievalQA.from_chain_type(
    llm,
    chain_type="stuff",
    retriever=docsearch.as_retriever(
        search_type="mmr", 
        search_kwargs={'k': 2, 'lambda_mult': 0.25} #检索更多具有更高多样性的文档 # 如果您的数据集有许多相似文档
    ),
    chain_type_kwargs={"prompt": QA_CHAIN_PROMPT},
    return_source_documents=True
)

def kengerbot_qa(question):
    result = qa_chain(question)
    return result['result']

if __name__ == '__main__':

    kengerbot_qa("你是谁")