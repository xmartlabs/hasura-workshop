import datetime
import uuid
from enum import Enum
from typing import Generic, TypeVar

from pydantic import BaseModel, conint, Field
from pydantic.generics import GenericModel



class HasuraActionRequest(BaseModel):
    request_query: str
    session_variables: dict
    action: dict


_Model = TypeVar('_Model')


class HasuraOperation(str, Enum):
    delete = 'DELETE'
    insert = 'INSERT'
    update = 'UPDATE'

class HasuraEventTriggerRequest(GenericModel, Generic[_Model]):
    event: dict
    created_at: datetime.datetime
    id: uuid.UUID
    delivery_info: dict
    table: dict
    trigger: dict
