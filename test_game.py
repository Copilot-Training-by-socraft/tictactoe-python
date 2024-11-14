import pytest
from game import Game


@pytest.fixture
def game():
    return Game()


def test_not_allow_player_oto_play_first(game):
    with pytest.raises(Exception):
        game.play('O', 0, 0)


def test_not_allow_player_xto_play_twice_in_arow(game):
    with pytest.raises(Exception):
        game.play('X', 0, 0)
        game.play('X', 1, 0)


def test_not_allow_player_to_play_in_last_played_position(game):
    with pytest.raises(Exception):
        game.play('X', 0, 0)
        game.play('O', 0, 0)


def test_not_allow_player_to_play_in_any_played_position(game):
    with pytest.raises(Exception):
        game.play('X', 0, 0)
        game.play('O', 1, 0)
        game.play('X', 0, 0)


def test_declare_player_x_as_awinner_if_three_in_top_row(game):
    game.play('X', 0, 0)
    game.play('O', 1, 0)
    game.play('X', 0, 1)
    game.play('O', 1, 1)
    game.play('X', 0, 2)

    assert game.winner() == 'X'


def test_declare_player_o_as_awinner_if_three_in_top_row(game):
    game.play('X', 2, 2)
    game.play('O', 0, 0)
    game.play('X', 1, 0)
    game.play('O', 0, 1)
    game.play('X', 1, 1)
    game.play('O', 0, 2)

    assert game.winner() == 'O'


def test_declare_player_x_as_awinner_if_three_in_middle_row(game):
    game.play('X', 0, 0)
    game.play('O', 1, 0)
    game.play('X', 2, 0)
    game.play('O', 1, 1)
    game.play('X', 2, 1)
    game.play('O', 1, 2)

    assert game.winner() == 'O'


def test_declare_player_x_as_awinner_if_three_in_bottom_row(game):
    game.play('X', 2, 0)
    game.play('O', 0, 0)
    game.play('X', 2, 1)
    game.play('O', 0, 1)
    game.play('X', 2, 2)

    assert game.winner() == 'X'


def test_declare_player_o_as_awinner_if_three_in_bottom_row(game):
    game.play('X', 0, 0)
    game.play('O', 2, 0)
    game.play('X', 1, 0)
    game.play('O', 2, 1)
    game.play('X', 1, 1)
    game.play('O', 2, 2)

    assert game.winner() == 'O'