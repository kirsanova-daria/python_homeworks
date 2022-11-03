import json
import keyword


class ColorizeMixin:
    """ изменяет цвет текста при вызове print() """
    repr_color_code = 33

    def __repr__(self) -> str:
        text = f'{self.title} | {self.price} ₽'
        return f"\033[1;{self.repr_color_code};40m {text}  \n"


class Base:
    """ динамически создает аттрибуты для Advert """
    def __init__(self, attr: dict) -> None:
        for key, value in attr.items():
            if isinstance(value, dict):
                setattr(self, key, Base(value))
            else:
                if keyword.iskeyword(key):
                    setattr(self, f'{key}_', value)
                else:
                    setattr(self, key, value)

    def __repr__(self) -> str:
        return f'{self.title} | {self.price} ₽'


class Advert(ColorizeMixin, Base):
    def __init__(self, input: dict) -> None:
        self.input = input
        if 'title' not in input.keys():
            raise ValueError
        super().__init__(self.input)

    @property
    def price(self) -> int:
        if 'price' not in self.input.keys():
            return 0
        else:
            return self._price

    @price.setter
    def price(self, value: int) -> None:
        if value < 0:
            raise ValueError('price must be >= 0')
        self._price = value


if __name__ == '__main__':
    corgi_str = """{
                "title": "Вельш-корги",
                "class": "dogs",
                "location": {
                "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
                }
                }"""
    corgi = json.loads(corgi_str)
    corgi_ad = Advert(corgi)
    print(corgi_ad.location.address)
    print(corgi_ad.class_)
    print(corgi_ad.price)
    print(corgi_ad)
