import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_DATA = ['all', 'january', 'february','march', 'april', 'june']
DAY_DATA = ['all', 'sunday','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

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
    city = ""
    while True: 
        try:
            city = input("Please enter a city from the list (Chicago, New York City, Washington): ").lower()
            if city  in CITY_DATA :
                break
        except:
            print("Invalid Input")    
    # TO DO: get user input for month (all, january, february, ... , june)
    month= ""
    while True:
        try:
            month = input("Please enter a month to filter the data by: All, January, February, ...., June: ").lower()
            if month in MONTH_DATA:
                break
        except:
            print("Invalid Input")    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day= ""
    while True:
        try:
            day= input("Please enter week of a day to filter the data by: All, Monday,.... Sunday: ").lower()
            if day in DAY_DATA:
                break
        except:
            print("Invalid Input")
    
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
 # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most common month:', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most common day:', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour= df['hour'].mode()[0]
    print('Most common start hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    
    popular_start_station= df['Start Station'].mode()[0]
    print('Most common start station:', popular_start_station)

    
    popular_end_station= df['End Station'].mode()[0]
    print('Most common end station: ', popular_end_station)

    
    df['popular_combo'] = df['Start Station'] + df['End Station']
    popular_combination = df['popular_combo'].mode()[0]
    print('Most frequent combination of start station and end station trip: ', popular_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    
    total_travel_time= df['Trip Duration'].sum()
    print('Total travel time(in minutes): ', total_travel_time/60)


    
    average_travel_time= df['Trip Duration'].mean()
    print('Average travel time(in minutes): ', average_travel_time/60)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    
    user_types = df['User Type'].value_counts()
    print(user_types)

    
    if 'Gender' in df.columns:
        gender_type = df['Gender'].value_counts()
        print(gender_type)
    else:
        print('Gender column doesn\'t exist.')
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print(df['Birth Year'].describe())
    else:
       print('Birth Year column doesn\'t exist.') 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        #Gets input from the user for the raw data
        answer = input('Would you like to see the raw data?(yes, no): ')
        if answer.lower() == 'yes':
            print(df.head())
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
