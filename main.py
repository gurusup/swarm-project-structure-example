from configs.agents.types import *
from swarm.repl import run_demo_loop
from datetime import datetime

if __name__ == "__main__":
    run_demo_loop(triage_agent, debug=False)