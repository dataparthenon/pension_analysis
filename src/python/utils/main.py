import pandas as pd
from collections import defaultdict
from utils.calculate_fas import calculate_fas


DEFERRED_FACTORS_PATH = 'data/deferred_factors.xlsx'
INCREASE_RATE_PATH = 'data/salary_increase_rate.xlsx'

def main(yos: int,
         age: int,
         comp: float) -> pd.DataFrame:
    deferred_factors = pd.read_excel(DEFERRED_FACTORS_PATH,
                                    usecols=['Age', 'Combined_Factor'],
                                    index_col='Age',
                                    )
    salary_increase_rate = pd.read_excel(INCREASE_RATE_PATH)


    deferred_factors.columns = [col_name.lower() for col_name in deferred_factors.columns]
    salary_increase_rate.columns = [col_name.lower() for col_name in salary_increase_rate.columns]


    INCREASE_RATES = salary_increase_rate['increase'].values
    DEFERRED_FACTORS = defaultdict(lambda: 1, deferred_factors['combined_factor'].to_dict())
    ACCRUED_BENEFIT_FACTOR = 0.0182
    PVAB_FACTOR = 12.5


    fas = calculate_fas(yos=yos, 
                        comp=comp,
                        increase_rates=INCREASE_RATES)
    fas_next_year = calculate_fas(yos=yos, 
                                  comp=comp,
                                  increase_rates=INCREASE_RATES, 
                                  years_ahead=1)

    accrued_benefit = yos * fas * ACCRUED_BENEFIT_FACTOR
    pvab = accrued_benefit * DEFERRED_FACTORS[age] * PVAB_FACTOR
    accrued_benefit_next_year = (yos + 1) * fas * ACCRUED_BENEFIT_FACTOR
    pvab_next_year = accrued_benefit_next_year * DEFERRED_FACTORS[age + 1] * PVAB_FACTOR
    pvab_increase = pvab_next_year - pvab
    return {
        'fas': fas,
        'fas_next_year': fas_next_year,
        'accrued_benefit': accrued_benefit,
        'pvab': pvab,
        'accrued_benefit_next_year': accrued_benefit_next_year,
        'pvab_next_year': pvab_next_year,
        'pvab_increase': pvab_increase
    }
