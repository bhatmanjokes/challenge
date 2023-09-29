import zipfile
import gzip
import csv
from .journal_entry_parser import JournalEntryParser

class ProcessArchive:
    def __init__(self, zip_path, csv_path):
        self.zip_path = zip_path
        self.csv_path = csv_path
        self.header = ['MACHINE_ID', 'TIMESTAMP', 'MESSAGE', 'ERROR']

    def process_archive(self):
        csv_data = []

        try:
            # Open the ZIP archive for reading
            with zipfile.ZipFile(self.zip_path, 'r') as zip_archive:
                for file_info in zip_archive.infolist():
                    if file_info.filename.endswith('systemd.journal'):
                        with zip_archive.open(file_info) as journal_file:
                            is_gzip_compressed = journal_file.read(2) == b'\x1f\x8b'
                            journal_file.seek(0)

                            if is_gzip_compressed:
                                # If the journal file is compressed with GZIP, decompress it
                                with gzip.GzipFile(fileobj=journal_file, mode='rb') as decompressed_file:
                                    journal_data = decompressed_file.read().decode('utf-8', errors='replace')
                            else:
                                journal_data = journal_file.read().decode('utf-8', errors='replace')

                        # Split journal data into entries and process them
                        log_entries = journal_data.split('\n\n')
                        for entry in log_entries:
                            if 'tunnel.service' in entry:
                                parser = JournalEntryParser(entry)
                                csv_data.append(parser.get_data())

            # Write the parsed data to a CSV file
            with open(self.csv_path, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(self.header)  # Write the header
                writer.writerows(csv_data)  # Write the data rows

        except Exception as e:
            print("Error:", str(e))
