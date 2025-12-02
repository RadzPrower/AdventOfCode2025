def main(data):
    return find_invalids(data)

def find_invalids(data):
    invalid_id_sum = 0
    ranges = data[0].split(',')
    for id_range in ranges:
        start, end = id_range.split('-')
        for i in range(int(start), int(end)+1):
            i_string = str(i)
            length = len(i_string)
            final_segment_length = length//2
            for segment_length in range(1, final_segment_length + 1):
                if length % segment_length == 0:
                    segments = []
                    for j in range(0, length, segment_length):
                        segments.append(i_string[j:j + segment_length])
                    if len(segments) > 1 and len(set(segments)) == 1:
                        invalid_id_sum += i
                        break
    result = "The sum of the invalid IDs is " + str(invalid_id_sum) + ".\n"
    return result