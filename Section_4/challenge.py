ip_address = input("Enter an IP address. An IP address consists in 4 numbers, "
                   "separated from each other with a full stop: ")
if ip_address != '.':
    ip_address += '.'
segment = 1
segments_length = 0
# character = ''
for character in ip_address:
    if character == '.':
        print(f"Segment {segment} contains {segments_length} characters")
        segment += 1
        segments_length = 0
    else:
        segments_length += 1
# unless the final character in the string was a .  then we haven't printed the last segment
if character != '.':
    print(f"Segment {segment} contains {segments_length} characters")





