class Preprocessing:
    """ Preprocess Marketing Campaign Data """
    def __init__(self, data):
        self.data = data

    def preprocessing(self) -> object:
        self.sort_data_by_date()
        self.drop_product_column()
        self.drop_phase_column()
        self.drop_campaign_type_column()
        self.drop_communication_medium_column()
        self.alter_campaign_values()
        self.categorize_visitors_spends()
        self.categorize_visitors_impressions()
        self.categorize_visitors_clicks()
        self.fill_null_values_link_clicks()

    def sort_data_by_date(self):
        self.data.sort_values(by="Date", inplace=True)
        self.data.reset_index(inplace=True, drop=True)

    def drop_product_column(self):
        self.data.drop("product", axis=1, inplace=True)

    def drop_phase_column(self):
        self.data.drop("phase", axis=1, inplace=True)

    def drop_campaign_type_column(self):
        self.data.drop("campaign_type", axis=1, inplace=True)

    def drop_communication_medium_column(self):
        self.data.drop("communication_medium", axis=1, inplace=True)

    def alter_campaign_values(self):
        self.data.iloc[:, 1] = self.data.iloc[:, 1].apply(
            lambda platform: {"Google Ads": "Google Ads_Search_Keywords",
                              "Facebook Ads": "Facebook Ads_Conversions_Creative"}[platform]
        )

    def categorize_visitors_spends(self):
        self.data.iloc[:, 8] = self.data.iloc[:, 8].apply(
            lambda seconds: self.categorize_visitors_by_spending_time(seconds)
        )

    @staticmethod
    def categorize_visitors_by_spending_time(seconds):
        if seconds == 0:
            return 0
        elif 0 < seconds <= 2 * 60:
            return 1
        elif 2 * 60 < seconds <= 5 * 60:
            return 2
        elif 5 * 60 < seconds <= 10 * 60:
            return 3
        elif 10 * 60 < seconds <= 30 * 60:
            return 4
        elif 30 * 60 < seconds <= 60 * 60:
            return 5
        elif 60 * 60 < seconds <= 120 * 60:
            return 6
        else:
            return 7

    def categorize_visitors_impressions(self):
        self.data.iloc[:, 9] = self.data.iloc[:, 9].apply(
            lambda impressions: self.categorize_visitors_based_on_impressions(impressions))

    @staticmethod
    def categorize_visitors_based_on_impressions(impressions):
        if impressions == 0:
            return 0
        elif 0 < impressions <= 20:
            return 1
        elif 20 < impressions <= 50:
            return 2
        elif 50 < impressions <= 200:
            return 3
        else:
            return 4

    def categorize_visitors_clicks(self):
        self.data.iloc[:, 10] = self.data.iloc[:, 10].apply(
            lambda clicks: self.categorize_visitors_based_on_clicks(clicks)
        )

    @staticmethod
    def categorize_visitors_based_on_clicks(clicks):
        if clicks == 0:
            return 0
        elif 0 < clicks <= 5:
            return 1
        elif 5 < clicks <= 10:
            return 2
        elif 20 < clicks <= 50:
            return 3
        elif 50 < clicks <= 200:
            return 4
        else:
            return 5

    def fill_null_values_link_clicks(self):
        self.data.iloc[:, 11] = self.data.iloc[:, 11].fillna(1.0)