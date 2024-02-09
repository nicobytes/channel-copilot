from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain import hub

prompt = hub.pull("nicobutes/youtube-tweet")

model = ChatOpenAI(model="gpt-4-0125-preview")
output_parser = StrOutputParser()

tweet_chain = (
    {
        "word_count": RunnablePassthrough(),
        "target_audience": RunnablePassthrough(),
        "language": RunnablePassthrough(),
        "text": RunnablePassthrough(),
        "link": RunnablePassthrough(),
    }
    | prompt
    | model
    | output_parser
)
