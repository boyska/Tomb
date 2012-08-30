#!/usr/bin/env zsh

source utils.sh
if [[ -z $output ]]; then
	output=/dev/null
fi
if [[ -z $sudo_pwd ]]; then
	echo "WARNING: sudo_pwd is probably needed by some test"
fi
rm /tmp/tomb_test_errorlog -f &> /dev/null
for t in *.test.sh; do
	sudo_pwd=$sudo_pwd source $t 3>> /tmp/tomb_test_errorlog 4>> /tmp/tomb_test_fulllog
	ret=$?
done

if [[ `stat -c '%s' /tmp/tomb_test_errorlog` == 0 ]]; then
	echo "No errors!"
else
	< /tmp/tomb_test_errorlog
	rm /tmp/tomb_test_errorlog
#TODO: make it optional!
	echo "\n--- Full log ---\n"
	< /tmp/tomb_test_fulllog
	rm /tmp/tomb_test_fulllog
	exit 1
fi

