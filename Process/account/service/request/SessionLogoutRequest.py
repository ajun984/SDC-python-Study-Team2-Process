from dataclasses import dataclass

from account.entity.Account_Session import Account_Session


@dataclass
class SessionLogoutRequest:
    __accountSessionId: int

    def toSession(self):
        return Account_Session(self.__accountSessionId)

    def __init__(self, accountSessionId=None, **kwargs):
        if accountSessionId is not None:
            self.__accountSessionId = accountSessionId
        elif "__accountSessionId" in kwargs:
            self.__accountSessionId = kwargs["__accountSessionId"]

    @classmethod
    def createFromTuple(cls, inputTuple):
        return cls(*inputTuple)

    def getAccountSessionId(self):
        return self.__accountSessionId


