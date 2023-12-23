# lib/testing/test_deli_counter.py
from deli_counter import line, take_a_number, now_serving

def test_line_empty():
    katz_deli = []
    assert line(katz_deli) == "The line is currently empty."

def test_take_a_number():
    katz_deli = []
    assert take_a_number(katz_deli, "Ada") == "Welcome, Ada. You are number 1 in line."
    assert take_a_number(katz_deli, "Grace") == "Welcome, Grace. You are number 2 in line."
    assert take_a_number(katz_deli, "Kent") == "Welcome, Kent. You are number 3 in line."

def test_line_after_take_a_number():
    katz_deli = ["Ada", "Grace", "Kent"]
    assert line(katz_deli) == "The line is currently: 1. Ada 2. Grace 3. Kent"

def test_now_serving():
    katz_deli = ["Ada", "Grace", "Kent"]
    assert now_serving(katz_deli) == "Currently serving Ada."
    assert line(katz_deli) == "The line is currently: 1. Grace 2. Kent"

def test_take_a_number_after_serving():
    katz_deli = ["Grace", "Kent"]
    assert take_a_number(katz_deli, "Matz") == "Welcome, Matz. You are number 3 in line."
    assert line(katz_deli) == "The line is currently: 1. Grace 2. Kent 3. Matz"

def test_now_serving_after_take_a_number():
    katz_deli = ["Grace", "Kent", "Matz"]
    assert now_serving(katz_deli) == "Currently serving Grace."
    assert line(katz_deli) == "The line is currently: 1. Kent 2. Matz"
