from bson import ObjectId
from flask.testing import FlaskClient
import pytest
from src.app import app
from src.models.history_model import HistoryModel
from src.models.user_model import UserModel


@pytest.fixture
def app_test():
    return app.test_client()


def test_history_delete(app_test: FlaskClient):
    user_data = {"name": "admin", "token": "um token válido"}
    UserModel(user_data).save()

    history_data = {
        "text_to_translate": "Hello",
        "translate_from": "en",
        "translate_to": "pt",
    }
    history = HistoryModel(history_data)
    history.save()

    existing_history = HistoryModel.find_one({"_id": ObjectId(history.id)})
    assert (
        existing_history is not None
    ), "O histórico não existe antes da exclusão"

    response = app_test.delete(
        f"/admin/history/{history.id}",
        headers={
            "Authorization": user_data["token"],
            "User": user_data["name"],
        },
    )

    assert response.status_code == 204, "A exclusão do histórico falhou"

    deleted_history = HistoryModel.find_one({"_id": ObjectId(history.id)})
    assert deleted_history is None, "O histórico ainda existe após a exclusão"
