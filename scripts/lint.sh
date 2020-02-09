#!/usr/bin/env bash
EXIT_CODE=0

pylint src || EXIT_CODE=1

pycodestyle src || EXIT_CODE=1

exit ${EXIT_CODE}
