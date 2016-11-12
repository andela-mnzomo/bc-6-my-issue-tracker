import json
import nose
from flask_testing import TestCase
from app import db
from manage import app
from app.models import User, Issue
from config import config


class TestBase(TestCase):
    """ Base configurations for the tests """

    def create_app(self):
        """ Returns app """
        return app

    def setUp(self):
        """ Create test database and set up test client """
        db.create_all()
        user = User(username="testuser", password="testpassword")
        issue1 = Issue(subject="Leaking roof",
                                 description="Roof is leaking",
                                 user_id=1)
        issue2 = Issue(subject="Bullying at the office",
                                 description="lots of bullying",
                                 user_id=1)

        db.session.add(user)
        db.session.add(issue1)
        db.session.add(issue2)
        db.session.commit()

    def tearDown(self):
        """ Destroy test database """
        db.session.remove()
        db.drop_all()

if __name__ == "__main__":
    nose.run()
