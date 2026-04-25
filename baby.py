"""A tiny baby-cat greeter for the cat-and-claude project."""

BABY_CAT = r"""
   /\_/\
  ( o.o )  meow~
   > ^ <
"""


def greet(name: str = "baby") -> str:
    return f"{BABY_CAT}\nHello, {name}! 宝贝，宝贝~"


if __name__ == "__main__":
    print(greet())
