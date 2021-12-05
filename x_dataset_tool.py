import sys

from dataset_tool import execute_cmdline

def create_argv_minstrgb():

    tfrecord_dir = "ds_train"
    src_dir = "ds_src"
    num_images = 5000

    cmd = "x_dataset_tool.py create_mnistrgb {} {} --num_images {}".format(tfrecord_dir, src_dir, num_images)

    cmd = cmd.strip()
    return cmd.split(" ")

def create_arg_lilei():

    tfrecord_dir = "ds_train_lilei"
    src_dir = "ds_chunk_lilei"
    #num_images = 5000

    cmd = "x_dataset_tool.py create_from_images {} {}".format(tfrecord_dir, src_dir)

    cmd = cmd.strip()
    return cmd.split(" ")

if __name__ == "__main__":
    #sys.argv = create_argv_minstrgb()
    sys.argv = create_arg_lilei()

    execute_cmdline(sys.argv)

