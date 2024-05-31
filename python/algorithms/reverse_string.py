def reverse_string(s):
    if len(s) == 0 or s == None:
        return ""

    chars = [c for c in s]
    start = 0
    end = len(chars) - 1

    while start < end:
        chars[start], chars[end] = chars[end], chars[start]
        start += 1
        end -= 1

    return "".join(chars)


s = "Hello, World!"
print(reverse_string(s))
