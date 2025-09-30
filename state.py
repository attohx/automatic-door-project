# state.py

# This module manages the state of the poultry gate system.
gate_state = {
    "status": "CLOSED"   # possible values: "OPEN", "CLOSED"
}

def set_state(new_state):
    gate_state["status"] = new_state

def get_state():
    return gate_state["status"]
