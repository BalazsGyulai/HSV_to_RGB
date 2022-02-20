
# Online Python - IDE, Editor, Compiler, Interpreter
R,G,B = 0,0,0
def hsvtorgb(H,S,V):
    global R,G,B
    
    C = V * S
    X = C * (1 - abs((H / 60)%2 - 1))
    m = V - C
    
    if 0 <= H and H < 60:
        r,g,b = C,X,0
    elif 60 <= H and H < 120:
        r,g,b = X,C,0
    elif 120 <= H and H < 180:
        r,g,b = 0,C,X
    elif 180 <= H and H < 240:
        r,g,b = 0,X,C
    elif 240 <= H and H < 300:
        r,g,b = X,0,C
    elif 300 <= H and H < 360:
        r,g,b = C,0,X
    
    R,G,B = round((r+m)*255), round((g+m)*255), round((b+m)*255)
     
while True:
    H = float(input("H"))
    S = float(input("S"))
    V = float(input("V"))
    
    hsvtorgb(H,S,V)
    print(R,G,B)