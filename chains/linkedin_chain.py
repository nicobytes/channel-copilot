from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain import hub

prompt = hub.pull("nicobutes/linkedin")

model = ChatOpenAI(model="gpt-4-0125-preview")
output_parser = StrOutputParser()

linkedin_chain = (
    {
        "counter_p": RunnablePassthrough(),
        "language": RunnablePassthrough(),
        "summary": RunnablePassthrough(),
        "link": RunnablePassthrough(),
        "target_audience": RunnablePassthrough(),
    }
    | prompt
    | model
    | output_parser
)
