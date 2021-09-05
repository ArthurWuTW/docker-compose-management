echo_stderr() {
    >&2 echo "$@"
}

exit_on_error() {
    echo_stderr $@
    exit 1
}
