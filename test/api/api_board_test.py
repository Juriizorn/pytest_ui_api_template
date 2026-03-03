from api.BoardApi import BoardApi


def test_get_boards(base_url: str, org_id: str, api_key: str, token: str):
    api = BoardApi(base_url, api_key, token, org_id)
    board_list = api.get_all_boards_by_org_id()

    assert board_list[1]["name"] == "Четвертая доска"


def test_create_board(base_url: str, org_id: str, api_key: str, token: str):
    name_board = "Четвертая доска"
    api = BoardApi(base_url, api_key, token, org_id)
    board_list_before = api.get_all_boards_by_org_id()
    api.create_board(name_board)
    board_list_after = api.get_all_boards_by_org_id()

    assert len(board_list_before) - len(board_list_after) == -1


def test_delete_board(base_url: str, org_id: str, api_key: str, token: str):
    name_board = "Четвертая доска"
    api = BoardApi(base_url, api_key, token, org_id)
    api.create_board(name_board)
    board_list_before = api.get_all_boards_by_org_id()
    new_id = board_list_before[-1]["id"]
    api.delete_board(new_id)
    board_list_after = api.get_all_boards_by_org_id()

    assert board_list_before[-1]["id"] != board_list_after[-1]["id"]
