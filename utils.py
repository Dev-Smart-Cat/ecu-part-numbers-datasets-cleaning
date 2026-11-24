import os
from sqlalchemy import create_engine


def fill_empty_rows(df):

    """
    Fill out all empty rows with the string "Not Available".

    Parameters:
        df: Dataframe with empty rows.

    Returns:
        df: Dataframe with all rows filled out with data.
    """
    # Loop to iterate over all cols
    for col in df.columns:
        # Fill out with a string the empty rows
        df[col] = df[col].fillna("Not Available")

    return df


def import_datasets_to_db(df, df_name=str):

    '''
    Import the df cleaned to the db

    Parameters: 
        df (DataFrame): main df to import to the db.
        df_name: string to label the df into the db.

    Returns:
        Import the df to the db. 
    '''
    # Setting up the connection with the PosgreSQL
    dbname=os.getenv("DBNAME")
    user=os.getenv("USER")
    password=os.getenv("PASSWORD")
    host=os.getenv("HOST")
    port=5432

    # String connection for SQLAlchemy (using psycopg2 as driver)
    engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}')

    return df.to_sql(df_name, engine, if_exists='replace', index=False)


def create_file_path(file_relative_path):

    '''
    Create a file path from the datasets on /data directory.

    Parameters: 
        str: String with the relative path from the dataset will be cleaned.

    Returns:
        Full relative from the dataset will be passed on the pd.read_csv() function.
    '''

    # Directory name where the datasets are located 
    dir = "../data"
    # Loop to iterate over the /data directory
    for filename in os.listdir(dir):
        # Condition to confirm when the passed dataset path is found
        if filename.endswith:
            csv_file_path = os.path.join(dir, file_relative_path)
    return csv_file_path        # Return the full dataset path