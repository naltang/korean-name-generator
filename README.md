# A random Korean name generator

Statistically plausible random Korean name generator.
It generates a list of names to the standard output, with several options.
It uses separate CSV files to read frequencies of family and given names.

## How to use

```
korean-name-generator.py [-h] [-f FAMILY-NAMES] [-g GIVEN_NAMES] [-c COUNT] [-s SEX] [-d DELIMITER]

options:
  -h, --help            show this help message and exit
  -f FAMILY-NAMES, --family-names FAMILY-NAMES
                        family names population CSV file, default=family-names.csv
  -g GIVEN-NAMES, --given-names GIVEN-NAMES
                        given names population CSV file, default=given-names.csv
  -c COUNT, --count COUNT
                        number of names to generate, default=1
  -s SEX, --sex SEX     sex of names to generate, default=whatever
  -d DELIMITER, --delimiter DELIMITER
                        use DELIMITER for name delimiter, default="\n"
```

### Examples
__Warning:__
_Actual output may be different, due to the nature of randomness._
_Names shown in these examples have no relation with real persons of these names._

+ No option gives you just one random name
```
$korean-name-generator.py
박창욱
```

+ To generate 5 random male names from diffferent frequency files
```
$korean-name-generator.py -f ex-family.csv -g ex-given.csv --count 5 -s female
홍그여자
그성그여자
홍저여자
그성저여자
이성그여자

```

+ To generate 10 random female names separated by a comma from different frequency files
```
$korean-name-generator.py --sex male -d , -c 10 -f ex-family.csv -g ex-given.csv
이성그남자,홍길동,그성그남자,홍그남자,홍저남자,홍길동,홍길동,홍이남자,홍그남자,저성길동
```

## License
MIT license

## Data Source
Family name data in _family-names.csv_ were retrieved from
https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1IN15SD
and _given-names.csv_ from https://efamily.scourt.go.kr/
