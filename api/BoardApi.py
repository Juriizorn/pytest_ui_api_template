import requests


class BoardApi:

    def __init__(self, base_url, api_key, token, org_id):
        self.base_url = base_url
        self.api_key = api_key
        self.token = token
        self.org_id = org_id

    def get_all_boards_by_org_id(self) -> dict:
        get_board = ("{trello}/organizations/{id}/boards?key="
                     "{key}&token={token}".format
                     (trello=self.base_url, id=self.org_id,
                      key=self.api_key, token=self.token))

        resp = requests.get(get_board)
        return resp.json()

    def create_board(self, name_board):

        create_board = ("{trello}/boards/?name={name}&key={key}"
                        "&token={token}".format
                        (trello=self.base_url, name=name_board,
                         key=self.api_key, token=self.token))
        resp = requests.post(create_board)
        return resp.json()

    def delete_board(self, board_id):
        delete_board = ("{trello}/boards/{id}?key={key}&token={token}"
                        .format(trello=self.base_url, id=board_id,
                                key=self.api_key, token=self.token))
        resp = requests.delete(delete_board)
        return resp.json()
