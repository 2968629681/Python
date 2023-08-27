a = eval(input())
ans = 0
if a>=401:
    ans = (a-400)*0.5663
    a=400
if a>150:
    ans += (a-150)*0.4663
    a=150
ans += a*0.4463
print("%.1f"%ans)
