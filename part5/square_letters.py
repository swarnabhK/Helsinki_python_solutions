# Layers: 4

# DDDDDDD
# DCCCCCD
# DCBBBCD
# DCBABCD
# DCBBBCD
# DCCCCCD
# DDDDDDD

lays = int(input("Layers: "))
layers = [''.join(chr(64+lays) for i in range(2*lays-1))]
for i in range(1,lays):
    s = layers[i-1]
    st = s[0:i]
    l = 2*lays-2*i-1
    for j in range(i,i+l):
        st+=chr(64+lays-i)
    st+=s[i+l:]
    layers.append(st)

#print forwards
for layer in layers:
    print(layer)
#print backwards excluding the last layer
for i in range(len(layers)-2,-1,-1):
    print(layers[i])

        