from langchain.prompts import PromptTemplate

template = """Convert the context into 5 tweets based on the context.

context:
{context}

Tweets in Spanish:
"""

TWEETS_PROMPT = PromptTemplate(
    template=template,
    input_variables=[
        "context",
    ],
)