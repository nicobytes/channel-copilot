from langchain.prompts import PromptTemplate
from langchain.prompts.chat import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate

system_template = """You are a helpful large language model that generates DALL-E prompts, that when given to the DALL-E model can generate beautiful high-quality images to use in social media posts about a YouTube Channel on technology.  Good DALL-E prompts will contain mention of related objects, and will not contain people or words.  Good DALL-E prompts should include a references about the topic."""
system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)


human_template = PromptTemplate(
    template="Create a DALL-E prompt per each paragraph to create an image, the following are the paragraphs: {text}",
    input_variables=["text"],
)

human_message_prompt = HumanMessagePromptTemplate(prompt=human_template)
DALLE_PROMPT = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])