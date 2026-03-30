from datetime import datetime

from agents import function_tool


@function_tool
def get_current_time() -> str:
    """
    Return the current local date and time as a formatted string.
    Use this tool when the user asks for the current time or date.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")