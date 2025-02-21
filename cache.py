import numpy
import math
list_color = numpy.array([
    (0, 0, 0),
    (105, 105, 105),
    (85, 85, 85),
    (128, 128, 128),
    (211, 211, 211),
    (255, 255, 255),
    (255, 153, 153),
    (204, 51, 51),
    (220, 20, 60),
    (153, 0, 0),
    (128, 0, 0),
    (255, 87, 0),
    (204, 255, 140),
    (129, 222, 118),
    (0, 111, 60),
    (58, 85, 180),
    (108, 173, 223),
    (140, 217, 255),
    (0, 255, 255),
    (183, 125, 255),
    (190, 69, 255),
    (250, 57, 131),
    (255, 153, 0),
    (255, 230, 0),
    (87, 52, 0)
])
checks = numpy.array((73, 253, 90))
difference = []
for lc in list_color:
    difference.append([
        _ if (_ := int(lc[0] - checks[0])) > 0 else 0,
        _ if (_ := int(lc[1] - checks[0])) > 0 else 0,
        _ if (_ := int(lc[2] - checks[0])) > 0 else 0,
        # int(lc[0] - checks[0]),
        # int(lc[1] - checks[1]),
        # int(lc[2] - checks[2])
    ])
difference = numpy.array(difference)
avg = numpy.vectorize(int)(numpy.mean(difference, axis = 1))
difference = zip(difference, avg, list_color)
difference = sorted(difference, key = lambda x: x[1])

for e in difference:
    print(e)
# for c in difference:
#     print(c)
# print("----")
# for c in avg:
#     print(c)