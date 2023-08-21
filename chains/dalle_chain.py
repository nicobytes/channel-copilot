from langchain.llms import OpenAI
from langchain import LLMChain
from chains.dalle_prompt import DALLE_PROMPT

class DalleChain():
    def __init__(self):
        llm = OpenAI(
            model_name='gpt-3.5-turbo',
            temperature=0.2,
            max_tokens=512,
        )

        self.chain = LLMChain(
            llm=llm,
            prompt=DALLE_PROMPT,
        )

    def generate_response(self, text: str) -> str:
        return self.chain.predict(text=text)

    @classmethod
    def from_class(cls):
        return cls()
