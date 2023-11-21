import pandas as pd

file_path = 'matches2020.csv'
data = pd.read_csv(file_path)
data_head = data.head()
print(data_head)

total_games = data.shape[0]
lfl_games = data[data['league'] == 'LFL']
total_lfl_games = lfl_games.shape[0]
print(total_lfl_games)

red_side_wins = data[data['result'] == 0]
total_red_side_wins = red_side_wins.shape[0]
total_games = data.shape[0]
winrate_red_side = (total_red_side_wins / total_games) * 100
print(winrate_red_side, "%")

lfl_teams_data = data[data['league'] == 'LFL']
lfl_teams = pd.concat([lfl_teams_data['blueteam'], lfl_teams_data['redteam']]).unique()
for team in lfl_teams:
    print(team)

mid_champions = pd.concat([data['bluemid'], data['redmid']])
most_played_mid_champion = mid_champions.mode().iloc[0]
print(most_played_mid_champion)

all_roles = pd.concat([data['bluetop'], data['bluejungle'], data['bluemid'], data['blueadc'], data['bluesupport'],
                      data['redtop'], data['redjungle'], data['redmid'], data['redadc'], data['redsupport']])
most_played_champions = all_roles.value_counts().head(5)
print(most_played_champions)

lec_teams_data = data[data['league'] == 'LEC'].copy()
lec_teams_data['winning_team'] = lec_teams_data.apply(lambda row: row['blueteam'] if row['result'] == 1 else row['redteam'], axis=1)
lec_teams_wins = lec_teams_data['winning_team'].value_counts().reset_index()
lec_teams_wins.columns = ['Team', 'Wins']
print(lec_teams_wins)

ezreal_vs_aphelios = data[((data['blueadc'] == 'Ezreal') & (data['redadc'] == 'Aphelios')) | ((data['blueadc'] == 'Aphelios') & (data['redadc'] == 'Ezreal'))]
total_games = ezreal_vs_aphelios.shape[0]
ezreal_wins = ezreal_vs_aphelios[ezreal_vs_aphelios['result'] == 1].shape[0]
winrate_ezreal_vs_aphelios = (ezreal_wins / total_games) * 100

print(winrate_ezreal_vs_aphelios, "%")
