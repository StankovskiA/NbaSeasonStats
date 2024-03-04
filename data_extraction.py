from selenium.webdriver.common.by import By
from selenium import webdriver

base_url = "https://www.nba.com/stats/teams/scoring"


def fetch_scores(season, driver):
    """Fetch NBA season stats for the specified season from the NBA website."""
    url = f"{base_url}?Season=20{season}-{season + 1}"
    driver.get(url)
    # Wait for a few seconds to ensure the page is loaded
    driver.implicitly_wait(5)

    season_data = []

    try:
        # Find the table element with the specified class
        table = driver.find_element(By.CLASS_NAME, "Crom_body__UYOcU")

        # Find all rows within the table
        rows = table.find_elements(By.TAG_NAME, "tr")

        # Extract data from each row
        for row in rows:
            # Find all cells (td) in the current row
            cells = row.find_elements(By.TAG_NAME, "td")

            # Extract and print the text from each cell
            row_data = [cell.text for cell in cells]

            # Keep only Season, Team, Wins and Losses
            row_data = [f"20{season}-{season + 1}",
                        row_data[1], row_data[3], row_data[4]]

            season_data.append(row_data)

        return season_data
    except Exception as e:
        print(
            f"Failed to retrieve data for season 20{season}-{season + 1}. Error: {e}")
        return None


def scrape(start_season: str = "18", end_season: str = "23", output_file: str = "nba_season_stats.csv"):
    """Scrape NBA season stats from the NBA website and save them to a CSV file."""
    # Set up the Firefox webdriver
    driver = webdriver.Firefox()

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("Season,Team,Wins,Losses\n")

        for season in range(start_season, end_season + 1):
            season_data = fetch_scores(season, driver)

            if season_data:
                for row in season_data:
                    f.write(",".join(row) + "\n")

    # Close the webdriver
    driver.quit()
