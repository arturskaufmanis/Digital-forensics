"""
This program extracts metadata for forensic purposes 
from given file.
"""

import os
import time
from pathlib import Path
from pprint import pprint

def extract_file_metadata(file_path):
    """ 
    Extracts metadata from a given file using
    os and pathlib libraries.

    Args:
        file_path (str): Path to the file to analyze.

    Returns:
        dict: Dictionary with file metadata.
    """
    try:
        # Create a path object for pathlib usage
        path_obj = Path(file_path)

        # Verify whether file exists
        if not path_obj.exists():
            return {"Error": f"File not found: {file_path}"}
        
        # Receive file statistics by using os
        file_stats = os.stat(file_path)

        # Extract and organise metadata by using pathlib and os
        metadata = {
            "file_name": path_obj.name,
            "file_path": str(path_obj.absolute()),
            "file_type": path_obj.suffix or "No extension",
            "file_size_bytes": file_stats.st_size,
            "file_size_kb": round(file_stats.st_size / 1024, 2),
            "status_change_date": time.ctime(file_stats.st_ctime),
            "modification_date": time.ctime(file_stats.st_mtime),
            "access_date": time.ctime(file_stats.st_atime),
            "permissions": oct(file_stats.st_mode)[-3:],
            "is_file": path_obj.is_file(),
            "is_directory": path_obj.is_dir(),
        }

        return metadata
    
    except Exception as e:
        return {"Error": f"Error extracting metadata: {str(e)}"}

def main():
    """ 
    Main function to run the metadata extraction tool.
    """

    print("File Metadata Extraction Tool")

    # User input for file path
    file_path = input("Enter the path to the file: ").strip()

    # Extract metadata from the specified file
    metadata = extract_file_metadata(file_path)

    # Print the extracted metadata
    print("\n" + "=" * 50)
    print("Extracted Metadata:")
    print("=" * 50)
    pprint(metadata)

if __name__ == "__main__":
    main()