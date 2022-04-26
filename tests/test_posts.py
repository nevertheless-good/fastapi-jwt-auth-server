import global_vars as _g


def test_write_post(client):
	headers = {
        "Authorization": f"Bearer {_g.access_token}"
	}
	post = dict(title="title test", detail="detail test")
	res = client.post("/posts", json=post, headers=headers)
	assert res.status_code == 201


def test_get_posts(client):
	headers = {
        "Authorization": f"Bearer {_g.access_token}"
	}
	res = client.get("/posts/?start=0&limit=10&order=desc", headers=headers)
	assert res.status_code == 200
	res_body = res.json()
	assert "id" in res_body[0].keys()
	_g.test_index = str(res_body[0]["id"])


def test_my_posts(client):
	headers = {
        "Authorization": f"Bearer {_g.access_token}"
	}
	res = client.get("/posts", headers=headers)
	assert res.status_code == 200


def test_update_post(client):
	headers = {
        "Authorization": f"Bearer {_g.access_token}"
	}
	post = dict(title="title update", detail="detail update")
	res = client.put(f"/posts/{_g.test_index}", json=post, headers=headers)
	res_body = res.json()
	assert res.status_code == 200
	assert "title update" == res_body["title"]
	assert "detail update" == res_body["detail"]

def test_delete_post(client):
	headers = {
        "Authorization": f"Bearer {_g.access_token}"
	}
	res = client.delete(f"/posts/{_g.test_index}", headers=headers)
	res_body = res.json()
	assert res.status_code == 200
