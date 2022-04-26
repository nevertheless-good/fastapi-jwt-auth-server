import global_vars as _g

print(_g.access_token)

#def test_register(client):
#	user = dict(username="test@gmail.com", password="test")
#	res = client.post("register", json=user)
#	assert res.status_code == 201
	

#def test_again_register(client):
#	user = dict(username="test@gmail.com", password="test")
#	res = client.post("register", json=user)
#	res_body = res.json()
#	assert res.status_code == 400
#	assert "The E-Mail is already used" == res_body["detail"]


def test_login(client):
	user = dict(username="test@gmail.com", password="test")
	res = client.post("login", json=user)
	res_body = res.json()
	assert res.status_code == 200
	assert "access_token" in res_body.keys()
	_g.access_token = str(res_body["access_token"])
	assert "refresh_token" in res_body.keys()
	_g.refresh_token = str(res_body["refresh_token"])


def test_update_access_token(client):
	headers = {
        "Authorization": f"Bearer {_g.refresh_token}"
    }
	res = client.get("/update_token", headers=headers)
	res_body = res.json()
	assert res.status_code == 200
	assert "access_token" in res_body.keys()
	_g.access_token = str(res_body["access_token"])


def test_get_users(client):
	headers = {
		"Authorization": f"Bearer {_g.access_token}"
	}
	res = client.get("users", headers=headers)
	res_body = res.json()
	assert res.status_code == 200


