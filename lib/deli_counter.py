# lib/deli_counter.py

def line(katz_deli):
    if not katz_deli:
        return "The line is currently empty."
    else:
        line_message = "The line is currently:"
        for i, person in enumerate(katz_deli, start=1):
            line_message += f" {i}. {person}"
        return line_message

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    position = len(katz_deli)
    return f"Welcome, {name}. You are number {position} in line."

def now_serving(katz_deli):
    if not katz_deli:
        return "There is nobody waiting to be served!"
    else:
        serving = katz_deli.pop(0)
        return f"Currently serving {serving}."
