import sys

def parse_args():
    args = sys.argv[1:]
    valid = True
    message = None
    valid_args = None

    if len(args) < 1:
        valid = False
        message = 'Argument required'
    elif args[0] == 'create':
        if len(args) != 2:
            valid = False
            message = 'Create requires 1 additional argument: <PROJECT NAME>'
            message += f'\n {len(args) - 1} additional arguments provided.'
        else:
            valid_args = args
    elif args[0] == 'pip':
        if len(args) < 2:
            valid = False
            message = 'Pip requires additional arguments.'
        else:
            valid_args = args
    if valid:
        return valid, valid_args
    return valid, message


