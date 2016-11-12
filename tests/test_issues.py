from app.models import User, Issue
from tests import TestBase


class TestIssues(TestBase):

    def test_user_count(self):
        """ Test that database works """
        self.assertEqual(User.query.count(), 1)

    def test_issue_count(self):
        self.assertEqual(Issue.query.count(), 2)
