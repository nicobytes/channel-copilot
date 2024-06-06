from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain import hub

prompt = hub.pull("nicobutes/twitter-thread")

model = ChatOpenAI(model="gpt-4-turbo")
output_parser = StrOutputParser()

thread_chain = (
    {
        "word_count": RunnablePassthrough(),
        "target_audience": RunnablePassthrough(),
        "language": RunnablePassthrough(),
        "number_of_tweets": RunnablePassthrough(),
        "text": RunnablePassthrough(),
        "link": RunnablePassthrough(),
    }
    | prompt
    | model
    | output_parser
)
