

HOME_TEAM_WON=1

def update_score(team,score,point):
    if team not in score:
        score[team]=0
    score[team]+=point



def tournamentWinner(competitions, results):
    # Write your code here.
    currentBestTeam=""
    scores={currentBestTeam:0}
    for idx, competition in enumerate(competitions):
        home_team,away_team=competition
        if results[idx] == HOME_TEAM_WON:
            winning_team= home_team
        else:
            winning_team = away_team
        update_score(winning_team,scores, point=3)

        if scores[winning_team]>scores[currentBestTeam]:
            currentBestTeam=winning_team

    return currentBestTeam

competitions= [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
  ]
results=[0, 0, 1]
print(tournamentWinner(competitions,results))