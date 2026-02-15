from agents import tool


@tool
def extract_text_from_image(image_bytes: bytes) -> str:
    """
    Extract visible text from an image using OCR.
    """
    return "Texte exemple en français"


@tool
def detect_language(text: str) -> str:
    """
    Detect the language of the extracted text.
    """
    return "French"


@tool
def translate_to_english(text: str) -> str:
    """
    Translate given text into English.
    """
    return "Sample text in English"


@tool
def explain_quebec_context(text: str) -> str:
    """
    Explain cultural or legal context of the sign in Quebec.
    """
    return "This type of sign is common in Quebec due to language laws."
