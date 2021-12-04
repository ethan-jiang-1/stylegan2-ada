import sys

from dataset_tool import execute_cmdline

def create_argv():
    sys.argv = "x_dataset_tool.py create_minstrgb"

if __name__ == "__main__":
    create_argv()
    execute_cmdline(sys.argv)