import matplotlib.pyplot as plt
import random

def plot_season_stats(df) -> tuple:
    """Plots the top 5 teams with most wins and losses for a given season."""
    season = random.choice(df['Season'].unique().tolist())
    season_df = df[df['Season'] == season]
    top_5_wins = season_df.nlargest(5, 'Wins')
    top_5_losses = season_df.nlargest(5, 'Losses')

    fig, axs = plt.subplots(1, 2, figsize=(12, 6))

    axs[0].bar(top_5_wins['Team'], top_5_wins['Wins'], color='skyblue')
    axs[0].set_title(f'Top 5 Teams with Most Wins in {season}')
    axs[0].set_xlabel('Team')
    axs[0].set_ylabel('Wins')
    axs[0].tick_params(axis='x', rotation=45)  # Rotate x ticks of the first plot

    axs[1].bar(top_5_losses['Team'], top_5_losses['Losses'], color='salmon')
    axs[1].set_title(f'Top 5 Teams with Most Losses in {season}')
    axs[1].set_xlabel('Team')
    axs[1].set_ylabel('Losses')
    axs[1].tick_params(axis='x', rotation=45)  # Rotate x ticks of the second plot

    plt.tight_layout()

    # Return the figure along with title and description
    return fig, f'Top 5 Teams Stats for {season}', f'This plot shows the top 5 teams with most wins and losses for the {season} season.'

def plot_random_teams_stats(df) -> tuple:
    """Plots the wins and losses of 3 random teams over multiple seasons."""
    # Selecting 3 random teams
    random_teams = random.choices(df['Team'].unique().tolist(), k=3)

    # Extracting data for the selected teams
    team_data = df[df['Team'].isin(random_teams)]

    # Creating line plot for wins
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))

    for team in random_teams:
        team_wins = team_data[team_data['Team'] == team]
        axs[0].plot(team_wins['Season'], team_wins['Wins'], label=team)

    axs[0].set_title('Wins for Random 3 Teams')
    axs[0].set_xlabel('Season')
    axs[0].set_ylabel('Wins')
    axs[0].legend()

    # Selecting 3 random teams
    random_teams = random.choices(df['Team'].unique().tolist(), k=3)

    # Extracting data for the selected teams
    team_data = df[df['Team'].isin(random_teams)]

    # Creating line plot for losses
    for team in random_teams:
        team_losses = team_data[team_data['Team'] == team]
        axs[1].plot(team_losses['Season'], team_losses['Losses'], label=team)

    axs[1].set_title('Losses for Random 3 Teams')
    axs[1].set_xlabel('Season')
    axs[1].set_ylabel('Losses')
    axs[1].legend()

    plt.tight_layout()

    # Return the figure along with title and description
    return fig, 'Random 3 Teams Stats', 'This plot shows the wins and losses of 3 random teams over multiple seasons.'

def plot_win_loss_trend(df):
    """Plots the win-loss trend for a specific team over multiple seasons."""
    team_name = random.choice(df['Team'].unique().tolist())
    team_data = df[df['Team'] == team_name]

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(team_data['Season'], team_data['Wins'], marker='o', label='Wins')
    ax.plot(team_data['Season'], team_data['Losses'], marker='x', label='Losses')

    ax.set_title(f'Win-Loss Trend for {team_name}')
    ax.set_xlabel('Season')
    ax.set_ylabel('Count')
    ax.legend()

    plt.xticks(rotation=45)
    plt.tight_layout()

    return fig, f'Win-Loss Trend for {team_name}', f'This plot shows the win-loss trend for {team_name} over multiple seasons.'

def plot_team_performance_comparison(df):
    """Plots the performance comparison (wins and losses) for 2 random teams in a particular season."""
    # Selecting 2 random teams
    random_teams = random.sample(df['Team'].unique().tolist(), 2)

    # Extracting data for the selected teams
    team_data = df[df['Team'].isin(random_teams)]

    # Creating bar plot for wins and losses
    fig, ax = plt.subplots(figsize=(10, 6))

    team_data.groupby(['Team', 'Season']).sum()[['Wins', 'Losses']].unstack('Team').plot(kind='bar', ax=ax)

    ax.set_title('Team Performance Comparison')
    ax.set_xlabel('Season')
    ax.set_ylabel('Count')
    ax.legend(title='Team', loc='upper left')

    plt.xticks(rotation=45)
    plt.tight_layout()

    return fig, 'Team Performance Comparison', 'This plot compares the performance (wins and losses) of 2 random teams in a particular season.'
