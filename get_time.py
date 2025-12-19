from __future__ import annotations

from datetime import datetime


def main() -> None:
    now = datetime.now().astimezone()
    print(now.strftime("%Y-%m-%d-%H-%M"))


if __name__ == "__main__":
    main()
