def scan_and_add(modifer, base_array):  # scan the array and add the correct parts up
    processed_array = [1]
    odd_pattern = 1  # after every 1 crap number, add the good one to our out array
    odd_pattern_saved = 1
    end_count = 0  # all the good nums come in seqences of 4
    diag_result = 0
    for x in base_array:
        if odd_pattern != 0:  # ****non zero means we're on crap int we dont want
            odd_pattern -= 1
        else:  # if not crap number and not done
            odd_pattern = odd_pattern_saved  # we are past the good num now, its all crap from here
            processed_array.append(x)  # add num to out list
            end_count += 1
            if end_count == 4:  # every final good num, inc to next odd seqence
                odd_pattern += 2  # next odd num
                odd_pattern_saved = odd_pattern  # set our save to new pattern
                end_count = 0  # reset
    for x in processed_array:
        diag_result += x  # add it all up, place in diag, this is our result
        final_result = diag_result + (len(processed_array) * (modifer - 1))
    return final_result


def spiralize(size, n=1):
    size *= size
    base_array = range(2, size + 1)  # this made things alot nicer
    return_value = scan_and_add(n, base_array)
    return return_value
