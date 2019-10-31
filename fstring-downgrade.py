import sys
import re


out = open(sys.argv[1] + '-nofstrings.py', 'w')
for line in open(sys.argv[1]):
	if "f'" not in line and 'f"' not in line:
		out.write(line)
		continue
	if "f'" in line:
		start = "f'"
		end = "'"
	if 'f"' in line:
		start = 'f"'
		end = '"'
	
	istart = line.index(start)
	iinside = istart + len(start)
	iend = iinside + line[iinside:].index(end)
	part = line[iinside:iend]
	matches = re.findall('{([^}:]*)(:[^}]*)?}', part)
	keys = [key for key, format in matches]
	part = re.sub('{([^}:]*)(:[^}]*)?}', '{\\2}', part)
	out.write(line[:istart])
	out.write(start.replace('f', ''))
	out.write(part)
	out.write(end)
	if len(keys) > 0:
		out.write('.format(' + ', '.join(['%s' % (key) for key in keys]) + ')')
	out.write(line[iend+len(end):])
