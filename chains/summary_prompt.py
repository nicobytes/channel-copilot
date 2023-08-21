from langchain.prompts import PromptTemplate
from langchain.prompts.chat import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate

system_template = """You are an assistant who can write a summary in 5 paragraphs for a YouTube channel, given the transcript of the video, the summary will be used to create online content on social media. The summary should be written from the first-person perspective of Nicolas Molina, the owner of the YouTube channel."""
system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)


human_template = """Provide a summary in Spanish of the following transcript. 
transcript:
{transcript}
"""

human_template = PromptTemplate(
    template=human_template,
    input_variables=["transcript"],
)

human_message_prompt = HumanMessagePromptTemplate(prompt=human_template)
SUMMARY_PROMPT = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])