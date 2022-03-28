import sys

hist = []
for line in sys.stdin:
  d = line.split(",")
  for t in range(len(hist), len(d)):
    hist.append([])
  for t in range(0, len(d)):
    hist[t].append(float(d[t]))
hh = []
for h in hist:
  h = sorted(h)
  hh.append([])
  if(len(h) < 1): continue
  band = max(abs(h[- 1]), abs(h[0]))
  tt = -1
  for t in range(0, int(sys.argv[1]) + 2):
    hh[- 1].append(0)
  for g in h:
    if(h[- 1] * h[0] < 0):
      u = int(abs(g + band) / 2 / band * int(sys.argv[1]))
    else:
      u = int(abs(g) / band * int(sys.argv[1]))
    if(u != tt): tt = u
    hh[- 1][tt] += 1
  h = []
for t in range(0, int(sys.argv[1])):
  g = []
  for h in hh:
    if(len(h) <= t): g.append(str(0))
    else: g.append(str(h[t]))
  print(",".join(g))

