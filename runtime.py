"""This module provides utility functions for performance analysis of Python scripts."""

import datetime
import subprocess
import sys
import time


def measure_execution_time(filename: str, dirpath: str = "") -> None:
    """
    Measures and logs the execution time of a Python script.

    This function runs the specified Python file as a subprocess and measures the time it takes to
    execute. The result, along with a timestamp, is written to an output file named after the Python
    script but with a `.out.txt` extension. This can be useful for tracking the performance of
    scripts over time.

    Args:
        filename (str): The name of the Python file (without the `.py` extension) to be executed.
        dirpath (str, optional): The directory path where the Python file is located. Defaults to
        the current directory.

    Output:
        None: The execution time is logged in a file with the `.out.txt` extension in the same
        directory.
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
