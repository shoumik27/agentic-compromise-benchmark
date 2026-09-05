# Agentic Compromise Benchmark

A labeled dataset of clean and attacker-compromised agent trajectories for evaluating deception detection and unsafe agent behavior.

## Quickstart

```bash
# 1. Create and activate environment
python -m venv venv
# Windows
.\venv\Scripts\Activate.ps1
# Linux/Mac
source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment
cp .env.example .env
# Edit .env and set OLLAMA_MODEL=llama3.1:8b (or your preferred model)

# 4. Generate trajectories
python -m src.run_generation