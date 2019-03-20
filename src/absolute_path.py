# Given an absolute pathname that may have . or .. as part of it, return the
# shortest standardized path.

# For example, given "/usr/bin/../bin/./scripts/../", return "/usr/bin/".


def standardized_path(path):
    ans = []
    for p in path.split('/'):
        if not p or p == '.':
            continue
        elif p == '..':
            if ans:
                ans.pop()
        else:
            ans.append(p)

    return '/{}/'.format('/'.join(ans))


if __name__ == '__main__':
    for path in [
        '/usr/bin/../bin/./scripts/../',
        '/usr/bin/', '/usr/../home',
        '/usr/../../.././usr/bin/..'
    ]:
        print(path, standardized_path(path))
