from settings import settings

from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain import hub
from langchain_openai.chat_models.base import BaseChatOpenAI

prompt = hub.pull("nicobutes/linkedin")

#model = ChatOpenAI(model="gpt-4o")
model = BaseChatOpenAI(
    model='deepseek-reasoner', 
    openai_api_key=settings.deepseek_api_key, 
    openai_api_base='https://api.deepseek.com',
    max_tokens=1024
)

output_parser = StrOutputParser()

linkedin_chain = (
    {
        "type_content": RunnablePassthrough(),
        "counter_p": RunnablePassthrough(),
        "language": RunnablePassthrough(),
        "summary": RunnablePassthrough(),
        "format": RunnablePassthrough(),
        "link": RunnablePassthrough(),
        "target_audience": RunnablePassthrough(),
    }
    | prompt
    | model
    | output_parser
)
