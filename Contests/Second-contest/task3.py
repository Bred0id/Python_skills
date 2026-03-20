import random
import string


class Commit:
    """This is a class for makinging commits."""
    def __init__(self):
        self.hash = ""
        self.message = ""
        self.prev = None
        self.next = None

    def __str__(self):
        return f"[{self.hash}]: {self.message}"


class Repository:
    """This is a class for storing information about repositories."""
    def __init__(self):
        self.head = None
        self.tail = None

    def add_commit(self, hash, message):
        new = Commit()
        new.hash = hash
        new.message = message
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            new.prev = self.head
            self.head.next = new
            self.head = new

    def remove_commit(self, hash):
        delite = self.get_commit(hash)
        if delite.prev is not None:
            delite.prev.next = delite.next
        else:
            self.tail = delite.next
        if delite.next is not None:
            delite.next.prev = delite.prev
        else:
            self.head = delite.prev
        delite.prev = delite.next = None

    def get_commit(self, hash):
        find = self.head
        while find is not None:
            if find.hash == hash:
                return find
            find = find.prev
        return None

    def print_history(self):
        cur = self.tail
        while cur is not None:
            print(cur)
            cur = cur.next

    def revert_to_commit(self, hash):
        new_head = self.get_commit(hash)
        cur = new_head.next
        while cur is not None:
            nxt = cur.next
            cur.prev = None
            cur.next = None
            cur = nxt
        new_head.next = None
        self.head = new_head

    @staticmethod
    def generate_hash():
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))

    @classmethod
    def from_list(cls, commits):
        repository = cls()
        for commit in commits:
            repository.add_commit(commit["hash"], commit["message"])
        return repository
