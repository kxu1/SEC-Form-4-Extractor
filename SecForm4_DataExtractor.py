import urllib2


# Class DataExtractor used to extract data from Form 4 filings		
class DataExtractor():
	
	#COMMENT THIS LATER
	NULL = ""
	OWNER_QUERIES = ["isDirector", "isOfficer", "isTenPercentOwner", "isOther"]
	LIST_ACTION = ["Transaction", "Holding"]
	REPORTING_TAGS = ["issuerTradingSymbol", "issuerName", "rptOwnerName"]
	SECURITIES_LIST = ["nonDerivative", "derivative"]
	SECURITIES_QUERIES = dict()
	SECURITIES_QUERIES["nonDerivativeTable"] = ["securityTitle", "transactionDate", "transactionCode", "transactionShares",
													 "transactionPricePerShare", "transactionAcquiredDisposedCode", 
													 "sharesOwnedFollowingTransaction", "directOrIndirectOwnership", 
													 "natureOfOwnership"]	
		   
	SECURITIES_QUERIES[ "derivativeTable" ] = ["securityTitle", "conversionOrExercisePrice", "transactionDate", 
													"transactionCode", "transactionShares", "transactionPricePerShare", 
													"transactionAcquiredDisposedCode", "exerciseDate", "expirationDate",
													"underlyingSecurityShares", "sharesOwnedFollowingTransaction",
													"directOrIndirectOwnership", "natureOfOwnership"]
	
	# Initializes the function with the filing information extracted from the site
	def __init__(self, filing):
		
		# Sets the text you search through to be the page of the insider buy
		self.text = urllib2.urlopen('http://www.sec.gov' + filing[2]).read()
		
		# If the person filing is an officer (e.g. CEO, CFO), this will help identify which type it is later
		self.officer_title = DataExtractor.NULL
														 
		
	# Attempt to find the text within a section "query" from a specified text
	def get_query(self, query, text):
		
		# If the query tags are found within the text, return the value found between the two tags
		try: 
			self.query_strt = text.index("<%s>" %query) + len("<%s>" %query)
			self.query_end = text.index("</%s>" %query, self.query_strt)
			self.output = text[self.query_strt:self.query_end]
			return self.output
		
		# Otherwise, if not found, return empty string	
		except: return DataExtractor.NULL
	
	# <footnoteId id="F1"/> DO THIS SHIT LATER
	def get_footnote_id(self, input):
		
		try:
			self.footnote_id_strt = input.index("<footnoteId id=\"") + len("<footnoteId id=\"")
			self.footnote_id_end = input.index("\"/>" , self.footnote_id_strt)
			self.output = input[self.footnote_id_strt:self.footnote_id_end]
			return self.output
			
		except: return DataExtractor.NULL
	
	# Determines if a footnote is within a certain block of text	
	def footnote_is_in(self, input):
		
		if "footnote" in input: return True
		else: return False	
		
	# Gets footnote itself
	def get_footnote(self, id, text):
		
		self.footnote_strt = text.index("<footnote id=\"%s\">" %id) + len("<footnote id=\"%s\">" %id)
		self.footnote_end = text.index("</footnote>", self.footnote_strt)
		self.footnote = text[self.footnote_strt:self.footnote_end]
		return self.footnote
	
	# Determines if a "value" tag is within a certain block of text 	
	def value_is_in(self, input):
		
		if "value" in input: return True
		else: return False
	
	# Get value between the value tags
	def get_value(self, input):
		
		try:
			self.output = self.get_query("value" , input)
			return self.output
			
		except: return DataExtractor.NULL

	# Returns a list of all non-derivative transactions and their details
	def get_all_transactions(self):
		
		# Table used to compile all transactions, transactions to track each insider trade	
		self.table = []
		
		# Gets the text within the blocks for both nonDerivative and Derivative sections
		for security_type in DataExtractor.SECURITIES_LIST:

			self.securities = self.get_query(security_type + "Table", self.text)
			
			# Gets the holding and transaction information listed in each section
			for action in DataExtractor.LIST_ACTION:
			
				# Since there can be multiple transactions reported per filing
				for each_row in range( self.securities.count( "<%s>" %( security_type + action ) ) ):
				
					self.transactions = [ security_type + action ]
						
					# Attempts to find each query tag and return the value
					for each_query in DataExtractor.SECURITIES_QUERIES[ security_type + "Table" ]:
	
						# If the output is not null, append the value to the table list
						# If there is a <value> tag, remove it first
						self.output = self.get_query( each_query , self.securities )
						if self.output != DataExtractor.NULL:
						
							if self.value_is_in( self.output ):
								self.value = self.get_value( self.output )
								self.transactions.append( self.value )
							else: self.transactions.append( self.output )
			
			
					# Remove the first set of transactions from the set of text you are parsing
					self.search_end = self.securities.index( "</%s>" %( security_type + action) ) + len( "</%s>" %( security_type + action) )
					self.securities = self.securities[ self.search_end : ]
			
					# Appends the set of transactions to the larger table
					self.table.append( self.transactions )
			
		return self.table
			
	def get_reporting_information( self ):
		
		self.reporting_info_table = []
		for each_query in DataExtractor.REPORTING_TAGS:
			
			self.output = self.get_query( each_query , self.text )
			self.reporting_info_table.append( self.output )
		
		return self.reporting_info_table
			
	def get_owner_status( self ):
		
		self.owner_status = [ False ] * 4
		self.count = 0
		for query in DataExtractor.OWNER_QUERIES:	
		
			# Tries to find and confirm all ownership status of the owner
			try:
				
				# If status (e.g. "isDirector") returns 1, then change value to true
				if self.get_query( query, self.text ) == "1": self.owner_status[ self.count ] = True		
				else: self.owner_status[ self.count ] = False
			
			# Sometimes, the status tags don't exist, so make false		
			except: self.owner_status[ self.count ] = False				
			
			# Increase the iteration to move on to the next space in the list owner_status
			self.count += 1	
		
		# If the reporting owner is an officer, specify which type, otherwise return NULL		
		if self.owner_status[ 1 ]: self.officer_title = self.get_query( "officerTitle" ).replace( "&amp;" , "&" )
		else: self.officer_title = DataExtractor.NULL
		
		return [ self.owner_status , self.officer_title ]