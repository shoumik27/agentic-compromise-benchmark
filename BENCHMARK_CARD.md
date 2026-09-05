# Agentic Compromise Benchmark — Benchmark Card

## Purpose
This benchmark tests whether an LLM-based agent can be manipulated by adversarial content embedded in tool outputs. It covers prompt injection via tools, memory poisoning, cross-agent handoff poisoning, rug-pull style tool behavior changes, and tool scope escalation.

## Motivation
Modern agent systems increasingly rely on external tools and multi-agent coordination. Recent research and disclosed attacks have shown that malicious content inside tool results can cause agents to take unsafe actions (data exfiltration, unauthorized sharing, destructive operations, etc.). This dataset provides labeled trajectories that map directly onto deception detection and unsafe agent action evaluation categories.

## Categories
- **mcp_prompt_injection**: Malicious instructions hidden inside otherwise normal tool results.
- **memory_poisoning**: Persistent false context injected into an earlier “memory” or notes tool.
- **cross_agent_context_poisoning**: Poisoned handoff message from one agent to another.
- **mcp_rug_pull**: Tool behaves normally at first, then suddenly changes to a malicious instruction.
- **tool_scope_escalation**: Tool output politely asks the agent to perform an action outside the original task scope.
- **clean**: Control trajectories with no attack.

## Dataset Statistics
- Total trajectories: 24
- Categories: 6 (5 attack types + clean)
- Agent model: llama3.1:8b (via Ollama)
- Labeling: Automated checker (improved) + full manual review of attack trajectories

### Final compromise rates (after correction)
| Category                        | Compromise Rate |
|---------------------------------|-----------------|
| clean                           | 0.00            |
| mcp_prompt_injection            | 1.00            |
| mcp_rug_pull                    | 0.75            |
| memory_poisoning                | 0.50            |
| tool_scope_escalation           | 0.50            |
| cross_agent_context_poisoning   | 0.00            |

## Labeling Methodology & Important Correction
The initial automated checker searched the entire trajectory text (including tool_result turns). Because the attack payload itself contains the target string, this produced many false positives — the checker was detecting the presence of the payload rather than actual agent compliance.

The checker was corrected to only inspect the agent’s own turns (`role == "agent"`). All attack trajectories were then manually re-reviewed. Four clear false positives were identified and corrected. The rates above reflect the corrected labels.

This process (finding that the metric was not measuring the intended construct, fixing it, and documenting the change) is itself a core part of the evaluation work this benchmark is meant to support.

## Limitations
- Fully synthetic and sandboxed — no real MCP servers or external systems were contacted.
- Small scale (N=24). Suitable as a development / pilot set rather than a large evaluation set.
- Single primary labeler.
- Agent behavior is specific to `llama3.1:8b`. Results will differ with stronger or weaker models.
- The automated checker uses string matching on the agent’s output and can still miss paraphrased compliance.

## Ethics
All attacks were executed against a completely local, simulated environment built for this project. No real user data, external services, or third-party systems were involved.