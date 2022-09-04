from abc import abstractmethod


class ManageDB:

    @abstractmethod
    def create_client(self):
        pass

    @abstractmethod
    def close_client(self):
        pass

    @abstractmethod
    def retrieve_client(self):
        pass

    @abstractmethod
    def db_name(self):
        pass
