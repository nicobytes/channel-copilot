import openai
from langchain.llms import OpenAI
from langchain import LLMChain
from chains.summary_prompt import SUMMARY_PROMPT

class SummaryChain():
    def __init__(self):
        llm = OpenAI(
            model_name='gpt-3.5-turbo-16k',
            temperature=0.2,
            max_tokens=512,
        )

        self.chain = LLMChain(
            llm=llm,
            prompt=SUMMARY_PROMPT,
        )

    def generate_response(self, transcript: str) -> str:
        return self.chain.predict(transcript=transcript)

    @classmethod
    def from_class(cls):
        return cls()
