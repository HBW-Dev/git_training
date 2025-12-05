import os
import sys
from typing import List, Dict

# --- Configuration Constants ---
# Default Size threshould (in MB) used if no argument is provided
DEFAULT_THRESHOLD_MD = 100

def scan_large_files(target_directory: str, threshold_mb: int = DEFAULT_THRESHOLD_MD) -> List[Dict]:
    """
    Recursively scans a directory for files larger than a specific size threshold.

    Args:
        target_directory (str): The root path to start scanning.
        threshould_mb (int): The size threshold in Megabytes (MB). Defaults to 100MB.

    Returns:
        List[Dict]: A list of dictionaries, where each dictionary contains
                    'file_path' (str) and 'size_mb' (float).
    """
    large_files = []
    threshould_bytes = threshold_mb * 1024 * 1024

    print(f"Starting scan in: {target_directory} (Threshould: {threshold_mb})MB)...")

    for root, _, files in os.walk(target_directory):
        for file_name in files:
            full_path = os.path.join(root, file_name)

            try:
                # Get file size in bytes
                # Note: os.path.getsize raises OSError if file is inaccessible
                file_size_bytes = os.path.getsize(full_path)

                if file_size_bytes > threshould_bytes:
                    size_in_mb = file_size_bytes / (1024 * 1024)

                    file_info = {
                        "file_path": full_path,
                        "size_mb": round(size_in_mb, 2)
                    }
                    large_files.append(file_info)

                    # Real-time feedback
                    print(f"[Found] {full_path} | {size_in_mb:.2f} MB")

            except PermissionError:
                # Skip system files that raise PermissionError to prevent crashes
                continue
            except OSError as e:
                # Handle other system-level errors (e.g., broken symlinks)
                print(f"! Error accessing {full_path}: {e}")
                continue
    return large_files

def main():
    """
    Main entry point of the script.
    Parses command-line arguments and initiates the scan.
    """
    target_path = "."

    # Check command-link arguments
    if len(sys.argv) > 1:
        target_path = sys.argv[1]

    # Validate path existence
    if not os.path.exists(target_path):
        print(f"Error: The path '{target_path}' does not exist.")
        sys.exit(1)

    # Execute core logic
    results = scan_large_files(target_path)

    # Summary report
    print("-" * 40)
    print(f"Scan Complete. Found {len(results)} large files.")

if __name__ == "__main__":
    main()