def edit_distance(string1, string2):
    m, n = len(string1), len(string2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if string1[i - 1] == string2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

    return dp[m][n], dp


string1 = "SWIMMER"
string2 = "SWIMMET"
distance, matrix = edit_distance(string1, string2)
assert distance == 1

string1 = ""
string2 = ""
distance, matrix = edit_distance(string1, string2)
assert distance == 0

string1 = ""
string2 = "S"
distance, matrix = edit_distance(string1, string2)
assert distance == 1

string1 = "S"
string2 = ""
distance, matrix = edit_distance(string1, string2)
assert distance == 1

string1 = "SWIMMER"
string2 = "swimmer"
distance, matrix = edit_distance(string1, string2)
assert distance == 7

string1 = " SWIMMER"
string2 = "SWIMMER "
distance, matrix = edit_distance(string1, string2)
assert distance == 2

string1 = "IMM"
string2 = "SWIMMER "
distance, matrix = edit_distance(string1, string2)
assert distance == 5
