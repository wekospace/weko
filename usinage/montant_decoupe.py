print "T2 M06 G43"
print "G17 G90 G21"
print "G0 Z10"
print "G0 X-205 Y0 M3"

def my_range(start, end, step):
    while start <= end:
        yield start
        start += step

for x in my_range(0.2, 10, 0.4):
    print 'G1 Z-%f F10' % (x)
    print 'G1 Y106 F250'
    print 'G1 Z-%f F10' % (x+0.2)
    print 'G1 Y0 F250'

print "G00 Z10 F250"
print "T0 M06 M02"

