import os
import pathlib

from publisher.extractor import Extractor

init_edition = 34
last_edition = 68


def execute():
    pass


def publish():
    root_dir = get_root_dir()
    extractor = Extractor()
    for edition in range(init_edition, last_edition + 1):
        json_text = extractor.to_json(edition)
        print(" processing edition {}".format(edition))
        filename = "{root_dir}/data_engineering_weekly_{edition}.json".format(root_dir=root_dir, edition=edition)
        with open(filename, 'w') as f:
            f.write(json_text)
        print(" finished writing edition {}".format(edition))


def get_root_dir():
    path = pathlib.Path(__file__).parent.resolve()
    return path.parent


if __name__ == "__main__":
    publish()
