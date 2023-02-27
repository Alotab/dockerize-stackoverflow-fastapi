from soflogic.stackoverflow import fetch_users


def test_fetch_users():
    assert "badge_counts" in fetch_users("Calvin")
