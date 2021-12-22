# Dices
Create and throw dices with easiness

- [X] No code
- [X] Dices name custom
- [X] Dices faces custom
- [X] Infinit dices creation
- [X] Infinit faces for each dice

## Download
```
git clone https://github.com/Neotoxic-off/Dices
cd Dices
chmod +x dices.py
echo "to start the configuration edit 'settings.json'"
```

## Usage
```
python3 dices.py
```

#### Result
```
dice 1: 4
dice 2: 4
dice 3: 8
dice 4: 4
```

## Settings Configuration

```JSON
{
    "dices" : [
        {
            "name" : "dice name",
            "content" : [
                "face 1",
                "face 2"
                ...
            ]
        }
    ]
}
```
