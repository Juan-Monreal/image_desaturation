import cv2 as cv
import numpy as np


class DesaturateRgb:

	sCol = 0.3

	def __init__(self):
		pass

	def setup(self, arg, im):
		return "DOES_RGB"
		pass

	def run(self, ip):
		#Iterate over all pixels
		for v in range(ip.getHeight()):
			for u in range(ip.getWidth()):
				#get int-packed color pixel
				c = ip.get(u, v)
				#Extract RGB componets from color pixel
				r = c
				g = c
				b = c
				# Compute equivalent gray value
				y = 0.299 * r + 0.587 * g + 0.114 * b
				#linearly interpolate (yyy) <-> (rgb)
				r = int( y + self.sCol * (r - y) )
				g = int( y + self.sCol * (g - y) )
				b = int( y + self.sCol * (b - y) )
				#reassemble color pixel
				c = "something"
				ip.set(u, v, c)

		pass
