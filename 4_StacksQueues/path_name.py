
def shortest_equivalent_path(path):
    if not path:
        return False

    pathNames = []
    if path[0] == '/':
        pathNames.append('/')

    for token in (token for token in path.split('/') if token not in ['.','']):
    # EQUIVALENT: token3 = list(filter((lambda token: token not in ['.','']),path.split('/')))
        if token == '..':
            if not pathNames or pathNames[-1] == '..':
                pathNames.append(token)
            else:
                if pathNames[-1] == '/':
                    raise ValueError('Path error')
                pathNames.pop()
        else:
            pathNames.append(token)

    result = '/'.join(pathNames)
    return result[result.startswith('//'):]

path = 'scripts//./../scrpits/awkscripts/././'
print(shortest_equivalent_path(path))