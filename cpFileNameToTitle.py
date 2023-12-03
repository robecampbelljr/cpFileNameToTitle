import os
import win32com.client
from mutagen.easymp4 import EasyMP4

	# This line starts the definition of a function named get_file_details that takes a parameter file_path.
def get_file_details(file_path, new_title):
	# Here, we create an instance of the Windows Shell Application using win32com.client.Dispatch. This allows us to interact with the Windows Shell.
	shell = win32com.client.Dispatch("Shell.Application")
	# We obtain a reference to the folder containing the file using shell.Namespace. os.path.dirname(file_path) extracts the directory path from the full file path.
	folder = shell.Namespace(os.path.dirname(file_path))
	# This line extracts the file name from the full file path using os.path.basename.
	file_name = os.path.basename(file_path)
	for i in range(folder.Items().Count):
		file = folder.Items().Item(i)
		# Load the metadata of the video file
		video = EasyMP4(file_path)
		keys = video.keys()
		print("Available keys:", keys)
		if len(keys) < 1:
			print("There are no keys available. Adding key...")
			# Create a new dictionary with the existing metadata
			new_metadata = dict(video)
			# Add the new key-value pair
			new_metadata['title'] = '1'
			# Update the existing metadata with the new dictionary
			video.update(new_metadata)
			print(f'"title" has been added to keys...')
		else:
			print("Keys available...")
		title = video['title']
		print(f"Title Before: {title}")
		# Change the title
		video['title'] = new_title
		# Save the changes
		video.save()
		print(f"Title After: {video['title']}")
		return title



def main(folder_path):
	for root, dirs, files in os.walk(folder_path):
		for file in files:
			file_path = os.path.join(root, file)
			new_title = file.rstrip(".mp4")
			if ".mp4" in file:
				title = get_file_details(file_path, new_title)
			else:
				print("This is not a video file.")

if __name__ == "__main__":
	folder_path = input("Enter your media folder's path: ")  # Change this to the path of your folder
	main(folder_path)