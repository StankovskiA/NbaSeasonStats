from plot_data import plot_season_stats, plot_random_teams_stats, plot_win_loss_trend, plot_team_performance_comparison
import matplotlib.backends.backend_pdf
import matplotlib.pyplot as plt
import pandas as pd

def generate_report(file_path: str, save: bool) -> None:
    """Generates a PDF report with plots for the NBA season stats."""
    df = pd.read_csv(file_path)
    functions = [plot_season_stats, plot_random_teams_stats, plot_win_loss_trend, plot_team_performance_comparison]
    
    # Create a PDF object to store plots
    if save:
        with matplotlib.backends.backend_pdf.PdfPages('report.pdf') as pdf:
            # Iterate over the functions and add pages to the PDF
            for func in functions:
                plot, title, description = func(df)
                add_page_to_pdf(pdf, plot, title, description)
    else:
        # Iterate over the functions and show plots
        for func in functions:
            plot, title, description = func(df)
            plt.show()
        
    plt.close('all')

def add_page_to_pdf(pdf, plot, title, description) -> None:
    """Adds a new page to the PDF with the given plot and metadata."""
    # Add a new page to the PDF
    pdf.savefig(plot)
    # Add title and description text
    pdf.infodict()['Title'] = title
    pdf.infodict()['Author'] = description
    pdf.infodict()['Subject'] = title
    pdf.infodict()['Keywords'] = title
    
    # Remove the plot from memory
    plt.close(plot)
