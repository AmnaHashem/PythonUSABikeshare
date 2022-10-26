import time
import pandas as pd
import numpy as np
from tabulate import tabulate


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = { 'january': 1,
               'february': 2,
               'march': 3,
               'april': 4,
               'may': 5,
               'june': 6,
               'july': 7,
               'august': 8,
               'september': 9,
               'october': 10,
               'november': 11,
               'december': 12 }

DAYS_DATA = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = str(input("Please enter the city name, you would like to explore? (chicago, new york city, washington): "))
        city.lower()
        if city in CITY_DATA:
            break
        else:
            print('please enter a valid city from the list in lowercase format\n')
        
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = str(input("Please enter the month name, you would like to explore? (all, january, february, ... , june): "))
        month.lower()
        if month in MONTH_DATA or month == 'all':
            break
        else:
            print('please enter a valid month\n')
            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = str(input("Please enter the day name, you would like to explore? (all, monday, tuesday, ... sunday): "))
        day.lower()
        if day in DAYS_DATA or day == 'all':
            break
        else:
            print('please enter valid day\n')
    
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    data = pd.read_csv(CITY_DATA[city])
    date = pd.DatetimeIndex(data['Start Time'])
    data['Year'] = date.year
    data['Month'] = date.month
    data['Day'] = date.day
    data['WeekDay'] = date.day_name()
    data['Hour'] = date.hour
    
    if month != 'all':
        df = data.loc[data['Month'] == MONTH_DATA[month]]
    elif day != 'all':
        df = data.loc[data['WeekDay'].str.lower() == day]
    elif month != 'all' and day != 'all':
        df = data.loc[(data['Month'] == MONTH_DATA[month]) and data['WeekDay'].str.lower() == day]
    else:
        df = pd.DataFrame(data)

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('Most Common Month: ', df['Month'].value_counts().idxmax())

    # TO DO: display the most common day of week
    print('Most Common Day of the Week: ', df['WeekDay'].value_counts().idxmax())

    # TO DO: display the most common start hour
    print('Most Common Day of the Week: ', df['Hour'].value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most Commonly Used Start Station: ', df['Start Station'].value_counts().idxmax())

    # TO DO: display most commonly used end station
    print('Most Commonly Used End Station: ', df['End Station'].value_counts().idxmax())

    # TO DO: display most frequent combination of start station and end station trip
    print('Most Frequent Combination of Start Station and End Station:\n', df.groupby(['Start Station', 'End Station']).size().nlargest(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total Travel Time: ', df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('Mean Travel Time: ', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of User Types\n', df['User Type'].value_counts())

    if city != 'washington':
        # TO DO: Display counts of gender
        print('Counts of Gender\n', df['Gender'].value_counts())
        print("There isn't a [Gender] column in this spreedsheet!")

        # TO DO: Display earliest, most recent, and most common year of birth
        print('Earliest Year Of Birth: ', df['Birth Year'].min())
        print('Most Recent Year Of Birth: ', df['Birth Year'].max())
        print('Most Common Year Of Birth: ', df['Birth Year'].value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def table_row(df):
    # TO DO: Dispaly 5 rows of data
    pd.set_option(“display.max_columns”,200)
    while True:
        display_data = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n')
        if display_data.lower() != 'yes':
            break
        print(tabulate(df_default.iloc[np.arange(0+i,5+i)], headers ="keys"))
        i+=5
              


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        table_row(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
