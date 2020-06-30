# map-api

## Overview

### GET

#### Game state of a baord

`curl http://<host>/v0/get-board?board_id=1`

Used when you wish to retrive the state of any given board.

**Response**

``` json
[
    {
    "hex_id": 111,
    "player_id": 1,
    "tokens": 5,
    "x": 0, 
    "y": 0,
    "neighbors": [112, 113],
    "playable": 1,
    },
    {
    "hex_id": 112,
    "player_id": 2,
    "tokens": 7,
    "x": 0,
    "y": 1,
    "neighbors": [111, 113],
    "playable": 1,
    },
    {
    "hex_id": 113,
    "player_id": null,
    "tokens": 0,
    "x": 1,
    "y": 0,
    "neighbors": [112, 111],
    "playable": 0,
    }
]
```

## Development

Test against your local `MySQL` instance. See the `game-database` repository
for latest database schema and test data. The username and password needed for
you database is in the `Makefile`. Don't forget to give your database user full
privileges or you may have trouble running the tests.

## Docker

> docker build -t board-api .

You only need to build this image if you are working on the `game-service`
repository.
