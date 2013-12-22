# Inputs all data for all valid forms into the database, but doesn't return any value
def get_all_current_filings():
	# RETURN: NULL
	
	# Run through the filings
	for each_filing in all_filings:
		
		# Only continue with current file search if the form_type is a Form 4
		if filing_type == "4":
			
			# If the form id is non existent, it means the filing is a duplicate
			# and can be ignored, so continue in the for loop to progress to the
			# next filing instance.
			if filing_id_number == NULL or foiling_has_already_been_processed( filing_id_number ):
				
				continue
			
			# Otherwise, continue with the program by storing the information in our database	
			filing_information = [ filing_type, filing_html_address, filing_txt_address, filing_id_number, filing_date ]
			current_company = DataExtractor( filing_information, SQL_database )

# Checks to see if current_form_id is in the list of form ID's already checked
# and returns a boolean
def filing_has_already_been_processed( current_filing_id ):
	# RETURN: BOOLEAN

# Gets all filing information from the html address:
class DataExtractor():

	def __init__( self, filing_information, SQL_database ):
		# Initializations here
		self.form_type = filing_information[ 0 ]
		self.form_html_address = filing_information[ 1 ]
		self.form_txt_address = filing_information[ 2 ]
		self.form_id_number = filing_information[ 3 ]
		self.form_date = filing_information[ 4 ]
		
		self.SQL_database = SQL_database
		
		# Executes its own definitions when initialized
		self.form_information = self.get_all_filing_information( self.form_text_address )
		self.company_information = self.get_all_company_information( self.ticker )
		
		# Uses the information from the two above programs to store in the SQL database
		self.store_all_information_in_database( self.SQL_database, self.form_information, self.company_information )
			
	def get_all_filing_information( url_for_text_file ):
		# RETURN: TEXT ARRAY
	
		# Stores the company ticker symbol to use to extract company info
		self.ticker_symbol = company_ticker
		
		# Returns an array of all filing info:
		# 	- Filer name
		# 	- Filer position
		# 	- Total amount of shares bought/sold, transaction type ( START WITH DIRECT PURCHASES ONLY )
		# 	- Total amount of derivatives bought/sold, transaction type ( IGNORE IN THE BEGINNING )
		
		# ALTERNATIVE: just save all
		# information as variables within the class, e.g.:
		#	- self.filer_name = get_filer_name()
		# and return nothing
		
	def get_all_company_information( stock_ticker ):
		# RETURN: TEXT ARRAY
		
		# Returns an array of all company info:
		# 	- Company name
		#	- Company ticker
		#	- Stock price at the time of insider trade
		#	- Market cap at the time of insider trade
		#	- Average daily volume at the time of insider trade
		
		# ALTERNATIVE: just save all
		# information as variables within the class, e.g.:
		#	- self.company_name = get_company_name()
		# and return nothing
		
	# Code to actually input the information into the SQL database
	def store_all_info_in_database( SQL_Database, form_information, company_information ):
		# RETURN: NULL

		# Here, the command will organize all collected information thus far into
		# an acceptable manner and deposit the relevant information into the database
		