from pydantic import BaseModel, Field


class Market(BaseModel):
    id: int
    name: str


class Product(BaseModel):
    name: str
    price: float = Field(..., gt=0, description="Цена должна быть больше нуля")
    tags: list[str] = []
    market: Market


product_data = {
    "name": "Phone",
    "price": 499.99,
    "tags": ["electronics", "smartphones"],
    "market": {
        "id": 1,
        "name": "Amazon"
    }
}

product = Product(**product_data)
print(product.market.name)


new_product = Product(
    name="Phone",
    price=499.98,
    tags=["electronics", "smartphone"],
    market=Market(id=1, name="Amazpn")
)

print(new_product)