from abc import ABC, abstractmethod

from repository.any_of_repository import clientsRepository


class Abc(ABC):
    @abstractmethod
    async def get_client(self): pass

class clients(Abc):
    @classmethod
    def get_client(self):
        return clientsRepository().get_client()

