# QuickShareOne

**QuickShareOne** is an open-source utility that enables the quick creation of a QR code—containing up to 4,296 alphanumeric characters or 7,089 numeric characters (excluding spaces)—directly from a terminal.

It allows you to effortlessly and quickly transfer data—whether a string, number, or link—from your computer straight to your mobile device.

## Features

- QR Generation.
- Easy to use terminal UI.

## Requirements

- Python 3

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Azio0/QuickShareOne.git
   cd QuickShareOne
   ```
2. Install Python and PIP:
   ```bash
   sudo apt-get install python3
   sudo apt-get install python3-pip
   ```
4. Install the required Python Packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Navigate to the ```source``` folder within the ```QuickShareOne``` directory. From there, you can run ```python -m qsom.py```.

You will be presented with a welcome message and an input prompt. Once submitted, your device’s default image preview software will open with the newly generated QR code.

When a new QR code is generated, the previous one is deleted. There is no native saving capability within this codebase. If you require access to the QR code in the future, please ensure you save the temporary file elsewhere. By default, it is stored within the ```source``` folder.

## Contributing

This is an open-source project, and contributions are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the terms of the MIT license.

## Contact

For any questions or suggestions, please open an issue or contact the project maintainers.

## Donations

This project is intended to be open-source and free from cost to use. I love coding, setting a target and accomplishing it, sometimes by using pre-existing technology or creating an original approach to a problem. It excites me and gives me a sense of purpose, but it is not always easy to find the time or motivation to keep pushing forward. Donations are welcome if you wish to give something towards the work I do, but it is completely optional and is certainly not a requirement.

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/azio0)
