from src.error import InstantiateCSVError


def tests_init():
    err = InstantiateCSVError()
    assert err.message == "Файл item.csv поврежден"
    err1 = InstantiateCSVError("Тест")
    assert err1.message == "Тест"


def tests_str():
    err = InstantiateCSVError("TEST")
    assert str(err) == "TEST"
