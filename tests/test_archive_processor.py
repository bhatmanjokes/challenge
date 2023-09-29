import os
import pytest
from parser.process_archive import ProcessArchive

@pytest.fixture
def test_paths():
    # Change the working directory to the directory containing the test script
    test_script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(test_script_dir)

    # Temporary paths for testing
    test_zip_path = 'challenge/data/smartconnect-db344f-20230922145036.zip' #update path
    test_csv_path = 'challenge/data/tunnel_service_data.csv' #update path
    yield test_zip_path, test_csv_path
    # Clean up: Remove the test CSV file
    if os.path.exists(test_csv_path):
        os.remove(test_csv_path)

def test_process_archive(test_paths):
    test_zip_path, test_csv_path = test_paths

    # Verify that the ZIP file exists
    if not os.path.exists(test_zip_path):
        pytest.fail(f"ZIP file not found: {test_zip_path}")

    # Create an instance of ArchiveProcessor
    processor = ProcessArchive(test_zip_path, test_csv_path)

    # Process the test archive
    processor.process_archive()

    # Check if the test CSV file has been created
    assert os.path.exists(test_csv_path)
