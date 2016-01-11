'''
DATA: 
	1. Data can be taken from the internet or your local machine
	2. Formats currently supported are:
		2.1 JSON - STILL TO INITIATE AS I WANT THIS TO WORK FROM MULTIPLE SOURCES: BLOOMBERG, YAHOO, QUANDL
		2.2 CSV - INITIATED
		
DATABASE: 
	1. CREATE AND CONFIGURE TABLE
	2. ADD DATA
	3. RUN ANALYSIS
	4. SAVE / TRUNCATE

ERROR CODES:
	[001]: Database did not submit data in the correct manner
	[002]:
	[003]:
	[004]:
'''

import MySQLdb
import math
import Quandl
import numpy as np

class DataScraper(object):
	
	def __init__(self,data_location,source,open,close,high,low,volume):
		''' 
		data_location: [STRING] __filepath__ -- required
		source: [STRING] __source__ = "Remote"; "Local" -- required
		database: [BOOLEAN] TRUE,FALSE -- Default=True -- required -- I always want to store in SQL database to make the rest of the script standardised
		open: [BOOLEAN] TRUE,FALSE -- Default=False -- optional
		close:[BOOLEAN] TRUE,FALSE -- Default=False -- optional
		high: [BOOLEAN] TRUE,FALSE -- Default=False -- optional
		low: [BOOLEAN] TRUE,FALSE -- Default=False -- optional
		volume: [BOOLEAN] TRUE,FALSE -- Default=False -- optional
		'''
		self.data_location = data_location
		self.source = source
		self.database = True
		self.open == True if(self.open != False) else self.open = False
		self.close == True if(self.close != False) else self.close = False
		self.high == True if(self.high != False) else self.high = False
		self.low == True if(self.low != False) else self.low = False
		self.volume == True if(self.volume != False) else self.volume = False
	
	def config_sql_database(self, number_of_columns):
		'''
		Description: A function to set up and initiate a database on the local machine
		'''
		try:
			#connect to MySQL and create datatable with specified columns
		except: 
			#Add more to this handler
			print("Issue creating database with details provided.")
			
		
	def add_data_to_sql_database(self):
		'''
		Description: 
		'''
		try:
			#Get the data from the source and add to table created from add_data_to_sql_database
		except: 
			#Add more to this handler
			print("Issue adding data to database. Database has been created though.")
		
	def get_data_to_sql_db(self):
		'''
		Description: 
		'''
		if(self.source == "Remote"):
			#GET THE DATA FROM QUANDL (BLOOMBERG, YAHOO ...)
		elif (self.source == "Local"):
			try:
				with open(self.data_location,'r') as data:
					number_of_columns_to_read = sum([self.open,self.close,self.high,self.low, self.volume])
					config_database(number_of_columns_to_read) #Create the database with the number of columns specified
					for column in range(0,number_of_columns_to_read):
						#data(column)
						#add data to the database
			except:
				#Add more to this handler
				print("Issue collecting data from the local path provided.")
		return True
			
				


'''
TESTING IF THIS CLASS WORKS HERE
'''

if __name__ == "__main__":
	
	#CONFIGURATION
	OPEN = True
	CLOSE = True
	HIGH = True
	LOW = True
	VOLUME = True
	
	#SPECIFY WHERE THE DATA IS AND SOURCE
	DATA_LOCATION = "C:\Users\Andrew\Desktop\PhD\AlgoTrade\AlgoTrade\DataScraper\data.csv"
	SOURCE = "Local"
	
	DATA_OBJECT = DataScraper( DATA_LOCATION, SOURCE, OPEN, CLOSE, HIGH, LOW, VOLUME )
	DATA_OBJECT.get_data_to_sql_db() #Insert data to MySQL database
	if (DATA_OBJECT.get_data_to_sql_db()):
		print("Completed...")
	elif(!DATA_OBJECT.get_data_to_sql_db()):
		print("Error: [001]")
