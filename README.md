# ynab-conversions
Convert different financial institutions' CSV statement formats into YNAB-importable CSVs.


## Venmo
To use, download a CSV statement from the Venmo website and enter your public Venmo name (NOT your handle) in the `[YOUR NAME HERE]` section of the script.
Since Venmo transactions can be from you or to you, this ensures the payee field is correct.

## Schwab
To use, download a CSV statement from the [Schwab website](https://www.schwab.com/).

## Cash
To use, download a CSV statement from the [Cash App website](https://cash.app/).
=======
```
$ python venmo-to-ynab.py your_statement.csv
```

## Schwab
To use, download a CSV statement from the [Schwab website](https://www.schwab.com/).
```
$ python schwab-to-ynab.py your_statement.csv
```

## Cash
To use, download a CSV statement from the [Cash App website](https://cash.app/).
```
$ python cash-to-ynab.py your_statement.csv
```