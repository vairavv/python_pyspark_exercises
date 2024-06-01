s=input().strip()
sub=input().strip()
custom_len=len(s)-len(sub)
sub_len=len(sub)
count=0
for i in range(0,custom_len+1):
    #print(s[i:i+sub_len])
    if sub==s[i:i+sub_len]:
        count+=1
print(count)