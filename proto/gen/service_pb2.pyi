from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class StatusMessage(_message.Message):
    __slots__ = ("client_name", "command_name", "content")
    CLIENT_NAME_FIELD_NUMBER: _ClassVar[int]
    COMMAND_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    client_name: str
    command_name: str
    content: str
    def __init__(self, client_name: _Optional[str] = ..., command_name: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...

class StatusResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
