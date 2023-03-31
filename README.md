# LexDAO-Transactions-Project
This project is designed to seek a wallet and pull all transactions into a data object that can be ported easily into psql.
In order to manage this project, one will need to know how to create a config file that maintains their password keys and API token.  
Without this, you will not be able to access the API.

# Project Plan
Loosely speaking this is the plan for how this project will materialize.  It may change over time.

  - [x] Create script to read and download all transactions in json file
  - [ ] Edit script to return the api call in a json object
  - [ ] Learn how to connect to postgresql with psycopg2
  - [ ] Edit script to pass json object to postgresql
  - [ ] Connect postgres to tableau
  - [ ] Evaluate wallet transactions
  - [ ] Map transactions to accounting behavior/chart of accounts with reference table keys
