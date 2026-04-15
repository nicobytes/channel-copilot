from __future__ import annotations

from functools import lru_cache
from uuid import uuid4

from deepagents import create_deep_agent
from deepagents.backends import FilesystemBackend
from agents.utils import extract_text_content


@lru_cache(maxsize=1)
def _build_summarizer_agent():
    return create_deep_agent(
        model="openai:gpt-5.4",
        memory=["./agents/summarize/AGENTS.md"],
        backend=FilesystemBackend(root_dir=".", virtual_mode=True),
    )


def summarize_transcript(transcript: str) -> str:
    agent = _build_summarizer_agent()
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": f"Provide a summary of the following transcript: {transcript}",
                }
            ]
        },
        config={"configurable": {"thread_id": f"summary-{uuid4()}"}},
    )

    messages = result.get("messages", []) if isinstance(result, dict) else []
    if not messages:
        raise ValueError("Deep Agent did not return any message.")

    last_message = messages[-1]
    content = getattr(last_message, "content", None)
    if content is None and isinstance(last_message, dict):
        content = last_message.get("content")

    summary = extract_text_content(content)
    if not summary:
        raise ValueError("Deep Agent returned an empty summary.")

    return summary
