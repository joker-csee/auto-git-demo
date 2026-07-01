import sys
from datetime import datetime


def greet(name: str) -> str:
    hour = datetime.now().hour
    if hour < 12:
        greeting = "Good morning"
    elif hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"
    return f"{greeting}, {name}!"


def farewell(name: str) -> str:
    return f"Goodbye, {name}!"


def calc(a: float, op: str, b: float) -> str:
    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op in ("*", "x"):
        result = a * b
    elif op == "/":
        if b == 0:
            return "Error: division by zero"
        result = a / b
    else:
        return f"Unknown operator: {op}"
    return f"{a} {op} {b} = {result}"


def text_info(text: str) -> dict:
    words = text.split()
    return {
        "text": text,
        "chars": len(text),
        "words": len(words),
        "reversed": text[::-1],
    }


def show_help():
    print("Usage: python hello.py <command> [args]")
    print()
    print("Commands:")
    print("  greet [name]     Greet (time-appropriate)")
    print("  farewell [name]  Say goodbye")
    print("  calc a op b      Calculate (+, -, *, /)")
    print("  info <text>      Analyze text")
    print("  help             Show this help")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_help()
        sys.exit(0)

    cmd = sys.argv[1]

    if cmd == "greet":
        name = sys.argv[2] if len(sys.argv) > 2 else "World"
        print(greet(name))

    elif cmd == "farewell":
        name = sys.argv[2] if len(sys.argv) > 2 else "World"
        print(farewell(name))

    elif cmd == "calc":
        if len(sys.argv) < 5:
            print("Usage: python hello.py calc <a> <op> <b>")
        else:
            a = float(sys.argv[2])
            op = sys.argv[3]
            b = float(sys.argv[4])
            print(calc(a, op, b))

    elif cmd == "info":
        text = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else ""
        if not text:
            print("Usage: python hello.py info <text>")
        else:
            info = text_info(text)
            print(f"Text:     {info['text']}")
            print(f"Chars:    {info['chars']}")
            print(f"Words:    {info['words']}")
            print(f"Reversed: {info['reversed']}")

    elif cmd == "help":
        show_help()

    else:
        print(f"Unknown command: {cmd}")
        show_help()
