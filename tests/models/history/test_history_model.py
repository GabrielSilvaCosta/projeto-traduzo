import json
from src.models.history_model import HistoryModel


def test_request_history():
    # Arrange
    list_history_json = HistoryModel.list_as_json()
    history_list = json.loads(list_history_json)

    # Act & Assert
    assert_is_string(list_history_json)
    assert_has_correct_number_of_items(history_list)
    assert_first_item_has_expected_text(history_list)


def assert_is_string(value):
    assert isinstance(value, str)


def assert_has_correct_number_of_items(history_list):
    assert len(history_list) == 2


def assert_first_item_has_expected_text(history_list):
    assert history_list[0]["text_to_translate"] == "Hello, I like videogame"
