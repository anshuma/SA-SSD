import mmcv
import os
import numpy as np
def draw_bounding_boxes(img_idx, annotations_folder, images_folder, saveto):
	# Load image
	image_path = os.path.join(images_folder, '%06d.png' % img_idx)
	if not os.path.exists(image_path):
		print(f"The image file {image_path} does not exist.")
	else:
		# Load the image
		image = mmcv.imread(image_path)

		# Check if the image is loaded (not empty)
		if image is None or image.size == 0:
			print(f"Failed to load the image from {image_path}.")
		else:
			image = mmcv.imread(image_path)

			# Path to the annotation file
			annotation_path = os.path.join(annotations_folder, '%06d.txt' % img_idx)
			print('annotation_path',annotation_path)
			# Check if the annotation file exists
			if not os.path.exists(annotation_path):
				print(f"No annotation for image {img_idx}")
				return

			# Read annotations
			with open(annotation_path, 'r') as f:
				lines = f.readlines()

				bboxes = []
				for line in lines:
					parts = line.strip().split(' ')
					name = parts[0]
					bbox = [float(x) for x in parts[4:8]]
					score = float(parts[-1])

					# Append bbox and score if you want to display the score
					bboxes.append(bbox + [score])

			bboxes_np = np.array(bboxes, dtype=np.float32) 
			# Draw bounding boxes on the image. The color and thickness can be customized.
			image_with_boxes = mmcv.imshow_bboxes(image, bboxes_np, colors='green', top_k=-1, thickness=2, show=False)

			# Save or display image
			mmcv.imwrite(image_with_boxes, os.path.join(saveto, '%06d.png' % img_idx))
			# or to just display the image use:
			#mmcv.imshow(image_with_boxes, win_name=str(img_idx), wait_time=0)

# Example usage
draw_bounding_boxes(img_idx=6, # replace with your actual image index
                    annotations_folder='/workspace/git/SA-SSD/test_anno', 
                    images_folder='/workspace/git/SA-SSD/data/testing/image_2', 
                    saveto='/workspace/git/SA-SSD/test_vis')
draw_bounding_boxes(img_idx=8, # replace with your actual image index
                    annotations_folder='/workspace/git/SA-SSD/test_anno', 
                    images_folder='/workspace/git/SA-SSD/data/testing/image_2', 
                    saveto='/workspace/git/SA-SSD/test_vis')
draw_bounding_boxes(img_idx=19, # replace with your actual image index
                    annotations_folder='/workspace/git/SA-SSD/test_anno', 
                    images_folder='/workspace/git/SA-SSD/data/testing/image_2', 
                    saveto='/workspace/git/SA-SSD/test_vis')
draw_bounding_boxes(img_idx=15, # replace with your actual image index
                    annotations_folder='/workspace/git/SA-SSD/test_anno', 
                    images_folder='/workspace/git/SA-SSD/data/testing/image_2', 
                    saveto='/workspace/git/SA-SSD/test_vis')
