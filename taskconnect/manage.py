#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
	#import warnings
	#warnings.filterwarnings('ignore', message=r'Module .*? is being added to sys\.path', append=True)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "taskconnect.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
