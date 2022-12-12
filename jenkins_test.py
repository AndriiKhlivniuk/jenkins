from jenkins import get_users

def test_users_page():
	assert 2 == get_users()["page"]

def test_users_per_page():
	assert 6 == get_users()["per_page"]

def test_users_total():
	assert 12 == get_users()["total"]