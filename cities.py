import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def findCities(text):

    raw_protest = pd.read_csv('/Users/ruthielin/Downloads/(USE) BLM Protests 2020.csv', delimiter=',')

    protest_info = raw_protest.drop(
        ['Region', 'Country', 'Comments', 'Alias', 'Date Added', 'Batch', 'Mailing Abbrevation', 'Search Label'],
        axis=1)

    # This is where User must input City
    City = text
    result = ""

    idx = protest_info.index[protest_info['City'] == City].tolist()

    if len(idx) > 0:
        if len(idx) == 1:
            x_pos = protest_info.iloc[idx[0], 1]
            y_pos = protest_info.iloc[idx[0], 2]

            nearby_city = protest_info[(protest_info["X Longitude"].between(x_pos - 0.25, x_pos + 0.25)) & (
                protest_info["Y Latitude"].between(y_pos - 0.25, y_pos + 0, 25))]

            columnSeriesObj = nearby_city['City']
            arr = columnSeriesObj.values.tolist()
            for i in arr:
                result += i
                if arr.index(i) != len(arr)-1:
                    result += ", "
        else:
            result += "\nSorry, we can't process your city, since there are more than one with the same name!"
    else:
        result += "\nSorry, we don't have data for your city."
    return result


# def findCities(text):
#     raw_protest = pd.read_csv("/Users/ruthielin/Downloads/(USE) BLM Protests 2020.csv", delimiter=',')
#
#     protest_info = raw_protest.drop(
#         ['Region', 'Country', 'Comments', 'Alias', 'Date Added', 'Batch', 'Mailing Abbrevation', 'Search Label'],
#         axis=1)
#
#     # This is where User must input City
#     City = text
#     result = ""
#
#     idx = protest_info.index[protest_info['City'] == City].tolist()
#
#     if len(idx) > 0:
#         if len(idx) == 1:
#             x_pos = protest_info.iloc[idx[0], 1]
#             y_pos = protest_info.iloc[idx[0], 2]
#
#             nearby_city = protest_info[(protest_info["X Longitude"].between(x_pos - 0.25, x_pos + 0.25)) & (
#                 protest_info["Y Latitude"].between(y_pos - 0.25, y_pos + 0, 25))]
#
#             columnSeriesObj = nearby_city['City']
#             arr = columnSeriesObj.values.tolist()
#             result += "Nearby Cities with Past BLM Protests\n"
#             for i in arr:
#                 result += i
#                 result += "\n"
#         else:
#             result += "\nSorry, we can't process your city, since there are more than one with the same name!"
#     else:
#         result += "\nSorry, we don't have data for your city"
#     return result

# def findCities(text):
#     raw_protest = pd.read_csv("/Users/ruthielin/Downloads/(USE) BLM Protests 2020.csv", delimiter=',')
#     protest_info = raw_protest.drop(
#         ['Region', 'Country', 'Comments', 'Alias', 'Date Added', 'Batch', 'Mailing Abbrevation', 'Search Label'],
#         axis=1)
#
#     # This is where User must input City
#     City = text
#     idx = protest_info.index[protest_info['City'] == City].tolist()
#
#     if len(idx) > 0:
#         if len(idx) == 1:
#             x_pos = protest_info.iloc[idx[0], 1]
#             y_pos = protest_info.iloc[idx[0], 2]
#
#             nearby_city = protest_info[(protest_info["X Longitude"].between(x_pos - 0.25, x_pos + 0.25)) & (
#                 protest_info["Y Latitude"].between(y_pos - 0.25, y_pos + 0, 25))]
#
#             columnSeriesObj = nearby_city['City']
#             arr = columnSeriesObj.values.tolist()
#             print("Nearby Cities with Past BLM Protests")
#             print()
#             for i in arr:
#                 print(i)
#         else:
#             print()
#             print("Sorry, we can't process your city, since there are more than one with the same name!")
#     else:
#         print()
#         print("Sorry, we don't have data for your city")
#     return "Hi"
