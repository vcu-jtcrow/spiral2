base_array = [1]        
processed_array = [1]
input_spiral = 501 #501 by 501 spiral  

def establish_array(ceiling):  # lets create our array first
    ceiling*=ceiling
    counter = 0
    for x in base_array: 
        counter += 1
        if counter == ceiling:
            break
        next_val = 1 + x  
        base_array.append(next_val) 

def scan_and_add():  # scan the array and add the correct parts up
    odd_pattern = 1  # after every 1 crap number, add the good one to our out array
    odd_pattern_saved = 1
    end_count = 0  # all the good nums come in seqences of 4
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
    diag_result = 0
    for x in processed_array:
        diag_result += x  # add it all up, place in diag, this is our result
    return diag_result

def spiralize(spiral):
    establish_array(spiral)
    base_array.remove(1)  # nastyness but should do the trick
    solution = scan_and_add()
    print(solution)
    #print(len(processed_array))
    return solution

spiralize(input_spiral)
