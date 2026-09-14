import pathlib
import sys

PROJECT_DIR = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_DIR))

from chatbot import FALLBACK_RESPONSE, generate_response, normalize_input


def test_normalize_input_handles_case_and_whitespace():
    assert normalize_input("   HeLLo   ") == "hello"
    assert normalize_input("How   Are   You") == "how are you"


def test_known_intent_returns_response_without_exiting():
    response, should_exit = generate_response("hello")
    assert response != FALLBACK_RESPONSE
    assert should_exit is False


def test_unknown_intent_uses_fallback():
    response, should_exit = generate_response("tell me a joke")
    assert response == FALLBACK_RESPONSE
    assert should_exit is False


def test_exit_command_stops_chat():
    response, should_exit = generate_response(" EXIT ")
    assert response == "Goodbye."
    assert should_exit is True
