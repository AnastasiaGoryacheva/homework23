def construct_query(cmd, value, file):
    if cmd == "filter":
        result = filter(lambda x: value in x, file)
    if cmd == "map":
        value = int(value)
        result = [x.split()[value] for x in file]
    if cmd == "limit":
        value = int(value)
        result = list(file)[:value]
    if cmd == "sort":
        value = bool(value)
        result = sorted(file, reverse=value)
    if cmd == "unique":
        result = list(set(file))
    return result
