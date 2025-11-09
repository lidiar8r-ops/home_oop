import pytest
import os

from src.product import Product


def test_product(protuct_one):
    assert protuct_one.name == "Samsung Galaxy S23 Ultra"
    assert protuct_one.description == "256GB, Серый цвет, 200MP камера"
    assert protuct_one.price == 180000.0
    assert protuct_one.quantity == 5
