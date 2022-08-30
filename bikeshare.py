import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        cities = ['chicago', 'new york city', 'washington']
        city = input("choose the city: chicago, new york city, washington ").lower()
        if city in cities:
            break
        else:
            print("Please enter a correct value")


    # get user input for month (all, january, february, ... , june)
    while True:
        months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
        month = input("choose the month: all, january, february, ... , june ").lower()
        if month in months:
            break
        else:
            print("Please enter a correct value")


    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = input("choose the day of week: all, monday, tuesday, ... sunday ").lower()
        if day in days:
            break
        else:
            print("Please enter a correct value")


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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
    df = df[df['month'] == month]
    
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df

def display(df):
    userInput = input('\nDo you want to see first 5 rows?: y/n\n')
    rows = 0
    pd.set_option('display.max_columns',200)
        
    while True:
        if userInput == 'n':
            break
        else:
            print(df.iloc[rows: rows + 5])
            rows += 5      
            userInput = input('\ndo you want to see another 5 rows?: y/n\n"n"to continue with the statistics\n')

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month  
    common_month = df['month'].mode()[0]
    print('The most common month: {}'.format(common_month))


    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The most common day_of_week: {}'.format(common_day))


    # display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('The most common hour: {}'.format(common_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most common start station: {}'.format(common_start_station))


    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most common end station: {}'.format(common_end_station))
    

    # display most frequent combination of start station and end station trip
    df['Combi'] = df['Start Station'] + df['End Station']
    common_combi = df['Combi'].mode()[0]
    print('The most common combination of start/end stations: {}'.format(common_combi))
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    trip_duration = df['Trip Duration'].sum()/3600
    print('total travel time: {} hours'.format(trip_duration))


    # display mean travel time
    avg_trip_duration = df['Trip Duration'].mean()/60
    print('average travel time: {} min'.format(avg_trip_duration))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user = df.groupby(['User Type'])['User Type'].count()
    print('\nCount of user types: {}'.format(user))
    

    # Display counts of gender
    if 'Gender' in df.columns:
        gender = df.groupby(['Gender'])['Gender'].count()
        print('\nCount of gender types: {}'.format(gender))
    else:
        print('Gender: no data available')


    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        most_common = df['Birth Year'].mode()[0]
        print('earliest year of birth: {}, most recent year of birth: {}, most common year of birth: {}'.format(earliest, most_recent, most_common))
    else:
        print('Birth Year: no data available')
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()