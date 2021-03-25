import click
import itertools
from snapshot import create_instance_snapshot

importfile = ""

@click.command()
@click.option('--importfile', '-i', default="", help='Path to import file. The file should contain tags (key value) of EC2 instances. words should be separated by spaces')

def hello(importfile):
    if not importfile:
        print(f"Please provide parameter --importfile followed by full path to import file\n")
    else:
        print(f"\nPath provided: {importfile.upper()}")
        read_file = open(importfile, "r")
        tags_separate = read_file.read()
        tag_list = tags_separate.split()
        read_file.close()
        tag_dictionary = dict(itertools.zip_longest(*[iter(tag_list)] * 2, fillvalue=""))
        print(f"Tags list read from the input file: {tag_list}")
        create_instance_snapshot(tag_dictionary)
    return print(f"End of script")


if __name__ == '__main__':
   hello()
