from agents import Agent
from .tools import (
    extract_text_from_image,
    detect_language,
    translate_to_english,
    explain_quebec_context
)

sign_agent = Agent(
    name="Sign Interpreter Agent",
    instructions="""
    You are an intelligent sign interpretation agent.
    Your job:
    1. Extract text from the image.
    2. Detect the language.
    3. Translate to English.
    4. Explain Quebec-specific context if relevant.
    
    Return structured JSON:
    {
        "original_text": "...",
        "language": "...",
        "translation": "...",
        "context": "..."
    }
    """,
    tools=[
        extract_text_from_image,
        detect_language,
        translate_to_english,
        explain_quebec_context
    ]
)
