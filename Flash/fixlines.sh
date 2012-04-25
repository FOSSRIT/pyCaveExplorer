#!/bin/bash

for i in $(find . -name '*.as' -exec file '{}' \; |
        grep 'with CR line terminators' |
        sed 's/:.*//g'); do
    echo $i;
    perl -pi -e 's/\r/\n/g;' "$i";
done
