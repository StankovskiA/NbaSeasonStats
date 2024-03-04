from generate_report import generate_report
from data_extraction import scrape
import argparse
import logging


logging.basicConfig(level=logging.INFO)

def main():
    parser = argparse.ArgumentParser(description="NBA Season Stats Analysis Tool")
    parser.add_argument("--start", type=int, help="Start season for the analysis. Format: YY", default=18, required=False)
    parser.add_argument("--end", type=int, help="End season for the analysis. Format: YY", default=23, required=False)
    parser.add_argument("--out", type=str, help="Name of the output file. Default: nba_season_stats.csv", default="nba_season_stats.csv", required=False)
    parser.add_argument("--report", type=bool, help="If the tool should generate a report", default=True, required=False)
    args = parser.parse_args()
    
    start_season = args.start
    end_season = args.end
    output_file = args.out
    report = args.report
    
    logging.info("NBA Season Stats Analysis Tool started")
    logging.info(f"Start Season: {start_season}, End Season: {end_season}, Output File: {output_file}, Generate PDF: {report}")

    # scrape(start_season, end_season, output_file)
    
    logging.info(f"Data saved to {output_file}")
    
    if report:
        logging.info("Generating report")
        generate_report(output_file)
    

if __name__ == "__main__":
    main()
