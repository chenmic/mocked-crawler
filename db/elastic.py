from typing import Optional


class MockedElasticsearch:
    def __init__(self):
        self.__documents = {}

    def add(self, _id: str, data: str):
        self.__documents[_id] = data
        print(f"Added {data} with id {_id} to ES")

    def get(self, _id: str) -> Optional[dict]:
        try:
            return self.__documents[_id]
        except KeyError:
            return None
