import re

def main():
    S = input().rstrip()
    P = input().rstrip()
    escaped_P = re.escape(P)
    len_p = len(P)
    count = 0
    for i in range(len(S) - len_p + 1):
        if S[i:i+len_p] == P: 
            count += 1 
    print(count)

if __name__ == "__main__":
    main()