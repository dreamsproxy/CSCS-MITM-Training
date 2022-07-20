cd machine/

FILE=./Vagrantfile
if [ -f "$FILE" ]; then
    echo "$FILE exists"
    echo "Attempting to initialize vagrant env"
    vagrant up
else
    echo " $FILE does not exist."
    echo "Attempting to run 'vagrant init ubuntu/focal64'"
    vagrant init ubuntu/focal64