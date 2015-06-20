with open("p059_cipher.txt", "r") as infile:
    for line in infile:
        val_temp = line.split(",")

values = [int(i) for i in val_temp]
length = len(values)

def convert_text(key):
    new_text = []
    for i in xrange(length):
        new_val = values[i] ^ key[i%3]
        new_text.append(new_val)
    return new_text



# lower case from 97 to 122
# should be many 32 (space) and 69 (E) and 101 (e)
# less than 32: reject
keys = [[i, j, k] for i in xrange(97, 123) for j in xrange(97, 123) for k in xrange(97, 123)]
possible_vals = []
for key in keys:
    possible_vals.append(convert_text(key))

possible_vals2 = []
for possible_val in possible_vals:
    if 32 in possible_val:
        possible_vals2.append(possible_val)

possible_vals3 = []
for possible_val in possible_vals2:
    if 101 in possible_val:
        possible_vals3.append(possible_val)

print len(possible_vals3)
