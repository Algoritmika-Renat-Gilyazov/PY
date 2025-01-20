def concat(*strings):
    out = ""
    for string in strings:
        out += string
    return out
def multi(string, n):
    out = string
    if not isinstance(string, str) or not isinstance(n, int):
        print("Wrong Args!")
        return ""
    return out * n