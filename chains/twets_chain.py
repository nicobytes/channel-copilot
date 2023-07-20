import openai
from langchain.llms import OpenAI
from langchain import LLMChain
from chains.twets_prompt import TWEETS_PROMPT

class TweetsChain():
    def __init__(self):
        llm = OpenAI(
            model_name='gpt-3.5-turbo',
            temperature=0.5,
            max_tokens=512,
        )

        self.chain = LLMChain(
            llm=llm,
            prompt=TWEETS_PROMPT,
        )

    def generate_response(self, context: str) -> str:
        return self.chain.predict(context=context)

    @classmethod
    def from_class(cls):
        return cls()
