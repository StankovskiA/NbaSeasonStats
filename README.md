# NbaSeasonStats

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Description

NbaSeasonStats is a Python package that provides functionality to retrieve and analyze NBA season statistics.

## Features

- Retrieve NBA season statistics for teams over various seasons
- Generate plots and reports on NBA season statistics
- Export NBA teams season statistics to a PDF file

## Installation
1. Clone the repository:
```git clone https://github.com/StankovskiA/NbaSeasonStats.git```

2. Change to the NbaSeasonStats directory:
```cd NbaSeasonStats```

3. Create a virtual environment:
```python -m venv .env```

4. Activate the virtual environment:
```source .env/bin/activate``` (Linux) or ```.env\Scripts\activate``` (Windows)

5. Install the package:
```pip install -e .```

## Usage
### Arguments
The package can be used from the command line. The following are the available arguments:
1. ```--start``` - The start year of the NBA season
2. ```--end``` - The end year of the NBA season
3. ```--out``` - The name of the output data file
4. ```--report``` - Whether to generate a report
5. ```--save``` - Whether to save the output file
6. ```--help``` - Get help on how to use the package


### Examples
1. To get help on how to use the package, run:
```NbaSeasonStats --help``` or ```NbaSeasonStats -h```

2. Run the package with the desired arguments:
```NbaSeasonStats --start 18 --end 23 --out nba_season_stats.csv --report True --save True```