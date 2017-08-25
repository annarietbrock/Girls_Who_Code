import pandas
import matplotlib

data = pandas.read_csv("data/weather_year.csv")

data

len(data)

data.columns

data.columns = ["date", "max_temp", "mean_temp", "min_temp", "max_dew",
                "mean_dew", "min_dew", "max_humidity", "mean_humidity",
                "min_humidity", "max_pressure", "mean_pressure",
                "min_pressure", "max_visibilty", "mean_visibility",
                "min_visibility", "max_wind", "mean_wind", "min_wind",
                "precipitation", "cloud_cover", "events", "wind_dir"]

data

data.mean_temp.head()

data.mean_temp.std()

data.mean_temp.hist()

data.std()

data.date.head()

first_date = data.date.values[0]
first_date

from datetime import datetime
datetime.strptime(first_date, "%Y-%m-%d")

data.date = data.date.apply(lambda d: datetime.strptime(d, "%Y-%m-%d"))
data.date.head()

data.index = data.date
data

data.ix[datetime(2012, 8, 19)]

data = data.drop(["date"], axis=1)
data.columns

empty = data.apply(lambda col: pandas.isnull(col))
empty

empty.events.head(10)

data.events.head(10)

data.dropna(subset=["events"])

data.events = data.events.fillna("")
data.events.head(10)

num_rain = 0
for idx, row in data.iterrows():
    if "Rain" in row["events"]:
        num_rain += 1

"Days with rain: {0}".format(num_rain)

freezing_days = data[data.max_temp <= 32]
freezing_days

freezing_days[freezing_days.min_temp >= 20]

data[(data.max_temp <= 32) & (data.min_temp >= 20)]

temp_max = data.max_temp <= 32
type(temp_max)
