# Problem-solving practice 2 (competition / LeetCode style) - a step up in difficulty.
#
# Most of these are natural fits for a STACK or a QUEUE (this week's data structures).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def eval_rpn(tokens):
    stack = []
    operators = {"+", "-", "*", "/"}

    for token in tokens:
        if token in operators:
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(int(a / b))
        else:
            stack.append(int(token))

    return stack[0]


def decode_string(s):
    stack = []
    current_str = ""
    current_num = 0

    for ch in s:
        if ch.isdigit():
            current_num = current_num * 10 + int(ch)
        elif ch == "[":
            stack.append((current_str, current_num))
            current_str = ""
            current_num = 0
        elif ch == "]":
            prev_str, k = stack.pop()
            current_str = prev_str + (current_str * k)
        else:
            current_str += ch

    return current_str


def daily_temperatures(temps):
    ans = [0] * len(temps)
    stack = []

    for i, temp in enumerate(temps):
        while stack and temp > temps[stack[-1]]:
            prev_i = stack.pop()
            ans[prev_i] = i - prev_i
        stack.append(i)

    return ans


def num_islands(grid):   # Part 4 - stretch (optional)
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                islands += 1
                visited.add((r, c))
                stack = [(r, c)]

                while stack:
                    curr_r, curr_c = stack.pop()
                    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        nr, nc = curr_r + dr, curr_c + dc
                        if (
                            0 <= nr < rows
                            and 0 <= nc < cols
                            and grid[nr][nc] == "1"
                            and (nr, nc) not in visited
                        ):
                            visited.add((nr, nc))
                            stack.append((nr, nc))

    return islands


def main():
    # Optional scratch space - try your functions here, then run: python lab10.py
    print(eval_rpn(["2", "1", "+", "3", "*"]))
    print(eval_rpn(["4", "13", "5", "/", "+"]))
    print(decode_string("3[a2[c]]"))
    print(decode_string("2[abc]3[cd]ef"))
    print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))
    print(num_islands(["11000", "11000", "00100", "00011"]))


if __name__ == "__main__":
    main()