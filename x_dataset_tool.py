import sys

from dataset_tool import execute_cmdline

def create_argv():

    tfrecord_dir = "ds_train"
    src_dir = "ds_src"
    num_images = 5000

    cmd = "x_dataset_tool.py create_mnistrgb {} {} --num_images {}".format(tfrecord_dir, src_dir, num_images)

    cmd = cmd.strip()
    return cmd.split(" ")

if __name__ == "__main__":
    sys.argv = create_argv()
    execute_cmdline(sys.argv)
