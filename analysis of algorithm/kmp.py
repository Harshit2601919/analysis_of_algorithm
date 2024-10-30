def compute_prefix(pattern):
    n = len(pattern)
    prefix = [0] * n
    length = 0
    i = 1
    while i < n:
        if pattern[i] == pattern[length]:
            length += 1
            prefix[i] = length
            i += 1
        else:
            if length != 0:
                length = prefix[length - 1]
            else:
                prefix[i] = 0
                i += 1
    return prefix

def kmp(text, pattern):
    n = len(text)
    m = len(pattern)
    prefix = compute_prefix(pattern)
    valid_shifts = 0
    match_index = -1
    i = j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
            if j == m:
                match_index = i - j
                break
        else:
            if j != 0:
                j = prefix[j - 1]
                valid_shifts += 1
            else:
                i += 1
                valid_shifts += 1
    return match_index, valid_shifts, prefix

# Input from user
text = input("Enter the text: ")
pattern = input("Enter the pattern to search for: ")

# Call the function and print the result
index, shifts, prefix = kmp(text, pattern)
if index != -1:
    print("Pattern found at index:", index)
    print("Number of valid shifts:", shifts)
    print("Pattern prefix array:", prefix)
else:
    print("Pattern not found in the text.")




def compute_prefix(pattern):
    n=len(pattern)
    prefix=[0]*n
    i=1
    length=0
    while i<n:
        if pattern[i]==pattern[length]:
            length+=1
            prefix[i]=length
            i+=1
        else:
            if length!=0:
                length=prefix[length-1]

            else:
                prefix[i]=0
                i+=1
    return prefix

def kmp(text,pattern):
    n=len(text)
    m=len(pattern)
    prefix=compute_prefix(pattern)
    i=j=0
    match_index=-1
    valid_shift=0
    while i<n:
        if pattern[j]==text[i]:
            i+=1
            j+=1
            if j==m:
                match_index=i-j
        else:
            if j!=0:
                j=prefix[j-1]
                valid_shift+=1
            else:
                i+=1
                valid_shift+=1
    return match_index,valid_shift,prefix



text=input("enter the text")
pattern=input("enter the pattern")
index, shift, prefix= kmp(text,pattern)
if index!=-1:
    print(f"the pattern if found at {index}")
    print(f"shift {shift}")
    print(f"prefix {prefix}")

else:
    print("no found")