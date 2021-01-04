test_name=$1
mkdir ./test_files/${test_name}
touch ./test_files/${test_name}/testcase_1.py ./test_files/${test_name}/result_1.py

export TEST_NAME=$test_name
envsubst < ./template/template_for_tests.tmpl > ./${test_name}_test.py
