from settings import settings

from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain import hub
from langchain_openai.chat_models.base import BaseChatOpenAI

prompt = hub.pull("nicobutes/summary-transcription")

# model = ChatOpenAI(model="gpt-4o")
model = BaseChatOpenAI(
    model='deepseek-reasoner', 
    openai_api_key=settings.deepseek_api_key, 
    openai_api_base='https://api.deepseek.com',
    max_tokens=1024
)

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
