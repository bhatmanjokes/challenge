import re

class JournalEntryParser:
    def __init__(self, entry):
        # Initialize class attributes
        self.machine_id = None
        self.timestamp = None
        self.message = None
        self.error = ''

        # Split the journal entry into lines and process each line
        lines = entry.split('\n')
        for line in lines:
            if line.startswith('_MACHINE_ID='):
                self.machine_id = line.split('=')[1]  # Extract machine ID
            elif line.startswith('__REALTIME_TIMESTAMP='):
                self.timestamp = line.split('=')[1]   # Extract timestamp
            elif line.startswith('MESSAGE='):
                # Remove timestamp from the message and store it
                stripped_line = re.sub(r'\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}', '', line)
                self.message = stripped_line.split('=')[1]
                if 'action' in stripped_line:
                    self.error = stripped_line  # Store action-related info
                elif re.search(r'\b(error|failed)\b', stripped_line, re.IGNORECASE):
                    self.error = stripped_line  # Store error-related info

    def get_data(self):
        # Return the parsed data as a list
        return [self.machine_id, self.timestamp, self.message, self.error]
