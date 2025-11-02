import pandas as pd
import math

# --- Sample dataset ---
data = {
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast', 'Sunny', 'Sunny', 'Rain'],
    'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool', 'Mild'],
    'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'Normal'],
    'Wind': ['Weak', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Weak', 'Weak'],
    'PlayTennis': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes']
}

df = pd.DataFrame(data)

# --- Helper functions ---

def entropy(target_col):
    elements, counts = np.unique(target_col, return_counts=True)
    entropy = 0
    for i in range(len(elements)):
        probability = counts[i]/np.sum(counts)
        entropy += -probability * math.log2(probability)
    return entropy


def info_gain(data, split_attribute_name, target_name="PlayTennis"):
    total_entropy = entropy(data[target_name])
    
    # calculate the values and counts for the split attribute
    vals, counts = np.unique(data[split_attribute_name], return_counts=True)
    
    # calculate weighted entropy
    weighted_entropy = 0
    for i in range(len(vals)):
        subset = data[data[split_attribute_name] == vals[i]]
        weighted_entropy += (counts[i]/np.sum(counts)) * entropy(subset[target_name])
    
    # calculate Information Gain
    info_gain = total_entropy - weighted_entropy
    return info_gain


def ID3(data, originaldata, features, target_attribute_name="PlayTennis", parent_node_class=None):
    # If all target values have same class → return that class
    if len(np.unique(data[target_attribute_name])) <= 1:
        return np.unique(data[target_attribute_name])[0]
    
    # If dataset is empty → return mode of original dataset
    elif len(data) == 0:
        return np.unique(originaldata[target_attribute_name])[np.argmax(
            np.unique(originaldata[target_attribute_name], return_counts=True)[1]
        )]
    
    # If no features left → return parent class
    elif len(features) == 0:
        return parent_node_class
    
    else:
        # Default class (mode of target)
        parent_node_class = np.unique(data[target_attribute_name])[np.argmax(
            np.unique(data[target_attribute_name], return_counts=True)[1]
        )]
        
        # Select feature with best information gain
        item_values = [info_gain(data, feature, target_attribute_name) for feature in features]
        best_feature_index = np.argmax(item_values)
        best_feature = features[best_feature_index]
        
        # Create tree structure
        tree = {best_feature: {}}
        
        # Remove best feature from list
        features = [f for f in features if f != best_feature]
        
        # Grow tree recursively
        for value in np.unique(data[best_feature]):
            sub_data = data[data[best_feature] == value]
            subtree = ID3(sub_data, data, features, target_attribute_name, parent_node_class)
            tree[best_feature][value] = subtree
        
        return tree


# --- Run the algorithm ---
import numpy as np

features = df.columns[:-1]  # all columns except target
tree = ID3(df, df, features)

print("Decision Tree:\n", tree)





# python -m pip install pandas numpy