# Read the gff file into a dictionary 

def gff_to_dict(gff_file):
	"""
	read gff file into dictionary
	"""
	gff_dict = {}
	for line in gff_file:
		line = line.strip("\n").split("\t")
		seqid = line[0]
		source = line[1]
		feature = line[2]
		# gff coordinates are 1-based, turn them to 0-based 
		# before recording into dictionary.
		start = int(line[3])-1 # make start 0-based
		end = int(line[4])
		strand = line[6]
		if not line[7] == ".":
			phase = int(line[7])
		attribute = line[8]
		mRNA_ID = attribute.split(";")[0].replace("ID=", "")

		if feature == "mRNA":
			# Set tuples as dictionary keys
			gff_key = (seqid, strand, mRNA_ID)
		if feature == "CDS":
			gff_value = (start, end, phase)
			if gff_key in gff_dict.keys():
				gff_dict[gff_key].append(gff_value)
			else:
				gff_dict[gff_key] = [gff_value]

	# coordinates in gff files are not written in standard format,
	# on plus (sense) strand, coordinates are usually written in 
	# a descending order. On the minus (anti-sense) strand, 
	# coordinates are written in a descending order. However, 
	# irregularites occur in both cases. Here, we check if the
	# coordinates are ascending, if descending, we reverse the list
	# so we will have a gff dictionary with all coordinates in 
	# ascending order.
	for key in gff_dict.keys():
		if key[1] == "+":
			if list(gff_dict[key])[0][0] > list(gff_dict[key])[-1][0]:
				gff_dict[key].reverse()
		elif key[1] == "-":
			if list(gff_dict[key])[0][0] < list(gff_dict[key])[-1][0]:
				gff_dict[key].reverse()			
	
	return gff_dict