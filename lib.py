def cashback(monthly_expenses): # объявление + указание параметров
    # отступ обязателен
    """
    >>> cashback(10_000)
    300.0
    :param monthly_expenses:
    :return:
    """
    percent = 3
    result = percent * monthly_expenses / 100
    return result # возврат значения



def Body_mass_index(weight, height): # объявление + указание параметров
    # отступ обязателен
    """
    >>> Body_mass_index (106, 1.68) #doctest: +ELLIPSIS
    37.55...
    """
    index = weight / (height * height )
    return index

