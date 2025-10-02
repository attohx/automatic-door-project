# heat_lamp_state.py

_state = "OFF"  # default

def get_state():
    global _state
    return _state

def set_state(new_state):
    global _state
    _state = new_state
