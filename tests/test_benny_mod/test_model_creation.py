from typing import Optional

from pydantic import Json, UUID4

from sqlmodel import SQLModel, Field


class PiSrcBaseModel(SQLModel):
    pass


def test_model_creation():
    class TestBase(PiSrcBaseModel):
        data: Json = ...

    class TestDbSa(TestBase, table=True):
        id: Optional[UUID4] = Field(default=None, primary_key=True)

    class TestRead(TestBase):
        id: UUID4

    assert TestBase.__fields__["data"].required is True
    assert TestDbSa.__fields__["id"].required is False
    assert TestRead.__fields__["id"].required is True

    assert True