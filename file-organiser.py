# directory file extension and summary tool
from collections import Counter
import os


def scan_folder(folder_path="."):
  if not os.path.exists(folder_path):
    print("folder path does not exist")
    return

  extension_counts = Counter()
  total_files = 0
  total_size_kb = 0

  for item in os.listdir(folder_path):
    full_path = os.path.join(folder_path, item)
    if os.path.isfile(full_path):
      total_files += 1
      total_size_kb += os.path.getsize(full_path) / 1024
      _, ext = os.path.splitext(item)
      ext_label = ext.lower() if ext else "no_extension"
      extension_counts[ext_label] += 1

  print(f"\n.... folder summary: {os.path.abspath(folder_path)} ...")
  print(f"total files : {total_files}")
  print(f"total size  : {total_size_kb:.2f}kb\n")

  if extension_counts:
    print("breakdown by file type:")
    for ext_name, count in extension_counts.most_common():
      print(f"  {ext_name:<15} : {count} file(s)")
  else:
    print("no files found in this directory")


#running scan on directory....
scan_folder(".")
