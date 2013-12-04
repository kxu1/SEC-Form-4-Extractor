from SecForm4_DataExtractor import *
from SecForm4_WebsiteLoader import *
from threading import Timer
import time


already_viewed = []


# 1) Stock ticker symbol
# 2) Type of stock

def form_search( ):

	response = [ ]
	filing = [ ]

	# Gets 40 most recent filings and appends the most relevant information
	webpage = urllib2.urlopen( 'http://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent' )
	for line in webpage:
		if line.startswith( "<td nowrap" ):
			response.append( line.strip( '<td nowrap="nowrap">' ) )

	# for line in response:
	# 	print line

	# Returned format looks like:
	# 1) file type for company 1s
	# 2) html web address + random junk + txt web address for company 1
	# 3) date and time for company 1
	# 4) file number if available for company 1
	# 5) file type for company 2...

	for x in range( 40 ):

		# Gets the filing type of a recent filing and adds it to the "filing" list
		index = response[ x*4 ].index( "<" )
		file_type = response[ x*4 ][ 0:index ]

		# Organizes the other filing information into a list with the format:
		# [File Type, HTML web address, TXT web address, File Date, File Time, File Number]
		if file_type == "4":	

			# Check to see if there is a filing number, if so, it is a reporting filing so keep going
			# If an issuer filing, go back to the top of for loop
			try:

				file_number_strt = response[ x*4+3 ].index( "filenum=" ) + 8
				file_number_end = response[ x*4+3 ].index( "&" , file_number_strt )
				file_number = response[ x*4+3 ][ file_number_strt : file_number_end ]
			
			except: continue	
		
			# Separates line into extracted html and txt web addresses to access the full filing
			# print response[x*4+1]
			response[ x*4+1 ] = response[ x*4+1 ].split( ">[html]</a><a " )

			# Finds the indexes of quotation around the link for both html and txt
			for y in range( 2 ):

				link_strt = response[ x*4+1 ][ y ].index( "\"" ) + 1
				link_end = response[ x*4+1 ][ y ].index( "\"" , link_strt )
				response[ x*4+1 ][ y ] = response[ x*4+1 ][ y ][ link_strt : link_end ]

			html_web_address = response[ x*4+1 ][ 0 ]
			txt_web_address = response[ x*4+1 ][ 1 ]

			# Separates line into date and time 
			response[ x*4+2 ] = response[ x*4+2 ][ :-6 ].split( "<br>" )
			file_date = response[ x*4+2 ][ 0 ]
			file_time = response[ x*4+2 ][ 1 ]

			# Creates a "filing" list with the above information
			filing = [ file_type , html_web_address , txt_web_address , file_date , file_time , file_number ]
		
			# Uses the filing to extract other information through the txt address
			company = DataExtractor( filing )
			table =	company.get_all_transactions()
			for transaction in table:
				if transaction[0] == "nonDerivativeTransaction":
					if transaction[3].upper() == "P":
						if filing[5] not in already_viewed:
							html = WebsiteLoader( filing[1] )
							html.get_all_document_links()
							html.open_form_page()
							print "\nThe ticker: " + company.get_reporting_information()[0]
							print "The company: " + company.get_reporting_information()[1]
							print "The reporting filer: " + company.get_reporting_information()[2]
		
							already_viewed.append( filing[5] )
			
	print already_viewed

def execute_form_search(): 
    while True:
    	
    	try:
			form_search()
			time.sleep(60)
			
	except:
			print "error"
			
# execute_form_search()

			