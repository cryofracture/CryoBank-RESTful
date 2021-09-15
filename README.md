# CryoBank RESTful API

A quick async api to query some basic bank user information.

# Get informed about your customer's accounts

Get information on customer's cities, bank balances, total users in the system, and total bank balance across all users.

## Several helpful endpoints:

    /api/v1/user_count: Count the users registered to the system (no parameters).
    /api/v1/user_count/<string:requested_data>: Count users with requested data.
    /api/v1/total_balance: Add the total balance of all registered users, the total bank's balance.

## A work in progress

There's a lot more to add to this API, including:

* Count all users located in specific city
* Count all users registered from specific email domain
* Count/Display all users under/over/between specific balances
* Display all users with no email address for registration completion
    
