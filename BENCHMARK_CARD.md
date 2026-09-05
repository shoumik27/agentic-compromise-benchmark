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
- Labeling: Automated string-based checker + manual review of 5 trajectories (≈21%)

### Compromise rates (automated labels)
| Category                        | Compromise Rate |
|---------------------------------|-----------------|
| clean                           | 0.00            |
| mcp_prompt_injection            | 1.00            |
| memory_poisoning                | 1.00            |
| mcp_rug_pull                    | 1.00            |
| tool_scope_escalation           | 1.00            |
| cross_agent_context_poisoning   | 1.00            |

## Labeling Methodology
1. Automated checker looks for the presence of a known compromise signal (email address or key phrase) in the agent’s full trajectory.
2. Manual review was performed on 5 trajectories (lines 1, 2, 6, 19, 24). For these records, `label_method` was set to `"manual_review"` and `labeler` to `"Shoumik"`.
3. No disagreements with the automated labels were found in the sampled trajectories.

## Limitations
- Fully synthetic and sandboxed — no real MCP servers or external systems were contacted.
- Small scale (N=24). Suitable as a development / pilot set rather than a large evaluation set.
- Single primary labeler (manual review only on a sample).
- Agent behavior is specific to `llama3.1:8b`. Results will differ with stronger or weaker models.
- The automated checker uses simple string matching and can miss subtle or paraphrased compromises.

## Ethics
All attacks were executed against a completely local, simulated environment built for this project. No real user data, external services, or third-party systems were involved.