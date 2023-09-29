from parser.process_archive import ProcessArchive

def main():
    zip_path = 'data/smartconnect-db344f-20230922145036.zip'
    csv_path = 'data/tunnel_service_data.csv'

    # Create an instance of ArchiveProcessor
    processor = ProcessArchive(zip_path, csv_path)

    # Process the archive
    processor.process_archive()

if __name__ == "__main__":
    main()
