import pandas
pandas.read_csv("taskdata.csv.")
dataset = pandas.read_csv("taskdata.csv")
y= dataset["10th_marks"]
x= dataset[["study_hrs","social_hr","netflix_hr","sleep_hr"]]
from sklearn.linear_model import LinearRegression
model = LinearRegression()
x.values
type(x)
x.values.shape
import pandas

pandas.read_csv("taskdata.csv.")

dataset = pandas.read_csv("taskdata.csv")

y= dataset["10th_marks"]

x= dataset[["study_hrs","social_hr","netflix_hr","sleep_hr"]]

from sklearn.linear_model import LinearRegression

model = LinearRegression()

x.values

type(x)

x.values.shape

model.fit(x,y)

model.predict([[5,2,4,7]])

