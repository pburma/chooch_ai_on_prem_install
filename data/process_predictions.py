
import sys
import json


#Do not edit 
class_title = sys.argv[1] if sys.argv[1:] else None
score = sys.argv[2] if sys.argv[2:] else None
coordinates = sys.argv[3].split(",") if sys.argv[3:] else None
model_id = sys.argv[4] if sys.argv[4:] else None
camera_name = sys.argv[5] if sys.argv[5:] else None



if __name__ == '__main__':
	"""
	class_title - String (Eg: mask_on)
	score       - Float (Eg: 0.95265)
	model_id    - Intiger (Eg: 1023)
	camera_name - String  (Eg: camera_1)
	coordinates - List [xmin,ymin,xmax,ymax] (Eg: ['293', '136', '339', '204'])
	
	Please use these parameters and build your logic below
	"""
	print(class_title,score,model_id,camera_name,coordinates)
	