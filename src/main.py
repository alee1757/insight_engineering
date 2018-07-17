import sys

def counting(input_file, output_file):
	drug_counter = get_drug_info(input_file,5,2,1,3,4)

	#start writing our new output txt using the output name provided 
	with open(output_file, 'w') as output:
		#header row for output file
		header = "drug_name,num_prescriber,total_cost \n"
		output.write(header)

		#iterate through drugs in dictionary
		for i in drug_counter:
			drug_in_question = drug_counter[i]
			to_write = i + "," + str(drug_in_question['num_prescribers']) + "," + str(drug_in_question['total_cost']) + "\n"
			output.write(to_write)
		output.close()


 
def get_drug_info(input_file, row_length, doctor_first_ix, doctor_last_ix, drug_name_ix, drug_cost_ix):
	#get drug info will open the input file and get the necessary information.
	#there are several parameters to account for the fact that column names or order may change
	
	drug_counter = {}
	prescription_ids = []
	skipped_input_header = False

	counter = 0
	input("i hate everything")
	with open(input_file, "r") as filestream:
		for line in filestream:
			print(counter)
			if counter%1000==0:
				print(counter)
			else:
				pass
			counter+=1
			if skipped_input_header:
				line_info = line.split(',')

				#testing if all of the fields exist
				if len(line_info)!=row_length or line_info[0] in prescription_ids:
					pass

				else:
					#preventing duplicate prescriptions
					prescription_ids.append(line_info[0])
					#getting the relevant information from the line
					drug_prescriber = line_info[doctor_first_ix] + " " + line_info[doctor_last_ix]
					drug_name = line_info[drug_name_ix]
					drug_cost = line_info[drug_cost_ix].rstrip()

					#if the drug is already in the dictionary, update values
					if drug_name in drug_counter:
						specific_drug = drug_counter[drug_name]
						if drug_prescriber in specific_drug['prescribers']:
							pass
						else:
							specific_drug['prescribers'].append(drug_prescriber)
							specific_drug['num_prescribers']+=1
						specific_drug['total_cost']+=float(drug_cost)

					#if the drug does not exist yet, create a new key
					else:
						drug_counter[drug_name]={}
						specific_drug = drug_counter[drug_name]
						specific_drug['prescribers'] = [drug_prescriber]
						specific_drug['num_prescribers'] = 1
						specific_drug['total_cost'] = float(drug_cost)

			#not copying the first header row
			else:
				skipped_input_header=True

	return(drug_counter)

if __name__ == "__main__":
	in_file = sys.argv[1]
	out_file = sys.argv[2]
	counting(in_file,out_file)