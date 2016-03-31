## Issue Tracker

__Issue Tracker__ is a web application written in Python using [Flask](http://flask.pocoo.org/ Flask's Homepage) for the Andela Kenya Class VI Bootcamp project. The application is a simple way to keep track of issues raised by people within an organization.

## Main Features

The application is able to:

- Allow users to register and login
- Allow users to raise an issue, specifying the issue subject, description, priority (low, medium, or high), and the department that is to handle the issue
- Allow users to view, edit, and delete their issues
- Allow admin users to view all issues
- Allow admin users to comment on issues
- Allow admin users to assign issues to another user for resolution
- Allow admin users to mark issues as resolved or in progress
- Allow users to receive notifications of any updates made to their issues by the admin

## Using Issue Tracker

You may view a live demonstration of __Issue Tracker__ on Heroku. You may register a new user account and login with the specified details. You may also login to the administrator account using the following credentials:

Email: admin@it.com
Password: cat2016

## Installation

You may also install the app on your local machine. 

__Prerequisites__
You should have a working installation of `Python 2.7` as well as `pip`. It is recommended that you use a virtual environment for this project.

To install the app:

1. Clone this repository
`git clone https://github.com/mbithe/bc-6-my-issue-tracker`

2. Install requirements
`pip install -r req.txt`

3. Run the server
`python manage.py runserver`

## Workflow

__Non-administrative Users__

Non-administrative users must register and login to use the application. Once logged in, they can raise an `issue`. They can `view`, `edit`, and `delete` their issues. They can also receive `notifications` when the status of an issue changes (that is, when it is marked as `in-progress` or `resolved`). The `dashboard` shows a summary of their issues and notifications.

__Administrative Users__

Administrative users can view all `issues` raised by all users. They can mark issues as `resolved` or `assign` issues to users. Assignment of issues automatically marks them as `in-progress`. Admin users can also `comment` on issues.

Admin users can also add `departments`, which are the departments to which issues are assigned (such as Operations, Training, and Human Resources). They can also specify `department heads` for each department. Admin users can `view`, `edit`, and `delete` departments. 

## Recommendations

The following recommendations would improve the application:

- User profiles, with profile pictures and brief biographies for each user
- Pushing of notifications as a popup rather than rendering them in a list on the notifications page
