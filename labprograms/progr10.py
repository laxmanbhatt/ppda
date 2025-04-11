import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder


data = {
    "Laptop": ["Dell Inspiron", "HP Pavilion", "Lenovo ThinkPad", "Apple MacBook"],
    "Operating System": ["Windows", "Windows", "Linux", "macOS"],
    "Storage": ["1TB", "512GB", "1TB", "256GB"]
}


df = pd.DataFrame(data)
print("Original Dataset:")
print(df)

onehot_encoder = OneHotEncoder(sparse=False)
os_encoded = onehot_encoder.fit_transform(df[["Operating System"]])
os_encoded_df = pd.DataFrame(os_encoded, columns=onehot_encoder.get_feature_names_out(["Operating System"]))
df = pd.concat([df, os_encoded_df], axis=1)

print("\nDataset After OneHotEncoding Operating System:")
print(df)


label_encoder = LabelEncoder()
df["Storage_Encoded"] = label_encoder.fit_transform(df["Storage"])

print("\nDataset After LabelEncoding Storage:")
print(df)

print("\nLabel Encoding Mapping for Storage:")
print(dict(zip(df["Storage"], df["Storage_Encoded"])))
