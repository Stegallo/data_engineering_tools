def greet(subject):
    return "hello " + subject


def say_hello():
    print(greet("world"))


def main():
    say_hello()


if __name__ == "__main__":
    main()
