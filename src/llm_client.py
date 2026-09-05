import os
from dotenv import load_dotenv

load_dotenv()
PROVIDER = os.getenv("LLM_PROVIDER", "ollama")

def call_llm(messages: list[dict]) -> str:
    """messages: [{"role": "system"/"user"/"assistant", "content": str}, ...]
    Returns the model's text response."""
    if PROVIDER == "ollama":
        import ollama
        model = os.getenv("OLLAMA_MODEL", "llama3.1")
        response = ollama.chat(model=model, messages=messages)
        return response["message"]["content"]

    elif PROVIDER == "anthropic":
        import anthropic
        client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        system = next((m["content"] for m in messages if m["role"] == "system"), None)
        non_system = [m for m in messages if m["role"] != "system"]
        resp = client.messages.create(
            model="claude-sonnet-4-6",   # check console.anthropic.com for current model names
            max_tokens=500,
            system=system,
            messages=non_system,
        )
        return resp.content[0].text

    else:
        raise NotImplementedError(
            f"Add a branch for provider={PROVIDER} — check that provider's current SDK docs "
            f"for the exact chat-completion call signature before wiring it in."
        )