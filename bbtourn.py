import pandas as pd

def getTeam():
    
    bbrank = pd.read_csv(r'school_win_pct_stats.csv', index_col='Ranking')

    return  bbrank
