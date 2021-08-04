import pytest
from flask import url_for

from app import app


# @pytest.fixture
# def client():
#     app = create_app()
#     return app.test_client()

def test_total():
    response = app.test_client().get("/total")
    assert response.status_code == 200
    assert response.data == b'{"total":50000005000000}\n'

def test_total2(): 
    response = app.test_client().get("/total2")
    assert response.status_code == 200
    with app.test_request_context(): 
        url_for("total2")