import sys
import re


out = open(sys.argv[1] + '-nofstrings.py', 'w')
for fullline in open(sys.argv[1]):
	linestart = 0
	#print("line: '%s'" % (fullline))
	while True:
		line = fullline[linestart:]
		if "f'" not in line and 'f"' not in line:
			out.write(line)
			break
		if "f'" in line:
			start = "f'"
			end = "'"
		elif 'f"' in line:
			start = 'f"'
			end = '"'
		
		istart = line.index(start)
		iinside = istart + len(start)
		if end not in line[iinside:]:
			print("skipping problematic part: '%s'" % line.rstrip())
			out.write(line)
			linestart += len(line)
			continue
		try:
			iend = iinside + line[iinside:].index(end)
			part = line[iinside:iend]
			matches = re.findall(r'{([^}:]*)(:[^}]*)?}', part)
			keys = [key for key, format in matches]
			part = re.sub(r'{([^}:]*)((:[^}]*)?)}', r'{\2}', part)
			#print('  "%s": matches:%s keys:%s' % (part, matches, keys))
			out.write(line[:istart])
			out.write(start.replace('f', ''))
			out.write(part)
			out.write(end)
			if len(keys) > 0:
				out.write('.format(' + ', '.join(['%s' % (key) for key in keys]) + ')')
			#out.write(line[iend+len(end):])
			linestart += iend + len(end)
		except:
			print("skipping problematic line: '%s'" % line.rstrip())
			out.write(line)
			linestart += len(line)
		
