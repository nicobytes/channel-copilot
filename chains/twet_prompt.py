from langchain.prompts import PromptTemplate
from langchain.prompts.chat import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate

system_template = """You are an assistant who can write a tweet based on the summary of the video. The summary should be written from the first-person perspective of Nicolas Molina, the owner of the tweet.

The generated tweet should be consistent with the summary, using emoticons and hashtags.
"""
system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)


human_template = """Create a twet in Spanish of the following summary.
summary:
{summary}
"""

human_template = PromptTemplate(
    template=human_template,
    input_variables=["summary"],
)

human_message_prompt = HumanMessagePromptTemplate(prompt=human_template)
TWET_PROMPT = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])