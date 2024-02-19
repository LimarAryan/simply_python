#check if directory TESTDIR is there
#if not, creates one

import os

MESSAGE = "The directory already exists."
TESTDIR = "testdir"

try:
    home = os.path.expanduser(
        "~"
    )
    print(home)

    if not os.path.exists(
        os.path.join(home, TESTDIR)
    ):
        os.makedirs(
            os.path.join(home, TESTDIR)
        )
    else:
        print(MESSAGE)
except Exception as e:
    print(e)