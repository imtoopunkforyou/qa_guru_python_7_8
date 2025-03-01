"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product(
        name="book",
        price=100,
        description="This is a book",
        quantity=1000,
    )


@pytest.fixture
def product_2():
    return Product(
        name="milk",
        price=50,
        description="This is a milk",
        quantity=100,
    )


@pytest.fixture
def cart():
    return Cart()

class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(5000) is False
        assert product.check_quantity(1000)
        assert product.check_quantity(10)

    def test_product_buy(self, product):
        product.buy(10)
        assert product.quantity == 990


    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(100000)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    def test_add_product(self, product, cart):
        count_of_first = 10
        cart.add_product(product=product, buy_count=count_of_first)
        assert cart.products[product] == count_of_first
        count_of_second = 5
        cart.add_product(product=product, buy_count=count_of_second)
        assert cart.products[product] == count_of_first + count_of_second

    def test_remove_product(self, cart, product):
        ...

    def test_clear(self, product):
        ...

    def test_get_total_price(self, product):
        ...

    def test_buy(self, product):
        ...
