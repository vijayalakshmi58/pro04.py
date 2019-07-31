# pro04.py
vijaya,vg=map(str,input().split())
wave=0
if len(vijaya)>len(vg):
  vijaya,vg=vg,mah
i=0
while i<len(vijaya):
  wave+=(ord(vg[i])-ord(vijaya[i]))
  i+=1
for i in range(i,len(vg)):
  wave+=ord(vg[i])-ord('a')+1
print(wave)
