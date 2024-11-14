from pandas import DataFrame, Series
from numpy import float64, prod, multiply


def calculate_survival_rate_to_age(current_age: int,
             to_age: int,
             mortality_factors: Series,
             mortality_improvement_factors: DataFrame) -> float64:
    """
    
    :param current_age: Current age as of a certain date
    :param to_age: Age to live to
    :param mortality_factors:
        A series indexed on age with values representing mortality rates
    :param mortality_improvement_factors:
        A DataFrame indexedon age with columns representing years, the values
        representing adjustments in the mortality rates
    :returns: Probability of living to to_age given current_age
    """
    assert len(mortality_factors) == mortality_improvement_factors.shape[1], \
        "Number of columns in mortality improvement factors should equal length of mortality factors"
    min_age, max_age = mortality_factors.index[0], mortality_factors.index[-1]
    num_ages = len(mortality_factors)
    truncation_length = current_age - min_age
    X = mortality_factors.loc[current_age:].values
    Y = mortality_improvement_factors.loc[current_age].values[:num_ages - truncation_length]
    return prod((1 - multiply(Y, X))[:(num_ages - (max_age - to_age + truncation_length))])


if __name__ == '__main__':
    print('Hello World')
