from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain import hub

prompt = hub.pull("nicobutes/generate_blog_post")

model = ChatOpenAI(model="gpt-4o")
output_parser = StrOutputParser()

blog_chain = (
    {
        "language": RunnablePassthrough(),
        "keyword": RunnablePassthrough(),
        "context": RunnablePassthrough(),
    }
    | prompt
    | model
    | output_parser
)
