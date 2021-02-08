def scrambler(password):
    keys = {
        1: "q01e",
        2:"p65o",
        3:"v78b",
        4:"r45u",
        5:"y78i",
        6:"z23t",
        7:"b17i",
        8:"m98t",
        9:"o16i",
        0:"g45i"
    }
    answer = ""
    for i in str(password):
        i = keys[int(i)]
        answer += i
    return answer

def interpreter(password):
    keys = {
        "q01e": 1,
        "p65o": 2,
        "v78b": 3,
        "r45u": 4,
        "y78i": 5,
        "z23t": 6,
        "b17i": 7,
        "m98t": 8,
        "o16i": 9,
        "g45i": 0
    }
    answer = ""
    password = str(password)
    for i in range(0, len(password), 4):
        answer += str(keys[password[i:i+4]])
    return answer


