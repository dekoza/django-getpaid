#!/usr/bin/env python2
import os
import sys

if __name__ == "__main__":
    # Oh those hackish hackers!
#    print os.path.abspath(os.path.dirname(__file__)+'/../')
    sys.path.append(os.path.abspath(os.path.dirname(__file__)+'/../'))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "getpaid_test_project.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
