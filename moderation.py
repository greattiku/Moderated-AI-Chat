# moderation.py

BANNED_KEYWORDS = ["kill", "hack", "bomb", "terror", "murder"]

def contains_banned_words(text: str) -> bool:
    """Check if text contains any banned keywords."""
    text_lower = text.lower()
    return any(word in text_lower for word in BANNED_KEYWORDS)

def redact_banned_words(text: str) -> str:
    """Replace banned keywords with [REDACTED]."""
    result = text
    for word in BANNED_KEYWORDS:
        result = result.replace(word, "[REDACTED]")
    return result