import pandas as pd
import json
from datetime import date, timedelta
from team_analysis import team_analysis_flow, except_messgs
from ref_analysis import ref_analysis_flow, refexcept_messgs


def main():
    today = date.today()
    tomorrow = date.today() + timedelta(days=1)
    print(today, tomorrow)

    if (today.day % 2) == 1:
        team_analysis_flow(today, tomorrow)
        ref_analysis_flow(today, tomorrow)
        for key in except_messgs.keys():
            print(f"{key}: {except_messgs[key]}")
        for key in refexcept_messgs.keys():
            print(f"{key}: {refexcept_messgs[key]}")


if __name__ == '__main__':
    main()