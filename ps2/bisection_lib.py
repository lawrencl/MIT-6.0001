import sys

def draw_interval(lower_bound, midpoint, upper_bound, original_upper_bound):
    """
    Scale 
    """   

    print "lowerbound:\t", lower_bound
    print "midpoint:\t", midpoint
    print "upperbound:\t", upper_bound
    scale_low = int(lower_bound)*50/int(original_upper_bound)
    scale_mid = int(midpoint)*50/int(original_upper_bound)
    scale_high = int(upper_bound)*50/int(original_upper_bound)
    skipone = False
    for i in range(51):
        if i == scale_low and i == scale_mid and i == scale_high:
            sys.stdout.write('.|')
            skipone = True
        elif i == scale_low and i == scale_mid:
            sys.stdout.write('{|')
            skipone = True
        elif i == scale_mid and i == scale_high:
            sys.stdout.write('|}')
            skipone = True
        elif i == scale_low:
            sys.stdout.write('{')    
        elif i == scale_mid:
            sys.stdout.write('|')    
        elif i == scale_high:
            sys.stdout.write('}')
        else:
            if not skipone:
                sys.stdout.write('.')   
            else:
                skipone = False
    print '\n' 
   
