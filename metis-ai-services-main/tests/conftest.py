"""Global pytest fixtures."""
import pytest

from metis_ai_services import create_app
from metis_ai_services import db as database
from metis_ai_services.models.user import User
from tests.util import EMAIL, ADMIN_EMAIL, PASSWORD


@pytest.fixture
def app():
    app = create_app("testing")
    return app


@pytest.fixture
def db(app, client, request):
    database.drop_all()
    database.create_all()
    database.session.commit()

    def fin():
        database.session.remove()

    request.addfinalizer(fin)
    return database


@pytest.fixture
def user(db):
    user = User(email=EMAIL, password=PASSWORD)
    db.session.add(user)
    db.session.commit()
    return user


@pytest.fixture
def admin(db):
    admin = User(email=ADMIN_EMAIL, password=PASSWORD, admin=True)
    db.session.add(admin)
    db.session.commit()
    return admin