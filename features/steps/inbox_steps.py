from behave import *
from nose.tools import assert_equal, assert_true


# if title is 'Inbox' then user is on the inbox page
@step('user is on the inbox page')
def step_impl(context):
    assert_equal(context.inbox_page.get_page_title(), 'Gmail')


# execute login steps again
@given('user successfully logs in with valid '
       'username "{username}" and '
       'valid password "{password}" and '
       'is on the inbox page')
def step_impl(context, username, password):
    context.execute_steps(u'''given user is on the login page''')
    context.login_page.login(username, password)


@step('user composes a message with '
      'recipient "{recipient}" and '
      'subject "{subject}" and '
      'message "{message}"')
def step_impl(context, recipient, subject, message):
    context.inbox_page.compose_message(recipient, subject, message)


@step('user sends message')
def step_impl(context):
    context.inbox_page.send_message()


@step('the message is sent successfully')
def step_impl(context):
    context.inbox_page.open_message()


@when('user deletes the message')
def step_impl(context):
    context.inbox_page.delete_message()


@then('the message is successfully deleted')
def step_impl(context):
    assert_true(context.inbox_page.delete_success)



