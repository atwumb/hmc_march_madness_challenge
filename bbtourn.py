import pandas as pd


divisions = {"MW": ["Kentucky", "Kansas", "Notre Dame",
                    "Maryland", "West Virginia",
                    "Butler", "Wichita", "Cincinnati",
                    "Purdue", "Indiana", "Texas",
                    "Buffalo", "Valparaiso", "Northeastern",
                    "New Mexico St", "Hampton"],

             "E": ["Villanova", "Virginia", "Oklahoma",
                   "Louisville", "Iowa", "Providence",
                   "Michigan State", "NC State", "LSU", "UGA",
                   "playin-e", "Wyoming", "Irvine",
                   "Alabama", "Belmont", "Lafayette"],

             "W": ["Wisconsin", "Arizona", "Baylor",
                   "UNC", "Arkansas", "Xavier",
                   "VCU", "Oregon", "Oklahoma State",
                   "Ohio", "Mississippi",
                   "Wofford", "Harvard", "Georgia State",
                   "Texas Southern", "Coastal Carolina"],

             "S": ["Duke", "Gonzaga", "Iowa State", "Georgetown",
                   "Utah", "Methodist", "Iowa",
                   "San Diego", "St John", "Davidson",
                   "UCLA", "Austin", "Washington",
                   "UAB", "North Dakota", "Robert Morris"]
}

winner = ""


def getTeam():
    bbrank = pd.read_csv(r'espn_power_rankings.csv')
    #bbrank = rank.set_index('TEAM')

    return bbrank


def getCompare(team1, team2):
    """

    :rtype : object
    """
    team_stats = getTeam()
   # t1 = team_stats[team_stats.TEAM == team1

   # t1_stat = team_stats.BPI[team_stats.TEAM == team1]
    #t2_stat = team_stats.BPI[team_stats.TEAM == team2]

    # if t1_stat > t2_stat:
    #     winner == team1
    # else:
    #     winner == team2
    #
    winner = team1
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


def getRound(ini_round, reg):
    count = len(ini_round)/2
    i = 0
    print(reg)
    while count > 0:
        if count == 16:
            print("Third")
            for i in len(ini_round):
                print(getCompare(ini_round[i],ini_round[i+1]))
        if count == 8:
            print("Sweet 16")
            for i in (len(ini_round)):
                print(getCompare(ini_round[i],ini_round[i+1]))
        if count == 4:
            print("Elite 8")
            for i in(len(ini_round)):
                print(getCompare(ini_round[i],ini_round[i+1]))

for div, team in divisions.items():
    if div == 'W':
        ini_round_w.append(getCompare(team[0], team[15]))
        ini_round_w.append(getCompare(team[7], team[8]))
        ini_round_w.append(getCompare(team[4], team[11]))
        ini_round_w.append(getCompare(team[3], team[12]))
        ini_round_w.append(getCompare(team[5], team[10]))
        ini_round_w.append(getCompare(team[2], team[14]))
        print("West- 2nd Rd")
        printrd(ini_round_w)

    if div == 'MW':

        ini_round_mw.append(getCompare(team[0], team[15]))
        ini_round_mw.append(getCompare(team[7], team[8]))
        ini_round_mw.append(getCompare(team[4], team[11]))
        ini_round_mw.append(getCompare(team[3], team[12]))
        ini_round_mw.append(getCompare(team[5], team[10]))
        ini_round_mw.append(getCompare(team[2], team[14]))
        print("Midwest- 2nd Rd")
        printrd(ini_round_mw)

    if div == 'S':
        ini_round.append(getCompare(team[0], team[15]))
        ini_round.append(getCompare(team[7], team[8]))
        ini_round.append(getCompare(team[4], team[11]))
        ini_round.append(getCompare(team[3], team[12]))
        ini_round.append(getCompare(team[5], team[10]))
        ini_round.append(getCompare(team[2], team[14]))
        print("South - 3rd Rd")
        printrd(ini_round)

    if div == 'E':
        ini_round_e.append(getCompare(team[0], team[15]))
        ini_round_e.append(getCompare(team[7], team[8]))
        ini_round_e.append(getCompare(team[4], team[11]))
        ini_round_e.append(getCompare(team[3], team[12]))
        ini_round_e.append(getCompare(team[5], team[10]))
        ini_round_e.append(getCompare(team[2], team[14]))
        print("East - 3rd Rd")
        printrd(ini_round_e)




