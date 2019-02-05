import sys
import csv

class CSVAvgDegPlugin:
	def input(self, filename):
		self.myfile = filename


	def run(self):
		f = open(self.myfile, 'r')
		csv_f = csv.reader(f)
		next(csv_f)
		self.edges = []
		
		for row in csv_f:
			self.edges.append(row[1:])
		
	
	def output(self, filename):
		edges = 0

		for row in self.edges:
			for i in range(0, len(row)):
				if(float(row[i]) != 0):
					edges += float(row[i])
		
		vertices = len(self.edges)
		avg_degree = (edges / vertices)
	
		print "Average degree: ", (avg_degree)
