import sys

try:
    if ('{{ cookiecutter.aws_container_credentials_relative_uri }}' == '/role' and
            '{{ cookiecutter.aws_role }}' == '<required>'):
        raise Exception('ERROR: AWS role is required')
except Exception as e:
    print(e, file=sys.stderr)
    sys.exit(1)
