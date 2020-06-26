import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as seabornInstance
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics


def get_risk(code):
    raw_RISK = pd.read_csv('/Users/ruthielin/Downloads/RISK Factors Take 2.csv', skiprows=1, delimiter=',')

    RISK_data = raw_RISK.dropna()
    RISK_data = RISK_data.drop(['OnlyWHITE_2012'], axis=1)
    RISK_data.columns = ['FIPS', 'State_Abbrev', 'Area_Name', 'HDDR', 'PCTPOVALL_2018', 'UNEMrate_2019', 'MHI_2018',
                         'OVER65_2012', 'MinorityPOP_2012', 'POP_Density_2010', 'POP_2010']

    Num_RISK = RISK_data.drop(['State_Abbrev', 'Area_Name'], axis=1)
    Num_RISK['MHI_2018'] = Num_RISK['MHI_2018'].str.replace(',', '')

    raw_covid = pd.read_csv('/Users/ruthielin/Downloads/us-counties.csv-2.txt', delimiter=',')
    covidDF = raw_covid.copy(deep=True)
    covidDF['month'] = pd.DatetimeIndex(covidDF['date']).month
    covidDF['day'] = pd.DatetimeIndex(covidDF['date']).day
    covidDF = covidDF.dropna()

    covidDF = covidDF.sort_values(by=['fips'], ascending=True)

    FIPS_Num = RISK_data.drop(
        ['State_Abbrev', 'Area_Name', 'HDDR', 'PCTPOVALL_2018', 'UNEMrate_2019', 'MHI_2018', 'OVER65_2012',
         'MinorityPOP_2012', 'POP_Density_2010', 'POP_2010'], axis=1)

    PercentInfect = []
    indexArr = []

    test = covidDF.copy(deep=True)

    test = test[test['date'] == '2020-06-21']

    Num_RISK = Num_RISK.join(test.set_index('fips'), on='FIPS')

    Num_RISK = Num_RISK.dropna()

    Num_RISK = Num_RISK.drop(['FIPS', 'date', 'county', 'state', 'deaths', 'month', 'day'], axis=1)

    Num_RISK.columns = ['HDDR', 'PCTPOVALL_2018', 'UNEMrate_2019', 'MHI_2018', 'OVER65_2012', 'MinorityPOP_2012',
                        'POP_Density_2010', 'POP_2010', 'COVID-19_cases']

    Num_RISK['PercentInfected'] = (Num_RISK['COVID-19_cases'] / Num_RISK['POP_2010'] * 1000)

    X = Num_RISK[['HDDR', 'PCTPOVALL_2018', 'UNEMrate_2019', 'MHI_2018', 'OVER65_2012', 'MinorityPOP_2012',
                  'POP_Density_2010']].values
    y = Num_RISK['PercentInfected'].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

    regressor = LinearRegression()
    regressor.fit(X_train, y_train)

    coeff_df = pd.DataFrame(regressor.coef_,
                            ['HDDR', 'PCTPOVALL_2018', 'UNEMrate_2019', 'MHI_2018', 'OVER65_2012', 'MinorityPOP_2012',
                             'POP_Density_2010'], columns=['Coefficient'])

    y_pred = regressor.predict(X_test)

    df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
    df1 = df.head(25)

    full_RISK = pd.read_csv('/Users/ruthielin/Downloads/(USE) BackUp (RISK ANALYZED)- Usable Statistics.csv',
                            skiprows=1, delimiter=',')

    get_RISKdf = full_RISK.drop(
        ['State_Abbrev', 'Area_Name', 'HDDRp100000', 'PCTPOVALL_2018', 'UNEMrate_2019', 'MHI_2018', 'OVER65_2012',
         'OnlyWHITE_2012', 'MinorityPOP_2012', 'POP_Density_2010', 'POP_2010', 'RISK', 'Unnamed: 14',
         'Formula 1 Descriptive Statistics'], axis=1)

    get_RISKdf = get_RISKdf.dropna()

    num = int(code)
    currentCounty = get_RISKdf[get_RISKdf['FIPS'] == num]
    currentCounty = currentCounty.reset_index()
    FIPS = currentCounty.FIPS
    RISK_val = currentCounty['Formula 1']

    return RISK_val[0]


# # prints RISK as a percentage bar between 0-100%
# plt.barh(FIPS, RISK_val)
# y_pos = np.arange(len(RISK_val))
# plt.yticks(y_pos, RISK_val)
# plt.ylabel('FIPS is ' + str(FIPS[0]))
# plt.xlabel('RISK Level (%)')
# plt.title('Your approximate risk is ' + str(RISK_val[0]) + "%")
# axes = plt.gca()
# axes.set_xlim([0, 100])
# plt.show()
# print('Your approximate risk is ' + str(RISK_val[0]) + '%')
#
# # Print model efficacy statistics
# print('Model Efficacy Statistics')
# print()
# print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
# print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
# print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
