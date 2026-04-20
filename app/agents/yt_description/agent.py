from __future__ import annotations

from functools import lru_cache
from uuid import uuid4

from agents.utils import extract_text_content
from deepagents import create_deep_agent
from deepagents.backends import FilesystemBackend


@lru_cache(maxsize=1)
def _build_yt_description_agent():
    return create_deep_agent(
        model="openai:gpt-5.4",
        memory=["./agents/yt_description/AGENTS.md"],
        backend=FilesystemBackend(root_dir=".", virtual_mode=True),
    )


def create_description(content: str, language: str) -> str:
    agent = _build_yt_description_agent()
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": (
                        "Create the description and tags in "
                        f"{language} based on this summary: {content}"
                    ),
                }
            ]
        },
        config={"configurable": {"thread_id": f"yt-description-{uuid4()}"}},
    )

    messages = result.get("messages", []) if isinstance(result, dict) else []
    if not messages:
        raise ValueError("Deep Agent did not return any message.")

    last_message = messages[-1]
    message_content = getattr(last_message, "content", None)
    if message_content is None and isinstance(last_message, dict):
        message_content = last_message.get("content")

    description = extract_text_content(message_content)
    if not description:
        raise ValueError("Deep Agent returned empty description and tags.")

    return description
