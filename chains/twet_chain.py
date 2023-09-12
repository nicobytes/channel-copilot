import openai
from langchain.llms import OpenAI
from langchain import LLMChain
from chains.twet_prompt import TWET_PROMPT

class TweetChain():
    def __init__(self):
        llm = OpenAI(
            model_name='gpt-3.5-turbo',
            temperature=0.5,
            max_tokens=512,
        )

        self.chain = LLMChain(
            llm=llm,
            prompt=TWET_PROMPT,
        )

    def generate_response(self, summary: str) -> str:
        return self.chain.predict(summary=summary)

    @classmethod
    def from_class(cls):
        return cls()
