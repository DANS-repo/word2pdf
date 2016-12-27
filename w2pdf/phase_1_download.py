#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import os

import logging

import sys
from fedora.worker import Worker

LOG = logging.getLogger(__name__)


def setup_logging():
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    ch.setFormatter(formatter)
    root.addHandler(ch)


def download():
    work_dir = os.path.join(os.path.expanduser("~"), "tmp", "word2pdf")
    os.makedirs(work_dir, exist_ok=True)
    id_list = os.path.join(work_dir, "id_list.txt")
    dump_dir = os.path.join(work_dir, "worker-downloads")
    log_file = os.path.join(work_dir, "worker-log.csv")

    worker = Worker()
    checksum_error_count = worker.download_batch(id_list, dump_dir, log_file)
    return checksum_error_count


if __name__ == '__main__':
    setup_logging()
    errors = download()
    assert errors == 0


