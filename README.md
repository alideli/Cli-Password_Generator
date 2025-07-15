# Installation

First, install the required dependencies:
```bash
pip install -r requirements.txt
```
# Password Generator & Strength Checker

A simple command-line tool to generate strong random passwords and save it and check password strength.

## Features
- Generate random passwords with custom length and special characters
- Check the strength of any password
- Choose which special characters to include
- Save generated password automaticly


## Usage

### Generate a password
```bash
python main.py --generate --length 12 --special_chr "@" "#" "$"
```
Parameters:
- `--generate` or `-cr`: Generate a random password
- `--length` or `-len`: Password length (default: 10)
- `--special_chr` or `-sch`: Special characters to include (choose from: @ # $ % ! & +) (default = @)

### Check password strength
```bash
python main.py --strength --password YOUR_PASSWORD
```
- `--strength` or `-strn`: Check password strength
- `--password` or `-pass`: The password to check

### View saved passwords
```bash
python main.py --view
```
This will show all saved passwords with their line numbers and descriptions.

### Remove a saved password by password number
First, use `--view` to see the password numbers. Then run:
```bash
python main.py --remove 2
```
This will remove the password number 2. Only one password can be removed at a time.


## Examples

Generate a 16-character password with special characters:
```bash
python main.py --generate --length 16 --special_chr "@" "#" "$"
```

Check the strength of a password:
```bash
python main.py --strength --password MyPassword123!
```

View all saved passwords:
```bash
python main.py --view
```

Remove the 3rd saved password:
```bash
python main.py --remove 3
```

Generate a password and check its strength in one command:
```bash
python main.py --generate --length 16 --special_chr "@" "#" "$" --strength
```
This will show you the generated password and its strength report immediately.

## Author
Made with ❤️ by Ali
