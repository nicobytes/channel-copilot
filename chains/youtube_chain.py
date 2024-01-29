from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain import hub

prompt = hub.pull("nicobutes/youtube")

model = ChatOpenAI(model="gpt-4-0125-preview")
output_parser = StrOutputParser()

youtube_chain = (
    {"summary": RunnablePassthrough(), "language": RunnablePassthrough()}
    | prompt
    | model
    | output_parser
)
