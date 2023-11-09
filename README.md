# kenger_ai
 kenger ai service


## 向量数据库
langchain教程里面用的的是Chroma向量数据库

### Chroma数据库使用
指定chroma持久化的目录，当我们不知道目录时,chroma会将数据存储在内存中，随着程序的关闭就会删除
`persist_directory = "./public"`



# ref

https://guangzhengli.com/blog/zh/gpt-embeddings/#prompt-%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5

[向量数据库](https://guangzhengli.com/blog/zh/vector-database/)

[基于GPT3.5实现本地知识库解决方案-利用向量数据库和GPT向量接口-实现智能回复并限制ChatGPT回答的范围](https://www.cnblogs.com/taoshihan/p/17252572.html)


## langchain 
[中文相关教程](https://github.com/liaokongVFX/LangChain-Chinese-Getting-Started-Guide)





# kenger ai v1.0

## 目的

我想要做一个什么，想要做点什么给我学习LLM收个尾。

虽然目前基于Agent的架构仍然有着较大的限制。但是还是可以考虑作为参考的。于是采用langchain框架。

目前的langchain之所以这么弱主要两个方面的原因吧。

- 架构本身的能力不足，架构不是百分百完美的，是以LLM为核心决策，以tools为扩展实现多方面的计算机任务，达到类似智能化的效果。
- LLM决策智能化有限。
  - LLM目前能力有限，存在幻觉问题等等
  - LLM不能保证100%正确。



综上，为了保证自己学习的知识实打实的变成自己掌握的，决定还是将学习到的东西，变成实际的对自己有用的工具。

## 项目架构

以LLM为核心，设计一个自动任务执行工具。

涉及到的核心模块：

- prompt工程，本项目计划使用openai的gpt服务
- 向量数据库，本地知识库。本项目使用chroma
- tools：
  - 发送邮件服务
  - 查询梗百科
  - 执行更新数据库服务
- chain
  - 一个chain在langchain里面就是一个任务的执行
- memory：内存，在langchain这里代表记忆。对话的历史记录





# 附录







## 语料收集

### 贴吧
[入典](https://zhuanlan.zhihu.com/p/569491745?utm_campaign=&utm_medium=social&utm_oi=1037133522892521472&utm_psn=1692899178441875456&utm_source=zhihu)









