# main.py
import pandas as pd
from status_classifier import classify_status
from hierarchy_classifier import load_model, build_index, classify_field_of_work
from translator import translate_to_english
from collections import defaultdict

# Sample dataset with mixed languages
data = [
    {"Status": "在校生", "Field_of_Work": "生物医学研究"},  # Chinese
    {"Status": "已工作", "Field_of_Work": "AI in medical imaging"}, # English
    {"Status": "student", "Field_of_Work": "Investment banking"},
    {"Status": "working", "Field_of_Work": "Pharmaceutical clinical trials"},
    {"Status": "N/A", "Field_of_Work": "N/A"},
    {"Status": "在校生", "Field_of_Work": "机械工程"},  # Chinese for mechanical engineering
    {"Status": "已工作", "Field_of_Work": "health insurance"},
    {"Status": "in study", "Field_of_Work": "university research"},
    {"Status": "working", "Field_of_Work": "远程医疗服务"}, # telemedicine in Chinese
    {"Status": "已工作", "Field_of_Work": "cloud computing SaaS"},
    {"Status": "working", "Field_of_Work": "cultural anthropology"},
    {"Status": "in study", "Field_of_Work": "-"},
    {"Status": "已工作", "Field_of_Work": "移动应用开发"} # Chinese for mobile app development
]

df = pd.DataFrame(data)

# Classify status first
df['Unified_Status'] = df['Status'].apply(classify_status)

model = load_model()
nodes_by_level = build_index(model)

def classify_fow_with_translation(field_text, status):
    if status == 'N/A':
        return None
    # Translate to English if contains Chinese
    english_text = translate_to_english(field_text)
    return classify_field_of_work(english_text, model, nodes_by_level, max_depth=4)

df['Unified_Field_of_Work'] = df.apply(lambda row: classify_fow_with_translation(row['Field_of_Work'], row['Unified_Status']), axis=1)

print("Classified Data:")
print(df)

def aggregate_counts(rows, field_key='Unified_Field_of_Work'):
    level_counts = defaultdict(lambda: defaultdict(int))
    for _, r in rows.iterrows():
        path = r.get(field_key)
        if not path:
            continue
        for i, cat in enumerate(path):
            level = i + 1
            level_counts[level][cat] += 1
    return level_counts

stats = aggregate_counts(df)

print("\nStatistics by level:")
for level in sorted(stats.keys()):
    print(f"Level {level}:")
    for cat, cnt in stats[level].items():
        print(f"  {cat}: {cnt}")

# Final Check
total_entries = len(df)
na_status_count = (df['Unified_Status'] == 'N/A').sum()
valid_status_count = total_entries - na_status_count

print("\nFinal Check:")
print(f"Total Entries: {total_entries}")
print(f"N/A Status Entries: {na_status_count}")
print(f"Valid Status Entries: {valid_status_count}")
print("Sum check:", na_status_count + valid_status_count == total_entries)
