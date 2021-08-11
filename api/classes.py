from dataclasses import dataclass


@dataclass(frozen=True)
class Product:

    __slots__ = ['id', 'name', 'description', 'buy_url', 'image_url']
    id: int
    name: str
    description: str
    buy_url: str
    image_url: str

    @property
    def payload(self):
        return f'*{self.title}*\n\n{self.body}'
    
    @property
    def title(self):
        return self.name

    @property
    def body(self):
        return f'{self.description}\n\n*Buy:* {self.buy_url}'
