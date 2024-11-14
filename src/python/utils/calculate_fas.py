from typing import List


def calculate_fas(yos: int,
                   comp: float,
                   increase_rates: List[float],
                   years_ahead=0) -> float:
    """
    Calculates the Five Year Average Salary (FAS) for a pension contributor.
    If the contributor has < 5 years of experience, returns 0
    If the contributor has more than 9 years of experience, then calculates
    the 3-year average salary.

    :param yos: Years of Service with state
    :param comp: Current compensation
    :param increase_rates: A list of salary increase rates where index = yos - 1
    :param years_ahead: How many years in the future to perform the FAS calculation
    :returns: FAS in $
    """
    for i in range(years_ahead):
        comp = comp * (1 + increase_rates[yos])
        yos += 1
    cum_sum = count = 0
    yos -= 1
    if yos < 4 or yos > 49:
        return 0
    elif yos < 10:
        while yos > 0 and count < 5:
            comp = comp / (1 + increase_rates[yos - 1])
            cum_sum += comp
            count += 1
            yos -= 1
    else:
        while count < 3:
            comp = comp / (1 + increase_rates[yos - 1])
            cum_sum += comp
            count += 1
            yos -= 1
    return cum_sum / count
