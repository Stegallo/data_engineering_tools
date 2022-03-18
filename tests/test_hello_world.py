from data_engineering_tools.hello_world import greet, main, say_hello


def test_greet():
    assert greet("") == "hello "
    assert greet("Alice") == "hello Alice"


def test_say_hello():
    say_hello()


def test_main():
    main()
