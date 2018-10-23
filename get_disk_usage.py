#!/usr/bin/env python3

# Get the disk usage of the file/directory and its sub folders

import os

def disk_usage(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for entry in os.listdir(path):
            childpath = os.path.join(path, entry)
            total += disk_usage(childpath)
        print(f"{path}'s size is: {total}")
    return total


def main():
    total_disk_space = disk_usage('/Users/gaurav_midha/Documents/repos')
    print(f"------ {total_disk_space} ---")

if __name__ == "__main__":
    main()
