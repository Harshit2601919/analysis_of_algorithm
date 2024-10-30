


def rabin_karp(text,pattern):
    n=len(text)
    m=len(pattern)

    hash_text=hash(text)
    hash_pattern=hash(pattern)
    
    valid_shift=0

    for i  in range(n-m+1):
        if hash_pattern==hash_text:
            if text[i:i+m]==pattern:
                return i,i+m-1,valid_shift
            
        if i<n-m:
            hash_text=hash(text[i+1:i+m+1])
            valid_shift+=1

    return -1,-1,valid_shift

text=input("enter the text")
pattern=input("enter the pattern")
start_index,end_index,shift=rabin_karp(text,pattern)

if start_index!=-1:
  print("string found at [",start_index,",",end_index,"]")
  print("shifts",shift)

else:
    print("no found")
