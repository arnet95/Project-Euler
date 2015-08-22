with open("./input/p059_cipher.txt", "r") as infile:
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
# should be many 32 (space) and 101 (e)
# less than 32: reject
keys = [[i, j, k] for i in xrange(97, 123) for j in xrange(97, 123) for k in xrange(97, 123)]

final_vals = []
for possible_value in [convert_text(key) for key in keys]:
    if 32 in possible_value:
        if 101 in possible_value:
            if 91 not in possible_value:
                if 92 not in possible_value:
                    if 93 not in possible_value:
                        if 94 not in possible_value:
                            if 95 not in possible_value:
                                if 96 not in possible_value:
                                    if 123 not in possible_value:
                                        if 125 not in possible_value:
                                            final_vals.append(possible_value)


#Now final_vals contains the only possible situation
print sum(i for i in final_vals[0])

print "Actual text:"
print ''.join([chr(i) for i in final_vals[0]])
