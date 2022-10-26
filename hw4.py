import json
import keyword


class ColorizeMixin:
    def __repr__(self):
        text = super().__repr__()
        color = super().repr_color_code
        return f"\033[1;{color};40m {text}  \n"


class Advert(ColorizeMixin):
    repr_color_code = 33

    def __init__(self, input: dict):
        for key, value in input.items():
            if isinstance(value, dict):
                setattr(self, key, Advert(value))
            else:
                if key == 'price':
                    setattr(self, f'_{key}', value)
                    setattr(self, key, value)
                elif keyword.iskeyword(key):
                    setattr(self, f'{key}_', value)
                else:
                    setattr(self, key, value)

    @property
    def price(self):
        if '_price' not in self.__dict__.keys():
            return 0
        else:
            return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError('price must be >= 0')
        self._price = value

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'


if __name__ == '__main__':
    corgi_str = """{
                "title": "Вельш-корги",
                "price": 1000,
                "class": "dogs",
                "location": {
                "address": "сельское поселение Ельдигинское,
                поселок санатория Тишково, 25"
                }
                }"""
    corgi = json.loads(corgi_str)
    corgi_ad = Advert(corgi)
    print(corgi_ad.location.address)
    print(corgi_ad.class_)
    print(corgi_ad)
