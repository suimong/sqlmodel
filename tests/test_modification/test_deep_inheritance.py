from typing import Optional

from pydantic import Json, UUID4

from sqlmodel import SQLModel, Field


class PiSrcBaseModel(SQLModel):
    pass


class TestBase(PiSrcBaseModel):
    data: Json


class TestDbSa(PiSrcBaseModel, table=True):
    id: Optional[UUID4] = Field(default=None, primary_key=True)


class TestDbNoSa(PiSrcBaseModel):
    id: Optional[UUID4] = Field(default=None, primary_key=True)


def test_inherit_model_creation():
    assert True