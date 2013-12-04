import urllib2
import webbrowser

class WebsiteLoader():
	
	def __init__( self, htm_address ):
		self.htm_address = htm_address
		self.document_links = []
	
	def get_all_document_links( self ):
		webpage =  urllib2.urlopen( 'http://www.sec.gov/%s' % self.htm_address )
		for line in webpage:
			if "href=" in line and "<td scope=" in line:
				self.link_strt = line.index( "href=\"" ) + len( "href=\"" )
				self.link_end = line.index( "\"" , self.link_strt )
			   	self.document_links.append( line[ self.link_strt : self.link_end ] )
		return self.document_links
	
	def open_form_page( self ):
		webbrowser.open_new( 'http://www.sec.gov/%s' %self.document_links[0] )