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

    return bbrank


def getCompare(team1, team2):
    winner = ""

    team_stats = getTeam()
    # t1 = team_stats[team_stats.TEAM == team1]

    t1_stat = team_stats.BPI[team_stats.Team == team1]
    t2_stat = team_stats.BPI[team_stats.Team == team2]

    t2 = np.float64(t2_stat)
    t1 = np.float64(t1_stat)

    # Using the maximum function of numpy,  compare the stats, if equals one then return the team that corresponds to the stat
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
swt_16_second = []
swt_16_first = []

temp_hold = []

def printrd(rdlist):
    i = 0

    while i < len(rdlist):
        print(rdlist[i])
        i += 1


def appendlist(rd, rdlist):
    i = 0
    while i < len(rdlist):
        rd.append(rdlist[i])
        i += 1
    return rd


def getRound(ini_round, reg):
    thd_rd = []
    i = 0

    while i < len(ini_round) - 1:
        thd_rd.append(getCompare(ini_round[i], ini_round[i + 1]))
        i = i + 2

    return thd_rd


for div, team in divisions.items():
    if div == 'MW':
        ini_round_mw.append(getCompare(team[0], team[15]))
        ini_round_mw.append(getCompare(team[7], team[8]))
        ini_round_mw.append(getCompare(team[4], team[11]))
        ini_round_mw.append(getCompare(team[3], team[12]))
        ini_round_mw.append(getCompare(team[5], team[10]))
        ini_round_mw.append(getCompare(team[2], team[13]))
        ini_round_mw.append(getCompare(team[6], team[9]))
        ini_round_mw.append(getCompare(team[1], team[14]))
        print('\n' +"Midwest-Second Round".upper())
        printrd(ini_round_mw)

    if div == 'W':
        ini_round_w.append(getCompare(team[0], team[15]))
        ini_round_w.append(getCompare(team[7], team[8]))
        ini_round_w.append(getCompare(team[4], team[11]))
        ini_round_w.append(getCompare(team[3], team[12]))
        ini_round_w.append(getCompare(team[5], team[10]))
        ini_round_w.append(getCompare(team[2], team[13]))
        ini_round_w.append(getCompare(team[6], team[9]))
        ini_round_w.append(getCompare(team[1], team[14]))
        print('\n' +"West-Second Round".upper())
        printrd(ini_round_w)

    if div == 'E':
        ini_round_e.append(getCompare(team[0], team[15]))
        ini_round_e.append(getCompare(team[7], team[8]))
        ini_round_e.append(getCompare(team[4], team[11]))
        ini_round_e.append(getCompare(team[3], team[12]))
        ini_round_e.append(getCompare(team[5], team[10]))
        ini_round_e.append(getCompare(team[2], team[13]))
        ini_round_e.append(getCompare(team[6], team[9]))
        ini_round_e.append(getCompare(team[1], team[14]))
        print('\n' + "East-Second Round".upper())
        printrd(ini_round_e)

    if div == 'S':
        ini_round.append(getCompare(team[0], team[15]))
        ini_round.append(getCompare(team[7], team[8]))
        ini_round.append(getCompare(team[4], team[11]))
        ini_round.append(getCompare(team[3], team[12]))
        ini_round.append(getCompare(team[5], team[10]))
        ini_round.append(getCompare(team[2], team[13]))
        ini_round.append(getCompare(team[6], team[9]))
        ini_round.append(getCompare(team[1], team[14]))

        print('\n' + "South-Second Round".upper())
        printrd(ini_round)

swt_16_first = appendlist(swt_16_first, getRound(ini_round_mw, "Midwest"))
swt_16_second = appendlist(swt_16_second, getRound(ini_round_e, "East"))
swt_16_first = appendlist(swt_16_first, getRound(ini_round_w, "West"))
swt_16_second = appendlist(swt_16_second, getRound(ini_round, "South"))

print('\n' + "Sweet Sixteen".upper())
printrd(swt_16_first)
printrd(swt_16_second)

print('\n' + "Elite 8".upper())
elite_1 = getRound(swt_16_first, "")
elite_2 = getRound(swt_16_second, "")
printrd(elite_1)
printrd(elite_2)
print('\n' + "Final Four".upper())
final_fr_1 = getRound(elite_1, "")
final_fr_2 = getRound(elite_2, "")

print("%s vs %s" %(final_fr_1[0], final_fr_1[1]))
print("%s vs %s" %(final_fr_2[0], final_fr_2[1]))


champ_1 = getRound(final_fr_1, "")
champ_2 = getRound(final_fr_2, "")
print("\nChampionship is %s vs %s" %(champ_1[0], champ_2[0]))
winner = getCompare(champ_1[0], champ_2[0])

print ("Winner is: %s" % winner)
