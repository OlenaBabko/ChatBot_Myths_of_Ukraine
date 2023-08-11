def back_button(property_func):
    def wrapper(self):
        base_value = property_func(self)
        return base_value + [["Назад"]]
    return wrapper