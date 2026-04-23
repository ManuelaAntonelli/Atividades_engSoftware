from abc import ABC, abstractmethod

class ChatMediator(ABC):
    @abstractmethod
    def send_message(self, message, user):
        pass

    @abstractmethod
    def add_user(self, user):
        pass

class ChatMediatorImpl(ChatMediator):
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def send_message(self, message, user):
        for u in self.users:
            if u != user:
                u.receive(message)

class User(ABC):
    def __init__(self, mediator, name):
        self.mediator = mediator
        self.name = name

    @abstractmethod
    def send(self, message):
        pass

    @abstractmethod
    def receive(self, message):
        pass

class UserImpl(User):
    def send(self, message):
        print(f"{self.name} enviou: {message}")
        self.mediator.send_message(message, self)

    def receive(self, message):
        print(f"{self.name} recebeu: {message}")

if __name__ == "__main__":
    chat = ChatMediatorImpl()

    u1 = UserImpl(chat, "Matheus")
    u2 = UserImpl(chat, "Jose")
    u3 = UserImpl(chat, "Manu")
    u4 = UserImpl(chat, "Ranny")

    chat.add_user(u1)
    chat.add_user(u2)
    chat.add_user(u3)
    chat.add_user(u4)

    u1.send("Salve")