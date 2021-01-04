test_name=$1
mkdir ./test_files/${test_name}

export TEST_NAME=$test_name
envsubst < ./template/template_for_tests.tmpl > ./${test_name}_test.py
