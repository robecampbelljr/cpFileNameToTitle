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
		title_was_changed = False
		file = folder.Items().Item(i)
		# Load the metadata of the video file
		video = EasyMP4(file_path)
		keys = video.keys()
		if len(keys) < 1:
			# Create a new dictionary with the existing metadata
			new_metadata = dict(video)
			# Add the new key-value pair
			new_metadata['title'] = 'Temp Title'
			# Update the existing metadata with the new dictionary
			video.update(new_metadata)
		title = video['title'][0]
		if title != new_title:
			# Change the title
			video['title'] = new_title
			# Save the changes
			video.save()
			title_was_changed = True
		return title_was_changed

def main(folder_path):
	total_files = 0
	mp4_files = 0
	changed_files = 0
	for root, dirs, files in os.walk(folder_path):
		for file in files:
			file_path = os.path.join(root, file)
			new_title = file.rstrip(".mp4")
			if ".mp4" in file:
				mp4_files += 1
				title_change = get_file_details(file_path, new_title)
				if title_change == True:
					changed_files += 1
			total_files += 1
	print(f"Total Files Processed: {total_files}\nMp4 Files Found: {mp4_files}\nTitles Changed: {changed_files}")

if __name__ == "__main__":
	folder_path = input("Enter your media folder's path: ")
	main(folder_path)