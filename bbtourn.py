import pandas as pd
import numpy as np


divisions = {"MW": ["Kentucky", "Kansas", "Notre Dame",
                    "Maryland", "West Virginia",
                    "Butler", "Wichita", "Cincinnati",
                    "Purdue", "Indiana", "Texas",
                    "Buffalo", "Valparaiso", "Northeastern",
                    "New Mexico St", "Hampton"],

             "E": ["Villanova", "Virginia", "Oklahoma",
                   "Louisville", "Iowa", "Providence",
                   "Michigan State", "NC State", "LSU", "UGA",
                   "Dayton", "Wyoming", "Irvine",
                   "Alabama", "Belmont", "Lafayette"],

             "W": ["Wisconsin", "Arizona", "Baylor",
                   "UNC", "Arkansas", "Xavier",
                   "VCU", "Oregon", "Oklahoma State",
                   "Ohio", "Mississippi", "Wofford", "Harvard", "Georgia State",
                   "Texas Southern", "Coastal Carolina"],

             "S": ["Duke", "Gonzaga", "Iowa State", "Georgetown",
                   "Utah", "Methodist", "Iowa",
                   "San Diego", "St John", "Davidson",
                   "UCLA", "Austin", "Washington",
                   "UAB", "North Dakota", "Robert Morris"]
}


def getTeam():
    bbrank = pd.read_csv(r'espn_power_rankings2.csv', dtype={'BPI': float, 'PVA': float})
    # bbrank = pd.read_excel("espn_power_rankings2.xls")

    # bbrank = rank.set_index('TEA

    return bbrank


def getCompare(team1, team2):
    winner = ""

    team_stats = getTeam()
    # t1 = team_stats[team_stats.TEAM == team1]

    t1_stat = team_stats.BPI[team_stats.Team == team1]
    t2_stat = team_stats.BPI[team_stats.Team == team2]
    # print(float(t1_stat))
    # print(float(t2_stat))

    t2 = np.float64(t2_stat)
    t1 = np.float64(t1_stat)
    # elif t1_stat < t2_stat:
    # winner == team2
    # else:
    # t1_stat = int(team_stats.Rank[team_stats.Team == team1])
    #     t2_stat = int(team_stats.Rank[team_stats.Team == team2])

    #Using the maximum function of numpy,  compare the stats, if equals one then return the team that corresponds to the stat
    if np.maximum(t1, t2) == t1:
        winner = team1

    else:
        winner = team2

    # winner = team1
    return winner


ini_round = []
ini_round_mw = []
ini_round_e = []
ini_round_w = []


def printrd(rdlist):
    i = 0
    while i < len(rdlist):
        print(rdlist[i])
        i += 1
def FinalRound(round):
    holdrd = 0
    holdrd.append(round)

    return holdrd

def getRound(ini_round, reg):

    final_fr = []
    elite_round = []
    count = float(len(ini_round) / 2)
    i = 0
    print((reg).upper())
    print("============")
    while count > 0:
        if count == 3.0:
            print("Third Round")
            for i in range(0, len(ini_round) - 1):
                print(getCompare(ini_round[i], ini_round[i + 1]))
        if count == 1.5:
            print('\n')
            print("Sweet 16")
            for i in range(0, len(ini_round) - 1):
                print(getCompare(ini_round[i], ini_round[i + 1]))
        # if count == 0.75:
        #     print('\n')
        #     print("Elite 8")
        #     for i in range(0, len(ini_round) - 1):
        #        # print(getCompare(ini_round[i], ini_round[i + 1]))
        #        elite_round.append(getCompare(ini_round[i], ini_round[i + 1]))
        i += 1
        count = count / 2


for div, team in divisions.items():

    if div == 'MW':
        ini_round_mw.append(getCompare(team[0], team[15]))
        ini_round_mw.append(getCompare(team[7], team[8]))
        ini_round_mw.append(getCompare(team[4], team[11]))
        ini_round_mw.append(getCompare(team[3], team[12]))
        ini_round_mw.append(getCompare(team[5], team[10]))
        ini_round_mw.append(getCompare(team[2], team[14]))
        print("Midwest- 2nd Rd")
        printrd(ini_round_mw)
        getRound(ini_round_mw, "Midwest")


    if div == 'W':
        ini_round_w.append(getCompare(team[0], team[15]))
        ini_round_w.append(getCompare(team[7], team[8]))
        ini_round_w.append(getCompare(team[4], team[11]))
        ini_round_w.append(getCompare(team[3], team[12]))
        ini_round_w.append(getCompare(team[5], team[10]))
        ini_round_w.append(getCompare(team[2], team[14]))
        printrd(ini_round_w)
        getRound(ini_round_w, "West")

    if div == 'E':
        ini_round_e.append(getCompare(team[0], team[15]))
        ini_round_e.append(getCompare(team[7], team[8]))
        ini_round_e.append(getCompare(team[4], team[11]))
        ini_round_e.append(getCompare(team[3], team[12]))
        ini_round_e.append(getCompare(team[5], team[10]))
        ini_round_e.append(getCompare(team[2], team[14]))
        # print("East - 2rd Rd")
        # printrd(ini_round_e)
        getRound(ini_round_e, "East")


    if div == 'S':
        ini_round.append(getCompare(team[0], team[15]))
        ini_round.append(getCompare(team[7], team[8]))
        ini_round.append(getCompare(team[4], team[11]))
        ini_round.append(getCompare(team[3], team[12]))
        ini_round.append(getCompare(team[5], team[10]))
        ini_round.append(getCompare(team[2], team[14]))
        # print("South - 2rd Rd")
        # printrd(ini_round)
        getRound(ini_round, "South")






