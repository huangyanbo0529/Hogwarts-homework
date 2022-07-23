# _*_coding_*_: utf-8
# Author：yb
# Date ：2022/7/24 0:17
# Tool ：IntelliJ IDEA
import os.path

cur_dir = os.path.dirname(os.path.abspath(__file__))
root_path = cur_dir[:cur_dir.find("\\hogwartsHomework") + len("\\hogwartsHomework")]

if __name__ == '__main__':
    print(cur_dir)
    print(root_path)
