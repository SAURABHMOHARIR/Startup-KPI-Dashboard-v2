import pandas as pd
import numpy as np

# Create dummy monthly data for a startup
months = pd.date_range('2024-01-01', periods=12, freq='M')

data = {
    'Month': months.strftime('%b-%Y'),
    'Revenue': np.random.randint(80000, 150000, 12),
    'ActiveUsers': np.random.randint(1000, 3000, 12),
    'CAC': np.random.randint(1500, 5000, 12),
    'ChurnRate': np.random.uniform(2, 6, 12),
    'CustomerGrowthRate': np.random.uniform(5, 15, 12)
}

df = pd.DataFrame(data)

# Calculate Lifetime Value (LTV)
df['LTV'] = (df['Revenue'] / df['ActiveUsers']) * (1 / (df['ChurnRate']/100))

# Save to CSV
df.to_csv('kpi_data.csv', index=False)
print("✅ Data generated and saved as kpi_data.csv")
