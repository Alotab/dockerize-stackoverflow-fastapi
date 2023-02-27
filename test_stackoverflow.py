from soflogic.stackoverflow import search_tagged_questions, get_questions, search_users, fetch_users

# def test_get_question():
#     assert 'python' in get_questions('python')


def test_fetch_users():
    assert 'badge_counts' in fetch_users('Calvin')