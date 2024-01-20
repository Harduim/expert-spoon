from redis_om import HashModel, Field


class User(HashModel):
    first_name: str
    last_name: str
    email: str = Field(index=True)
    password: str
