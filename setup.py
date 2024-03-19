from setuptools import setup, find_packages

setup(
    name="NbaSeasonStats",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "selenium",
        "matplotlib"
    ],
    entry_points={
        "console_scripts": [
            "NbaSeasonStats = nba_stats:main"
        ]
    },
)
