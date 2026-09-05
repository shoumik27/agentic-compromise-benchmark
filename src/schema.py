from dataclasses import dataclass, field, asdict
from typing import Literal, Optional
import json
import time

AttackCategory = Literal[
    "mcp_prompt_injection",
    "memory_poisoning",
    "cross_agent_context_poisoning",
    "mcp_rug_pull",
    "tool_scope_escalation",
    "clean",  # no attack — control group
]

Severity = Literal["none", "low", "medium", "high"]

@dataclass
class Turn:
    role: str            # "system" | "user" | "tool_result" | "agent"
    tool_name: Optional[str] = None
    content: str = ""

@dataclass
class Trajectory:
    id: str
    category: AttackCategory
    task_id: str
    task_description: str
    attack_payload: Optional[str]        # None for clean trajectories
    turns: list                          # list of Turn (as dicts)
    final_action: str                    # the agent's stated final action
    compromised: bool                    # ground-truth label
    severity: Severity
    rationale: str                       # why it's labeled this way
    labeler: str                         # "auto_checker" or your name
    label_method: str                    # "automated" or "manual_review"
    created_at: float = field(default_factory=time.time)

    def to_json(self) -> str:
        return json.dumps(asdict(self), ensure_ascii=False)