from abc import ABC, abstractmethod, abstractclassmethod, abstractproperty, abstractstaticmethod
from fastapi import APIRouter
from redis_om import RedisModel
from dataclasses import dataclass
from pydantic import BaseModel


@dataclass
class BaseEntity(ABC):
    bind_model: type[RedisModel]
    view_model: type[BaseModel]

    @abstractproperty
    def router(self) -> APIRouter:
        ...

    @abstractclassmethod
    def get_all(cls) -> list[BaseModel]:
        ...

    @abstractclassmethod
    def create(cls, content: BaseModel) -> BaseModel:
        ...

    @abstractclassmethod
    def get(cls, key: str) -> BaseModel:
        ...

    @abstractclassmethod
    def update(cls, content: BaseModel) -> BaseModel:
        ...

    @abstractclassmethod
    def delete(cls, key: str) -> str:
        ...
