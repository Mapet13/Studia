#!/bin/bash

find . -type f -name 'makefile' | while read FILE ; do
    if [[ "${FILE}" != "./utils/makefile" ]]; then
        cat ./utils/makefile > "${FILE}"
    fi
done 