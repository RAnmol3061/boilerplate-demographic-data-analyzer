import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("/workspace/boilerplate-demographic-data-analyzer/adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    age_sex = df[['sex', 'age']]
    sex = age_sex['sex']
    sex_male_only = age_sex[sex != "Female"]
    sex_male_only_age = sex_male_only['age']
    average_age_men = round(sex_male_only_age.mean(), 1 )

    # What is the percentage of people who have a Bachelor's degree?
    education = df['education'].value_counts()
    total = education.sum()
    value = education['Bachelors']
    percent = (value/total)*100
    percentage_bachelors = round(percent, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    
    #higher_education
    edu_salary_df = df[['education', 'salary']]
    advE_salary = edu_salary_df[edu_salary_df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    salary_advE = advE_salary['salary']

    total_advanced = advE_salary.shape[0]
    total_above50K = advE_salary[salary_advE == '>50K'].shape[0]

    percent = (total_above50K/total_advanced)*100
    higher_education = round(percent, 1)

    #lower_education
    edu_salary_df = df[['education', 'salary']]
    basic_salary = edu_salary_df[~edu_salary_df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    salary_basic = basic_salary['salary']

    total_basic = salary_basic.shape[0]
    total_above50K = basic_salary[salary_basic == '>50K'].shape[0]

    percent = (total_above50K/total_basic)*100
    lower_education = round(percent, 1)

    # percentage with salary >50K
    higher_education_rich = higher_education
    lower_education_rich = lower_education

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    work_hour = df['hours-per-week']
    min_hour = work_hour.min()
    min_work_hours = round(min_hour, 1)

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    hour_salary_df = df[['hours-per-week', 'salary']]
    salary_minhour = hour_salary_df['salary']
    hours = hour_salary_df['hours-per-week']
    min_hour_perweek = hours.min()
    min_hour = hour_salary_df[hours == min_hour_perweek]

    total = min_hour.shape[0]
    min_hour_above50K = min_hour[salary_minhour == '>50K'].shape[0]

    percent = (min_hour_above50K/total)*100

    num_min_workers = None

    rich_percentage = round(percent, 1)

    # What country has the highest percentage of people that earn >50K?
    country_salary = df[['native-country', 'salary']]
    salary_coun = country_salary['salary']
    coun_df = country_salary['native-country']

    total_counts_country = coun_df.value_counts()
    high_earners = country_salary[salary_coun == '>50K']
    high_earners_counts = high_earners['native-country'].value_counts()

    percent_high_earners = (high_earners_counts/total_counts_country)*100

    max_percent_country = percent_high_earners.idxmax()
    max_percent = percent_high_earners.max()

    highest_earning_country = max_percent_country
    highest_earning_country_percentage = round(max_percent, 1)

    # Identify the most popular occupation for those who earn >50K in India.
    country_salary = df[['native-country', 'salary', 'occupation']]
    country = country_salary['native-country']
    salary = country_salary['salary']

    india_salary = country_salary[country == "India"]
    india_salary_above50K = india_salary[salary == '>50K']

    highest_occ_counts = india_salary_above50K['occupation'].value_counts()
    highest_occ = highest_occ_counts.idxmax()
    top_IN_occupation = highest_occ

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
