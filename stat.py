import sys
import numpy

h  = []
d0 = []
for line in sys.stdin:
  buf = line.split(",")
  for t in range(0, len(buf)): buf[t] = float(buf[t])
  if(len(d0) < 1):
    d0 = numpy.array(buf)
  else:
    h.append(numpy.dot(d0, numpy.array(buf)))
h  = sorted(h)
hh = []
for t in range(0, int(sys.argv[1]) + 1): hh.append(0)
band = max(abs(h[- 1]), abs(h[0]))
tt = -1
for g in h:
  if(h[- 1] * h[0] < 0):
    u = int(abs(g + band) / 2 / band * int(sys.argv[1]))
  else:
    u = int(abs(g) / band * int(sys.argv[1]))
  if(u != tt): tt = u
  hh[tt] += 1
h = []
for g in hh:
  h.append(str(g))
print(",".join(h))

