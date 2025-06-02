import pandas as pd
import spacy

# Load spaCy NLP model
nlp = spacy.load("en_core_web_sm")

# --- 1. Load Litigation Data ---
# Replace with your actual data file path
DATA_PATH = "data/litigation_data_massachusetts_2019_2025.csv"
litigation_df = pd.read_csv(DATA_PATH)

# --- 2. Filter for AI Patent Cases ---
ai_keywords = [
    "neural network", "machine learning", "AI", "artificial intelligence",
    "deep learning", "generative AI"
]

def is_ai_case(text):
    return any(keyword.lower() in str(text).lower() for keyword in ai_keywords)

litigation_df["is_ai_case"] = litigation_df["case_description"].apply(is_ai_case)
ai_cases = litigation_df[litigation_df["is_ai_case"]]

# --- 3. NLP Extraction: Section 101 Eligibility and Outcome Classification ---
def extract_section_101(text):
    if "section 101" in str(text).lower() or "101 eligibility" in str(text).lower():
        return True
    return False

def classify_outcome(text):
    text = str(text).lower()
    if "settle" in text:
        return "Settlement"
    elif "dismiss" in text:
        return "Dismissal"
    elif "judgment" in text or "verdict" in text:
        return "Judgment"
    else:
        return "Other"

ai_cases["section_101"] = ai_cases["case_summary"].apply(extract_section_101)
ai_cases["outcome"] = ai_cases["case_outcome"].apply(classify_outcome)

# --- 4. Technical Classification: Hardware vs. Algorithm ---
def classify_tech(text):
    text = str(text).lower()
    if "chip" in text or "hardware" in text or "processor" in text:
        return "Hardware"
    elif "algorithm" in text or "model" in text or "software" in text:
        return "Algorithm"
    else:
        return "Other"

ai_cases["tech_type"] = ai_cases["case_description"].apply(classify_tech)

# --- 5. Comparative Metrics ---
ai_settlement_rate = (ai_cases["outcome"] == "Settlement").mean()
ai_injunction_rate = ai_cases["injunction_granted"].mean() if "injunction_granted" in ai_cases.columns else None
ai_discovery_motions_avg = ai_cases["discovery_motions"].mean() if "discovery_motions" in ai_cases.columns else None

non_ai_cases = litigation_df[~litigation_df["is_ai_case"]]
non_ai_settlement_rate = (non_ai_cases["case_outcome"].apply(classify_outcome) == "Settlement").mean()
non_ai_discovery_motions_avg = non_ai_cases["discovery_motions"].mean() if "discovery_motions" in non_ai_cases.columns else None

print("AI Case Settlement Rate:", ai_settlement_rate)
print("AI Case Injunction Rate:", ai_injunction_rate)
print("AI Case Avg Discovery Motions:", ai_discovery_motions_avg)
print("Non-AI Case Settlement Rate:", non_ai_settlement_rate)
print("Non-AI Case Avg Discovery Motions:", non_ai_discovery_motions_avg)

# --- 6. Summary Table ---
summary = pd.DataFrame({
    "Type": ["AI", "Non-AI"],
    "Settlement Rate": [ai_settlement_rate, non_ai_settlement_rate],
    "Avg Discovery Motions": [ai_discovery_motions_avg, non_ai_discovery_motions_avg]
})
print(summary)

# --- 7. Save Results ---
ai_cases.to_csv("ai_patent_cases_massachusetts_results.csv", index=False)
summary.to_csv("ai_vs_nonai_summary.csv", index=False)
