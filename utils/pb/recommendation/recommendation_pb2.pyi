from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RecommendationRequest(_message.Message):
    __slots__ = ("userName", "itemName")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    ITEMNAME_FIELD_NUMBER: _ClassVar[int]
    userName: str
    itemName: str
    def __init__(self, userName: _Optional[str] = ..., itemName: _Optional[str] = ...) -> None: ...

class RecommendationResponse(_message.Message):
    __slots__ = ("recommendations",)
    RECOMMENDATIONS_FIELD_NUMBER: _ClassVar[int]
    recommendations: _containers.RepeatedCompositeFieldContainer[RecommendationItem]
    def __init__(self, recommendations: _Optional[_Iterable[_Union[RecommendationItem, _Mapping]]] = ...) -> None: ...

class RecommendationItem(_message.Message):
    __slots__ = ("itemId", "itemName")
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    ITEMNAME_FIELD_NUMBER: _ClassVar[int]
    itemId: str
    itemName: str
    def __init__(self, itemId: _Optional[str] = ..., itemName: _Optional[str] = ...) -> None: ...
