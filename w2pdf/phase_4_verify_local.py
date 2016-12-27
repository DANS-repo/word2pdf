#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import os

import sys

from fedora.worker import LocalWorker


def setup_logging():
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    ch.setFormatter(formatter)
    root.addHandler(ch)


def verify_checksum_local():
    work_dir = os.path.join(os.path.expanduser("~"), "tmp", "word2pdf")
    log_file = os.path.join(work_dir, "worker-log.csv")

    worker = LocalWorker()
    checksum_error_count = worker.verify_checksums_local(log_file)
    return checksum_error_count


if __name__ == '__main__':
    setup_logging()
    errors = verify_checksum_local()
    assert errors == 0