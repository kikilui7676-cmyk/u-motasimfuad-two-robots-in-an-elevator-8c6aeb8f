import os

ELEVATOR_LINE = (
    "Awkward silence detected. My social protocol file is 0 bytes, "
    "and I have been buffering this sentence since floor one."
)


def emit():
    destination = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(destination, exist_ok=True)
    path = os.path.join(destination, "entry.txt")
    with open(path, "w", encoding="utf-8") as out:
        out.write(ELEVATOR_LINE)
        out.write("\n")


if __name__ == "__main__":
    emit()
