import pandas
import HealthCheck

df = pandas.read_excel("Users.xlsx")
users_list = [row.tolist() for index, row in df.iterrows()]

for i in range(len(users_list)):
    HealthCheck.create_api(users_list[i][0], users_list[i][1])