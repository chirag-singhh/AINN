from sklearn.tree import DecisionTreeClassifier, export_text
import pandas as pd

# Dataset
data = {
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast', 'Sunny', 'Sunny', 'Rain'],
    'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool', 'Mild'],
    'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'Normal'],
    'Wind': ['Weak', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Weak', 'Weak'],
    'PlayTennis': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes']
}

df = pd.DataFrame(data)

# Convert categorical data to numeric
df_encoded = df.apply(lambda col: col.astype('category').cat.codes)

X = df_encoded.drop('PlayTennis', axis=1)
y = df_encoded['PlayTennis']

# Train model
clf = DecisionTreeClassifier(criterion='entropy')
clf.fit(X, y)

# Display tree
tree_rules = export_text(clf, feature_names=list(X.columns))
print(tree_rules)




# python -m pip install scikit-learn
