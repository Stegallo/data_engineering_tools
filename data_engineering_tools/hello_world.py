def greet(subject: str) -> str:
    return "hello " + subject


def say_hello() -> None:
    print(greet("world"))


def main() -> None:
    say_hello()


if __name__ == "__main__":
    main()
