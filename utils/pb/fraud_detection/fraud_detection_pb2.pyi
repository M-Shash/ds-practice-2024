from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class f_detectionRequest(_message.Message):
    __slots__ = ("name", "id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: int
    def __init__(self, name: _Optional[str] = ..., id: _Optional[int] = ...) -> None: ...

class f_detectionResponse(_message.Message):
    __slots__ = ("fraudResult",)
    FRAUDRESULT_FIELD_NUMBER: _ClassVar[int]
    fraudResult: bool
    def __init__(self, fraudResult: bool = ...) -> None: ...
