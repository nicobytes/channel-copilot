from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain import hub

prompt = hub.pull("chickensoup/twitter-thread")

model = ChatOpenAI(model="gpt-4-0125-preview")
output_parser = StrOutputParser()

thread_chain = (
    {
        "word_count": RunnablePassthrough(),
        "target_audience": RunnablePassthrough(),
        "language": RunnablePassthrough(),
        "number_of_tweets": RunnablePassthrough(),
        "text": RunnablePassthrough(),
    }
    | prompt
    | model
    | output_parser
)