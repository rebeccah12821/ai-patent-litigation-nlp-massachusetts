NLP-Enhanced Legal Analytics: AI Patent Litigation in the District of Massachusetts
This repository contains code and analysis for an in-depth study of AI-related patent litigation in the District of Massachusetts (2019–2025), leveraging natural language processing (NLP) to extract legal and technical insights from court records and USPTO litigation data.

Overview
This project applies advanced NLP and data analytics to analyze the landscape of AI patent litigation in Massachusetts federal court. The analysis focuses on case outcomes, legal issues (such as Section 101 patent eligibility), and technical distinctions (hardware vs. algorithm) in AI-related disputes.

Key Features
Data Collection: Scraped and aggregated patent litigation data from the USPTO litigation portal and federal court dockets (2019–2025).

Case Filtering: Identified relevant cases using Python (pandas) and AI-specific keywords (e.g., "neural network," "generative AI").

NLP Analysis: Used spaCy to extract legal concepts (e.g., Section 101 eligibility) and classify case outcomes (settlement, dismissal, judgment).

Technical Classification: Distinguished AI patent cases by technical basis (hardware vs. algorithm).

Comparative Metrics: Compared AI and non-AI patent cases on settlement rates, discovery complexity (motions per case), and injunction frequency.

Notable Case Studies
Singular Computing v. Google (2019–2024): $1.6B settlement over AI training chip patents, emphasizing the value of specialized hardware.

Recentive Analytics v. Fox Corp (2025): Landmark Section 101 ruling invalidating generic machine learning patents, underscoring the need for genuine technical innovation.

OpenEvidence v. Pathway Medical (2025): First generative AI trade secret case, involving prompt injection attacks on large language models.

UMG Recordings v. Suno (2024): First generative AI copyright case over unauthorized music training.

Key Findings
Prevalence: 71% of patent cases involved AI technologies.

Legal Scrutiny: All challenged AI patents faced Section 101 eligibility analysis.

Complexity: AI cases averaged over three times more discovery motions than standard patent cases.

Outcomes: 60% of AI cases settled pre-trial; 40% resulted in injunctions.

Skills Demonstrated
Legal Research

Data Analysis

Natural Language Processing (spaCy)

Technical Communication

Usage
Clone the repository:

text
git clone https://github.com/rebeccah12821/ai-patent-litigation-nlp-massachusetts.git
Install dependencies:

text
pip install -r requirements.txt
Run the main analysis script:

text
python analyze_litigation.py
License
Distributed under the MIT License. See LICENSE for details.

