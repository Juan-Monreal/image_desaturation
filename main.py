import cv2
import numpy as np


images = ['example.jpg', '00-puppy.jpg','avocado.jpg', 'flowers.jpg', 'iris_setosa.jpg']
path = 'data/'
scaleR = 0.299
scaleG = 0.587
scaleB = 0.114
scale = 255
percent = 0.3

for image in images:
	img = cv2.imread(path + 'images/' + image)
	# separate b,g,r
	b, g, r = cv2.split(img)
	b = b.astype(np.float32)
	g = g.astype(np.float32)
	r = r.astype(np.float32)

	scale = scaleR * r + scaleG * g + scaleB * b
	# convert to cmyk
	# see
	# https://stackoverflow.com/questions/14088375/how-can-i-convert-rgb-to-cmyk-and-vice-versa-in-python/41220097
	# https://www.codeproject.com/Articles/4488/XCmyk-CMYK-to-RGB-Calculator-with-source-code
	c = 1 - r / scale
	m = 1 - g / scale
	y = 1 - b / scale
	k = cv2.min(cv2.min(c, m), y)
	c = scale * (c - k) / (1 - k)
	m = scale * (m - k) / (1 - k)
	y = scale * (y - k) / (1 - k)

	# desaturate neighbors of G which are C,Y
	c = cv2.multiply(c, percent)
	y = cv2.multiply(y, percent)

	# convert back to bgr
	r = scale * (1.0 - c / scale) * (1.0 - k)
	g = scale * (1.0 - m / scale) * (1.0 - k)
	b = scale * (1.0 - y / scale) * (1.0 - k)
	r = r.clip(0, 255).astype(np.uint8)
	g = g.clip(0, 255).astype(np.uint8)
	b = b.clip(0, 255).astype(np.uint8)
	img_desat = cv2.merge([b, g, r])

	# save result
	cv2.imwrite(path + 'saves/' + image + '_desaturation_03.jpg', img_desat)

	# cv2.imshow('img', img)
	# cv2.imshow('img_desat', img_desat)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()
print('Done')
