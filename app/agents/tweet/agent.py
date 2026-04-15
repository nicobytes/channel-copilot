from __future__ import annotations

from functools import lru_cache
from uuid import uuid4

from deepagents import create_deep_agent
from deepagents.backends import FilesystemBackend
from agents.utils import extract_text_content


@lru_cache(maxsize=1)
def _build_tweet_agent():
    return create_deep_agent(
        model="openai:gpt-5.4",
        memory=["./agents/tweet/AGENTS.md"],
        backend=FilesystemBackend(root_dir=".", virtual_mode=True),
    )


def create_tweet(content: str, language: str, target: str, link: str) -> str:
    agent = _build_tweet_agent()
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": (
                        f"Create an improved tweet in {language} for {target}. "
                        f"Include this link if relevant: {link}. "
                        f"Base tweet content: {content}"
                    ),
                }
            ]
        },
        config={"configurable": {"thread_id": f"tweet-{uuid4()}"}},
    )

    messages = result.get("messages", []) if isinstance(result, dict) else []
    if not messages:
        raise ValueError("Deep Agent did not return any message.")

    last_message = messages[-1]
    message_content = getattr(last_message, "content", None)
    if message_content is None and isinstance(last_message, dict):
        message_content = last_message.get("content")

    tweet = extract_text_content(message_content)
    if not tweet:
        raise ValueError("Deep Agent returned an empty tweet.")

    return tweet
