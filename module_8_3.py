class IncorrectVinNumber(Exception):
    '''Исключение ввода неверного вин кода автомобиля'''
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    '''Исключение ввода неверного номера автомобиля'''
    def __init__(self, message):
        self.message = message




class Car:
    def __init__(self, model: str, vin: int, number: str):
        self.model = model
        self.__vin = vin
        self.__number = number
        self.__is_valid_vin(vin)
        self.__is_valid_number(number)

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if not 1000000 <= vin_number <= 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        self.__vin = vin_number
        return True



    def __is_valid_number(self, number):
        if not isinstance(number, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(number) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        self.__number = number
        return True

if __name__ == '__main__':
    try:
        first = Car('Model1', 1000000, '3df12j')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{first.model} успешно создан')

    try:
        second = Car('Model2', 300, 'т001тр')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{second.model} успешно создан')

    try:
        third = Car('Model3', 2020202, 'нет номера')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{third.model} успешно создан')
