from __future__ import annotations
from abc import ABC, abstractmethod
from telebot.types import CallbackQuery, Message


class Context(ABC):
    """
    The Context defines the interface of interest to clients. It also maintains
    a reference to an instance of a State subclass, which represents the current
    state of the Context.
    """

    _state = None
    """
    A reference to the current state of the Context.
    """

    def __init__(self, tg_id, state: State) -> None:
        self.tg_id = tg_id
        self.transition_to(state)

    def transition_to(self, state: State):
        """
        The Context allows changing the State object at runtime.
        """

        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.user = self

    """
    The Context delegates part of its behavior to the current State object.
    """

    def button_request(self, call):
        self._state.handle_button(call)

    def text_request(self, msg):
        self._state.handle_text(msg)


class State(ABC):

    @property
    def user(self) -> Context:
        return self._user

    @user.setter
    def user(self, user: Context) -> None:
        self._user = user

    @abstractmethod
    def handle_button(self, call) -> None:
        pass

    @abstractmethod
    def handle_text(self, msg: Message) -> None:
        pass
