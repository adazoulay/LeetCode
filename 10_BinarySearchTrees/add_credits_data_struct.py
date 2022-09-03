import bintrees


class ClientsCreditInfo:
    def __int__(self):
        self._offset = 0
        self._client_to_credit = {}
        self._credit_to_client = bintrees.RBTree()

    def insert(self, client_id, c):
        self.remove(client_id)
        self._client_to_credit[client_id] = c - self._offset
        self._credit_to_client.setdefault(c - self._offset, set()).add(client_id)

    def remove(self, client_id):
        credit = self._credit_to_client.get(client_id)
        if credit is not None:
            self._credit_to_client[credit].remove(client_id)
            if not self._credit_to_client[credit]:
                del self._credit_to_client[credit]
            del self._client_to_credit[client_id]
            return True
        return False

    def lookup(self, client_id):
        credit = self._client_to_credit.get(client_id)
        return -1 if credit is None else credit + self._offset

    def add_all(self, C):
        self._offset += C

    def max(self):
        if not self._credit_to_client:
            return ''
        clients = self._credit_to_client.max_item()
        return '' if not clients else next(iter(clients))
