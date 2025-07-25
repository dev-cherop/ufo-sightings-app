UFO-SIGHTINGS-APP
Uncover Mysteries, Inspire Wonder, Explore the Unknown

Built with the tools and technologies:

Table of Contents
Overview

Getting Started

Prerequisites

🛠️ Installation
Build the ufo-sightings-app from its source and set up its dependencies:

Clone the repository:

Bash

> git clone https://github.com/dev-cherop/ufo-sightings-app
Navigate to the project directory:

Bash

> cd ufo-sightings-app
Install the dependencies:

Using Docker (Recommended for a consistent environment):

Bash

> docker build -t dev-cherop/ufo-sightings-app .
Using Pip (for direct Python environment setup):

Bash

> pip install -r requirements.txt
▶️ Usage
Once installed, you can launch the application:

Using Docker:

Bash

docker run -it {image_name}
(Replace {image_name} with dev-cherop/ufo-sightings-app or your chosen image tag)

Using Pip:

Bash

python {entrypoint}
(Replace {entrypoint} with the actual entry point script, e.g., python app.py if your main script is app.py)

🐛 Testing
Ensure everything is working perfectly by running the tests. The ufo-sightings-app utilizes the {test_framework} test framework.

Using Docker:

Bash

echo 'INSERT-TEST-COMMAND-HERE'
(You'll need to replace 'INSERT-TEST-COMMAND-HERE' with the actual Docker command to run your tests, e.g., docker run {image_name} pytest)

Using Pip:

Bash

pytest

pytest
