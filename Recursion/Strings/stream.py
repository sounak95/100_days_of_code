
#p:  processed, up: unprocessed
def skip1(p, up):
    if len(up)==0:
        print(p)
        return

    ch=up[0]
    if ch=='a':
        skip1(p, up[1:])
    else:
        skip1(p+ch, up[1:])



def skip2(up):
    if len(up)==0:
        return ""

    ch=up[0]

    if ch=='a':
        return skip2(up[1:])
    else:
        return ch + skip2(up[1:])

def skip_apple(up, substr):
    if len(up)==0:
        return ""
    if up.startswith(substr):
        return skip_apple(up[len(substr):], substr)
    else:
        return up[0] + skip_apple(up[1:], substr)

def skip_app_not_apple(up):
    if len(up)==0:
        return ""
    if up.startswith("app") and not up.startswith("apple"):
        return skip_app_not_apple(up[3:])
    else:
        return up[0] + skip_app_not_apple(up[1:])

if __name__ == "__main__":
    # skip1("","bacapplcdah")
    # print(skip2("bacapplcdah"))
    # print(skip_apple("appleabc", "apple"))
    print(skip_app_not_apple("bacapplcdah"))


