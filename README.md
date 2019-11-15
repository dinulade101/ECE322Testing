# 291-Mini-Project-I
A command line application for ride sharing using SQLite as our database for CMPUT 291 Mini-Project-I

## Testing

To run all unittests
```
python3 -m unittest discover
```

To run a specific test suite
```
python3 -m unittest test.test_membercommand
```

To run the test coverage
```
pip3 install coverage
coverage run -m unittest discover
```

To view the results and generate html page of results
```
coverage report -m 
coverage html
```

## Instructions
To Install:
```
./install.sh
```

To run:
```
python3 main.py prj.db
```

To run with your own database file:
```
python3 main.py <path_to_database>
```

## Authors
* Kenta Watanabe Tellambura
* Danish Dua
* Dinula De Silva
