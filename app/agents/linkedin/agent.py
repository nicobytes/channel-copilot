from __future__ import annotations

from functools import lru_cache
from uuid import uuid4

from deepagents import create_deep_agent
from deepagents.backends import FilesystemBackend

from agents.utils import extract_text_content


@lru_cache(maxsize=1)
def _build_linkedin_agent():
    return create_deep_agent(
        model="openai:gpt-5.4",
        memory=["./agents/linkedin/AGENTS.md"],
        backend=FilesystemBackend(root_dir=".", virtual_mode=True),
    )


def create_linkedin_post(content: str, language: str) -> str:
    agent = _build_linkedin_agent()
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": (
                        f"Rewrite and improve this content for a LinkedIn post in {language} "
                        f"for developers: {content}"
                    ),
                }
            ]
        },
        config={"configurable": {"thread_id": f"linkedin-{uuid4()}"}},
    )

    messages = result.get("messages", []) if isinstance(result, dict) else []
    if not messages:
        raise ValueError("Deep Agent did not return any message.")

    last_message = messages[-1]
    message_content = getattr(last_message, "content", None)
    if message_content is None and isinstance(last_message, dict):
        message_content = last_message.get("content")

    linkedin_post = extract_text_content(message_content)
    if not linkedin_post:
        raise ValueError("Deep Agent returned an empty LinkedIn post.")

    return linkedin_post
