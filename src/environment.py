from typing import Callable

# A tool is just a function: (context: dict) -> str (the text the agent "sees" as tool output)
TOOL_REGISTRY: dict[str, Callable] = {}

def register_tool(name):
    def wrapper(fn):
        TOOL_REGISTRY[name] = fn
        return fn
    return wrapper

def run_tool(name: str, context: dict) -> str:
    return TOOL_REGISTRY[name](context)