
#!/bin/bash

# echo "nbdev builds..."
# nbdev_build_lib && nbdev_clean_nbs && nbdev_build_docs
# echo "pip installs..."
# pip install $(cat settings.ini | grep -o "requirements =.*" | cut -f3- -d' ')
echo "Create folder structure..."
LIB_NAME=$(cat settings.ini | grep -o "lib_name =.*" | cut -f3- -d' ')

ROOT=$PWD 
cd nbs
ln -f -s $ROOT/$LIB_NAME $PWD
function create_folder_structure {


    for dir in */; do # */ to matach only directories
        [ -L "${dir%/}" ] && continue
        if [ -d "$dir" ]; then # check if directory has further directoies
            (cd "$dir" && ln -f -s $ROOT/$LIB_NAME $PWD  && create_folder_structure); # replace pwd with the command to be executed in the directory
        fi 
    done
}

function delete_folder_structure {


    for dir in */; do # */ to matach only directories
        echo "$dir"
        [ -L "${dir%/}" ] && continue
        if [ -d "$dir" ]; then # check if directory has further directoies
            (cd "$dir" && rm -f  "$PWD/$LIB_NAME"  && delete_folder_structure); # replace pwd with the command to be executed in the directory
        fi 
    done
}


create_folder_structure
# delete_folder_structure