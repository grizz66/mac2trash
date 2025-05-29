
#!/usr/bin/env python3
"""
mac2trash: Un-Apple your files.
Removes macOS metadata and junk files from a directory or zip archive.
"""

import os
import sys
import shutil
import zipfile
import argparse

JUNK_PATTERNS = [
	'.DS_Store', '__MACOSX', '._*', 'Icon\r', '.VolumeIcon.icns', '.fseventsd', '.Spotlight-V100'
]

def is_junk(name):
	for pattern in JUNK_PATTERNS:
		if pattern.endswith('*'):
			if name.startswith(pattern[:-1]):
				return True
		elif pattern in name:
			return True
	return False

def clean_directory(path):
	trash_count = 0
	for root, dirs, files in os.walk(path, topdown=False):
		for name in files:
			full_path = os.path.join(root, name)
			if is_junk(name):
				os.remove(full_path)
				print(f"🗑️ Removed file: {full_path}")
				trash_count += 1
		for name in dirs:
			full_path = os.path.join(root, name)
			if is_junk(name):
				shutil.rmtree(full_path, ignore_errors=True)
				print(f"🗑️ Removed directory: {full_path}")
				trash_count += 1
	return trash_count

def clean_zip(zip_path, output_path):
	temp_dir = zip_path + '_tmp'
	with zipfile.ZipFile(zip_path, 'r') as zip_ref:
		zip_ref.extractall(temp_dir)
	count = clean_directory(temp_dir)
	with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as new_zip:
		for root, _, files in os.walk(temp_dir):
			for file in files:
				full_path = os.path.join(root, file)
				arcname = os.path.relpath(full_path, temp_dir)
				new_zip.write(full_path, arcname)
	shutil.rmtree(temp_dir)
	print(f"✅ Cleaned zip written to: {output_path}")
	return count

def main():
	parser = argparse.ArgumentParser(
		prog='mac2trash',
		description="Remove macOS metadata from files and folders",
		epilog="Because your cross-platform friends don't want your .DS_Store files."
	)
	parser.add_argument("path", help="Path to directory or .zip file")
	args = parser.parse_args()

	if not os.path.exists(args.path):
		print("❌ Path does not exist.")
		sys.exit(1)

	if os.path.isdir(args.path):
		count = clean_directory(args.path)
		print(f"✅ Removed {count} junk items from folder.")
	elif zipfile.is_zipfile(args.path):
		output = args.path.replace('.zip', '_clean.zip')
		count = clean_zip(args.path, output)
		print(f"✅ Removed {count} junk items from archive.")
	else:
		print("❌ Unsupported file type.")
		sys.exit(1)

if __name__ == "__main__":
	main()
