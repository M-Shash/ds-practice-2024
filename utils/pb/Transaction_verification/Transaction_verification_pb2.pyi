from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TransactionVerificationRequest(_message.Message):
    __slots__ = ("cardID", "card_owner")
    CARDID_FIELD_NUMBER: _ClassVar[int]
    CARD_OWNER_FIELD_NUMBER: _ClassVar[int]
    cardID: str
    card_owner: str
    def __init__(self, cardID: _Optional[str] = ..., card_owner: _Optional[str] = ...) -> None: ...

class TransactionVerificationResponse(_message.Message):
    __slots__ = ("validationResult",)
    VALIDATIONRESULT_FIELD_NUMBER: _ClassVar[int]
    validationResult: bool
    def __init__(self, validationResult: bool = ...) -> None: ...
