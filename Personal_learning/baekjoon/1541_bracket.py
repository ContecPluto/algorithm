word = input()
val = ""
arr = []
for w in word:
    if w.isdigit():
        val += w
    else:
        arr.append(str(int(val)))
        arr.append(w)
        val = ""
arr.append(str(int(val)))

i = 0
while i < len(arr) - 2:
    if arr[i] == "-" and arr[i+2] == "+":
        arr[i+1:i+4] = [str(eval("".join(arr[i+1:i+4])))]
        i -= 1
    i += 1
print(eval("".join(arr)))