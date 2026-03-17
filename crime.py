# import python libary
import pandas as pd

data = pd.read_csv("Crime_Data_from_2020_to_Present.csv")
data = data.dropna(subset=('AREA','AREA NAME','Crm Cd','Crm Cd Desc','TIME OCC'))

print(len(data))
print(data.columns)
user_input = int(input("enter the area code: "))
result = data[data['AREA'] == user_input]

# 1 Analysis 1 — Area Crime Pattern
print("Analysis 1 — Area Crime Pattern")
print("\n")
max_crime_code = result['Crm Cd'].value_counts().idxmax()
max_crime_desc = result['Crm Cd Desc'].value_counts().idxmax()
min_crime_code = result['Crm Cd'].value_counts().idxmin()
min_crime_desc = result['Crm Cd Desc'].value_counts().idxmin()
max_date_occur = result['DATE OCC'].value_counts().idxmax()
min_date_occur = result['DATE OCC'].value_counts().idxmin()
max_time_occur = result['TIME OCC'].value_counts().idxmax()
min_time_occur = result['TIME OCC'].value_counts().idxmin()

print("AREA:", result['AREA NAME'].iloc[0])
print("Most common crime code:", max_crime_code)
print("Most common crime description:", max_crime_desc)
print("They most of crime happend in date:",max_date_occur)
print("They most of crime happend in time:",max_time_occur)

print("least common crime code:", min_crime_code)
print("least common crime description:", min_crime_desc)
print("They least of crime happend in date:",min_date_occur)
print("They least of crime happend in time:",min_time_occur)
print("\n")

# 2 Analysis 2 — Crime Distribution (Area-wise)
print("Analysis 2 — Crime Distribution (Area-wise)")
print("\n")
code_area = data[data['AREA'] == user_input]
total_crime = code_area['Crm Cd Desc'].value_counts().sum()
count_crime = code_area['Crm Cd Desc'].value_counts()
most_crime = code_area['Crm Cd Desc'].value_counts().idxmax()
least_crime = code_area['Crm Cd Desc'].value_counts().idxmin()
print("They area name is:",code_area['AREA NAME'].iloc[0])
print("Total no of crimes:",total_crime)
print("Most of crime happened:",most_crime)
print("Least of cirme happened:",least_crime)
i = 0
percentage = (count_crime/total_crime)*100
for i in count_crime.index:
    print("They crime:",i)
    print("count:",count_crime[i])
    print("precentage is :",round(percentage[i],2),"%")
print("\n")

# 3 Analysis 3 — Top 10 Crimes
print("Analysis 3 — Top 10 Crimes")
print("\n")
code_area = data[data['AREA'] == user_input]
count_crime = code_area['Crm Cd Desc'].value_counts()
print("Top 10 crime of the certain area")
print(count_crime.head(10))   
print("\n")
 
# 4 Analysis 4 — Crime Code Analysis
print("Analysis 4 — Crime Code Analysis")
print("\n")
print("Max:",data['Crm Cd'].max())
print("Min:",data['Crm Cd'].min())
print("Range:",data['Crm Cd'].max() - data['Crm Cd'].min())
crime_code = int(input("Enter the crime code:"))
crime_code1 = data[data['Crm Cd']==crime_code]

counts = crime_code1['AREA NAME'].value_counts()
most_crime = counts.idxmax()
least_crime = counts.idxmin()
least_counts = counts[least_crime]
most_counts = counts[most_crime]
print("The crime name:",crime_code1['Crm Cd Desc'].value_counts())
print("Most crime happend in the los Angles:",most_crime)
print("Counts:",most_counts)
print("Least crime happend in the los Angles:",least_crime)
print("Counts:",least_counts)
print("\n")

# 5 Time-based crime analysis
print("\nTime-based crime analysis")
print("\n")
hours =  data[data['AREA'] == user_input]
hours['time_hours'] = hours['TIME OCC']//100

def time(hour):
    if 6 <= hour < 12:
        return "Morning"
    elif 12 <= hour < 18:
        return "Afternoon"
    elif 18 <= hour < 22:
        return "Evening"
    else:
        return "Night"
periods = hours['time_hours'].apply(time)
periods_count =periods.value_counts()
periods_total = periods.value_counts().sum()
percentage_periods = (periods_count/periods_total)*100
for per in periods_count.index:
    print("time periods:",per)
    print("Count:", periods_count[per])
    print("Percentage:", round(percentage_periods[per], 2), "%")
    print()
print("\n")
