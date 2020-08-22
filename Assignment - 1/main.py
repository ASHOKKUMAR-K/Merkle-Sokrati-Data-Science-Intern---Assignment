import pandas as pd
# import numpy as np
from preprocessing import Preprocessing

if __name__ == "__main__":
    market_campaign = pd.read_excel("data/Data Analyst Assignment.xlsx", sheet_name=0)
    preprocessor = Preprocessing(market_campaign)
    preprocessor.preprocessing()

    # Exporting pre-processed file to a CSV file
    market_campaign.to_csv("data/market_campaign_preprocessed.csv")