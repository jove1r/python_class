ipAddress = input("Please provide an ip adress ")

segment = 1
segment_length = 0
character = ""

for character in ipAddress:
    if character == '.':
        print("segment {} contains {} characters".format(segment,segment_length))
        segment += 1
        segment_length = 0
    else:
        segment_length += 1

#unless the final character ewas a '.' then we havent printed the last segment
if character != '.':
    print("segment {} contains {} characters".format(segment, segment_length))
