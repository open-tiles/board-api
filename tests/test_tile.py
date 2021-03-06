import json
import models.tile


class FakeURL:

    def __init__(self, queries={}):
        self.query = queries


class FakeRequest:

    def __init__(self, _raise_exception=False, _json=None, app=None, url=None):
        self._json = _json
        self._raise_exception = _raise_exception
        self.app = app or {}
        self.rel_url = url

    async def json(self):
        if self._raise_exception:
            json.loads('None')
        return self._json


async def test_is_connected(pool):
    connected_url = FakeURL(queries={
        "from": '5',
        "to": '2'
        })
    request = FakeRequest(app={'pool': pool}, url=connected_url)
    connected_response = await models.tile.is_connected(request)
    connected_actual = json.loads(connected_response.text)
    assert {"Connection": True} == connected_actual

    not_connected_url = FakeURL(queries={
        "from": 5,
        "to": 2
        })
    not_connected_request = FakeRequest(
            app={'pool': pool},
            url=not_connected_url
            )
    not_connected_response = await models.tile.is_connected(
            not_connected_request
            )
    not_connected_actual = json.loads(not_connected_response.text)
    assert {"Connection": True} == not_connected_actual


async def test_get_edges(pool):
    tile_id = 5
    edges = await models.tile.tile_edges(pool, tile_id)
    assert edges == [2, 3, 4, 6, 8, 9]


async def test_get_tile(pool):
    connected_url = FakeURL(
            queries={
                "id": 2
                })
    request = FakeRequest(app={'pool': pool}, url=connected_url)
    response = await models.tile.get_tile(request)
    actual = json.loads(response.text)
    expected = {
            "id": 2,
            "owner": 1,
            "tokens": 5,
            "x": 0,
            "y": 1,
            "playable": 1,
            "edges": [3, 4, 5]
            }
    assert expected == actual


async def test_change_ownership(pool):
    data = {
            "tokens": 500,
            "tile_id": 1
            }
    request = FakeRequest(app={"pool": pool}, _json=data)
    response = await models.tile.update_tokens(request)
    actual = json.loads(response.text)
    expected = {'Result': 'Updated tile-id 1'}
    assert expected == actual
