from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain import hub

prompt = hub.pull("nicobutes/summary-transcription")

model = ChatOpenAI(model="gpt-4o")
output_parser = StrOutputParser()

summary_chain = (
    {
        "transcript": RunnablePassthrough(),
        "language": RunnablePassthrough(),
    }
    | prompt
    | model
    | output_parser
)
