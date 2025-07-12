# Password Generator & Strength Checker

A simple command-line tool to generate strong random passwords and check password strength.

## Features
- Generate random passwords with custom length and special characters
- Check the strength of any password
- Choose which special characters to include

## Usage

To generate a password:

```bash
python main.py --generate --length 12 --special_chr "@" "#" "$"
```

Parameter details:
- `--generate` or `-cr`: Generate a random password
- `--length` or `-len`: Password length (default: 10)
- `--special_chr` or `-sch`: Special characters to include (choose from: @ # $ % ! & +) (default = @)

To check password strength:

```bash
python main.py --strength --password YOUR_PASSWORD
```

- `--strength` or `-strn`: Check password strength
- `--password` or `-pass`: The password to check

## Examples


Generate a 16-character password with special characters:
```bash
python main.py --generate --length 16 --special_chr "@" "#" "$"
```

Check the strength of a password:
```bash
python main.py --strength --password MyPassword123!
```

You can also generate a password and check its strength in one command:
```bash
python main.py --generate --length 16 --special_chr "@" "#" "$" --strength
```
This will show you the generated password and its strength report immediately.

## Author
Made with ❤️ by Ali
