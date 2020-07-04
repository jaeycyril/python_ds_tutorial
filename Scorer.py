from typing import List, Dict

def get_m_movies_test(m_movies_list: List[int]) -> str:
    assert(type(m_movies_list) == list), "Your function does not return a list"
    assert(len(m_movies_list) == 2), "You do not have the correct number of movies in your result"
    for movie in m_movies_list:
        assert(movie[0].upper() == "M"), f"This movie: {movie} does not begin with M"
    return f"All Tests Passed"


def average_age_test(avg_age: int) -> str:
    assert(avg_age == 24.4), f"Your answer is not correct. It should be 24.4 but yours is {avg_age}"
    return f"Test passed"


"""
Query answers to Data Manipulation

Exercise 1

dataset[(dataset['sex'] == 'Female') 
        & (dataset['native-country'] == 'England') 
        & (dataset['income_band'] == '>50K')].shape[0]
        
Exercise 2

dataset.groupby(["sex","occupation"]).aggregate({"hours-per-week":"mean"})\
                                    .sort_values(by="hours-per-week", ascending=False)\
                                    .loc["Male", :]
"""
    