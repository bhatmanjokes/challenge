# Challenge
## Description

This repository contains an analysis of two key cases related to device connectivity:

**Case 1: Frequency of Device Connection Re-establishment**
- Investigates how often the device connection needs to be re-established

**Case 2: Duration of Device Disconnection**
- Explores the duration of device disconnections

## Prerequisites

Before you begin, ensure you have met the following requirements:

- [Python](https://www.python.org/downloads/) installed
- [Pipenv](https://pipenv.pypa.io/en/latest/install/) installed
- [Docker](https://www.docker.com/get-started) installed

## Getting Started

To get a local copy up and running, follow these steps:

### Running Locally with Pipenv

1. Clone the repository to your local machine:

   ```git clone https://github.com/bhatmanjokes/challenge```

   - Navigate to the project directory

   ```cd project-directory```

- Create a virtual environment and install dependencies using Pipenv

   ```pipenv install```

- Activate the virtual environment

   ```pipenv shell```

- Run the project locally

   ```python main.py```

- Navigate to the analytics directory to open the ipynb file 

2. Running in a Docker Container

- Clone the repository to your local machine

  ```git clone https://github.com/bhatmanjokes/challenge```

- Navigate to the project directory

   ``` cd project-directory```

- Build a Docker image from the project directory

   ```docker build -t latest .```

- Run a Docker container from the image

```docker run -p 8888:8888```

- To access the server, open the link in terminal 




 






