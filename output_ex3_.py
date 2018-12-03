# output_ex3.py
# 5th chapter exercise 3
'''
def main():
    for ch in "aardvark":
        print(ch)
main()
'''
'''
def main():
    for w in "Now is the winter of our discontent...".split():
        print(w)
main()
'''
'''
def main():
    for w in "Mississippi".split("i"):
        print(w, end=" ")
main()
'''
'''
def main():
    msg = ""
    for s in "secret".split("e"):
        msg = msg + s
    print(msg)
main()
'''

def main():
    msg = ""
    for ch in "secret":
        msg = msg + chr(ord(ch)+ 1)
    print(msg)
main()
