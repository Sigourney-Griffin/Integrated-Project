# Feature Engineering script
# Used to clean the claims data


def feature_engineering(df):
    # Create a copy of the dataframe to avoid modifying the original one
    data = df.copy()
    
    # Convert 'policy_bind_date' and 'incident_date' to datetime
    data['policy_bind_date'] = pd.to_datetime(data['policy_bind_date'])
    data['incident_date'] = pd.to_datetime(data['incident_date'])
    
    # Handling Missing Values
    # Since the column '_c39' has all missing values, we can drop it
    data.drop(columns=['_c39'], inplace=True)
    
    # New columns
    df["Contract Years"] = df["months_as_customer"]/12
    df['total_premiums_paid'] = (df['policy_annual_premium']/12) * df['months_as_customer']
    df['net_value_of_customer'] = df['total_premiums_paid'] - df['total_claim_amount']

    
    # Calculate 'days_since_policy_binding' feature
    data['days_since_policy_binding'] = (data['incident_date'] - data['policy_bind_date']).dt.days
    
    # Extract the month and day from 'policy_bind_date' and 'incident_date'
    data['policy_bind_month'] = data['policy_bind_date'].dt.month
    data['policy_bind_day'] = data['policy_bind_date'].dt.day
    data['incident_month'] = data['incident_date'].dt.month
    data['incident_day'] = data['incident_date'].dt.day
    
    
    # Drop the original 'policy_bind_date' and 'incident_date' columns
    data.drop(['policy_bind_date', 'incident_date'], axis=1, inplace=True)
    
    return data
