from langchain.prompts import PromptTemplate

template = """Convert the context into a tweet of up to 140 characters based on the context.

context:
{context}

Tweet in Spanish:
"""

TWEETS_PROMPT = PromptTemplate(
    template=template,
    input_variables=[
        "context",
    ],
)