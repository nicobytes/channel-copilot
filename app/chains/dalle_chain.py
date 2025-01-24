from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain import hub

prompt = hub.pull("nicobutes/dalle")

model = ChatOpenAI(model="gpt-4-0125-preview")
output_parser = StrOutputParser()

dalle_chain = (
    {
        "text": RunnablePassthrough(),
    }
    | prompt
    | model
    | output_parser
)
