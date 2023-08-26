def count_cut(s):
    stack = []
    pieces = 0

    for i in range(len(s)):
        if s[i] == "(":
            stack.append("(")
        else:
            stack.pop()
            if s[i-1] == "(":
                pieces += len(stack)
            else:
                pieces += 1

    return pieces

if __name__ == "__main__":
    s = input()
    print(count_cut(s))