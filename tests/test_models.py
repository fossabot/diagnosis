# -*- coding: utf-8 -*-
"""Model unit tests."""
import datetime as dt

import pytest

from mpharma.diagnosis.models import Category, Code
from mpharma.diagnosis.utils import create_code


@pytest.mark.usefixtures('db', 'app')
class TestCode:
    """Code tests."""

    def test_create_code(self, app):
        data = {
            "category_code": "A0",
            "diagnosis_code": 1234,
            "full_code": "A01234",
            "abbreviated_description": "Comma-ind anal ret",
            "full_description": "Comma-induced anal retention",
            "category_title": "Malignant neoplasm of anus and anal canal"
        }
        with app.app_context():
            created = create_code(**data)
            retrieved = Code.query.filter_by(full_code="A01234").first()
            assert created.category.code == "A0"
            assert created.full_code == "A01234"
            assert created.full_code == retrieved.full_code

        retrieved.delete()
