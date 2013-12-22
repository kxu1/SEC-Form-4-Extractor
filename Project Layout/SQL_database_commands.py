class SQLDatabase():
	
	def __init__(self, database_name):
		# Initializations here; don't know how to initialize this yet
		# Presumably load the database that we are looking for here
		self.SQL_database = get_database( database_name )

	# Get the individual values from the database for use in the GUI component
	def get_query( query ):
		# Query values may be things like
		#	- Company name
		#	- Company ticker
		#	- Stock price at time of purchase
		#	- Derivative transaction code
		#	- Etc.
	
	# Information relevant to the analysis of current filing but will not be stored
	def get_all_insider_trading_history_information( stock_ticker ):
		# RETURN: TEXT ARRAY
		
		# Returns an array of all insider trading history info:
		#	- Average insider buying per year over the last 5 years (starting from filings a month ago)
		#	- Array of all company direct purchases for the past year
		#	- Array of all company direct sales for the past year
		
		# ALTERNATIVE, just save all
		# information as variables within the class, e.g.:
		#	- self.average_yearly_buys = get_yearly_buys()
		# and return nothing
	
	# Exports the entire table to excel for analysis in R Studio
	def export_information_table_to_excel( name_of_file ):
		# Creates an excel file with all the cells filled saved as the name_of_file.xml
		