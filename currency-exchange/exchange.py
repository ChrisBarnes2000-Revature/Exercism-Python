def exchange_money(budget, exchange_rate):
    """This function should return the value of the exchanged currency.
    
    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    return float(budget/exchange_rate);

def get_change(budget, exchanging_value):
    """This function should return the amount of money that is left from the budget.
    
    :param budget: float - amount of money you own.
    :param exchanging_value: int - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    return float(budget-exchanging_value);

def get_value_of_bills(denomination, number_of_bills):
    """This exchanging booth only deals in cash of certain increments. 
    The total you receive must be divisible by the value of one "bill" or unit, 
    which can leave behind a fraction or remainder. 
    Your function should return only the total value of the bills (excluding fractional amounts)
    the booth would give back. Unfortunately, the booth gets to keep the remainder/change as an added bonus.

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """
    return int(denomination*number_of_bills);

def get_number_of_bills(budget, denomination):
    """This function should return the number of new currency bills that you can receive within the given budget.
    In other words: How many whole bills of new currency fit into the amount of old currency let in your budget? 
    Remember -- you can only receive whole bills, not fractions of bills, so remember to divide accordingly.
    Effectively, you are rounding down to the nearest whole bill/denomination.

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """
    return int(budget/denomination);

def exchangeable_value(budget, exchange_rate, spread, denomination):
    """This function should return the maximum value of the new currency after calculating the exchange rate plus the spread. 
    Remember that the currency denomination is a whole number, and cannot be sub-divided.

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    # Parameter spread is the percentage taken as an exchange fee, written as an integer.
    # It needs to be converted to decimal by dividing it by 100.
    # If 1.00 EUR == 1.20 USD and the spread is 10, the actual exchange rate will be:
            # 1.00 EUR == 1.32 USD because 10% of 1.20 is 0.12, and this additional fee is added to the exchange.
    spread_precent = spread / 100;
    spread_deficit = exchange_rate * spread_precent;
    new_rate = exchange_rate + spread_deficit;
    # budget, denomination, spread, spread_precent, spread_deficit, exchange_rate, new_rate
    NUM_BILLS = get_number_of_bills(budget, denomination);    # int - number of bills after exchanging all your money.
    VAL_BILLS = get_value_of_bills(denomination, NUM_BILLS);  # int - total value of bills you now have.
    FINAL_VAL = int(exchange_money(budget, new_rate));        # float - exchanged value of the foreign currency you can receive.
    # VAL_LEFT = get_change(budget, exchanging_value);         # float - amount left of your starting currency after exchanging.
    return FINAL_VAL;

def non_exchangeable_value(budget, exchange_rate, spread, denomination):
    """This function should return the value that is not exchangeable due to the denomination of the bills.
    Remember - this booth gets to keep the change in addition to charging an exchange fee.
    Start by calculating the value you would receive if you were able to keep subdivided bills,
    then subtract the amount you would receive in whole bills.
    Both amounts should take the spread,or the exchange fee into account.

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int non-exchangeable value.
    """
    
    # Start by calculating the value you would receive if you were able to keep subdivided bills,
    total_val = exchangeable_value(budget, exchange_rate, spread, denomination);
    # Both amounts should take the spread, or the exchange fee into account.
    num_bills = get_number_of_bills(budget, denomination);
    bills_val = get_value_of_bills(denomination, num_bills);
    # then subtract the amount you would receive in whole bills. 
    leftover_val = total_val - bills_val;
    return int(leftover_val);
