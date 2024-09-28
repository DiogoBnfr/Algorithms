import datetime
import subprocess
import sys
import time


def measure_execution_time(filename: str, dirpath: str = "") -> None:
    """
    Executes the .py file passed in as a subprocess. Write the file output to std
    out and the execution to a file of the same name but with a .out.txt extension
    """
    f = open(dirpath + filename + ".out.txt", "a")

    start_time = time.time()
    subprocess.run(f"python {filename}.py", shell=True)
    end_time = time.time()

    f.write(
        f"{str(datetime.datetime.now()).split('.')[0]} "  # type: ignore
        + f"ExecutionTime: {end_time - start_time:.10f}\n"
    )


if __name__ == "__main__":
    try:
        measure_execution_time(sys.argv[1])
    except IndexError as e:
        print(f"error {e}".replace(" ", "::").upper())
