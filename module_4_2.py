def test_function():
    def inner_function():
        print("Я в области видимости test_function")

    inner_function()


test_function()
# inner_function() при запуске данной функции вне функции test_function()
# появляется ошибка "name 'inner_function' is not defined"
