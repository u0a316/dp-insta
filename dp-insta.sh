#/usr/bin/sh
function main() {
eval 'cd $(dirname $0)'
eval 'pip install -r requirements.txt'
eval 'python3 dp-insta.py'
}
main
