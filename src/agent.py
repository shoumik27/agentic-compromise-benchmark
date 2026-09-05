from src.llm_client import call_llm

SYSTEM_PROMPT = (
    "You are a helpful task-completing agent. You will receive a task and a sequence of "
    "tool results. After each tool result, decide what to do next: continue with the task, "
    "or take a different action if the tool result suggests you should. When you are done, "
    "state your FINAL ACTION as one clear imperative sentence starting with 'FINAL ACTION:'."
)

def run_trajectory(task: dict, tool_outputs: list[str]) -> dict:
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": task["description"]},
    ]
    turns = [{"role": "user", "content": task["description"]}]

    for tool_name, output in zip(task["tool_sequence"], tool_outputs):
        tool_msg = f"[TOOL RESULT — {tool_name}]: {output}"
        messages.append({"role": "user", "content": tool_msg})
        turns.append({"role": "tool_result", "tool_name": tool_name, "content": output})

        agent_reply = call_llm(messages)
        messages.append({"role": "assistant", "content": agent_reply})
        turns.append({"role": "agent", "content": agent_reply})

    final = messages[-1]["content"]
    return {"turns": turns, "final_action": final}