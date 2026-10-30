---
annotations_creators:
  - no-annotations
language:
  - en
license: cc-by-4.0
multilinguality:
  - monolingual
size_categories:
  - 1K<n<10K
source_datasets:
  - original
tags:
  - ats
  - resume-optimization
  - job-postings
  - keyword-analysis
  - recruitment
  - nlp
task_categories:
  - tabular-classification
  - text-retrieval
pretty_name: ResumeFitting ATS Job Posting Keyword Study (3,518 Postings)
---

# ResumeFitting ATS Job Posting Keyword Dataset (3,518 Postings)

Empirical keyword frequency data across 3,518 job postings from 81 technology companies, collected from public Greenhouse job boards.

## Dataset Overview

This dataset, curated by ZoeVera for ResumeFitting, provides term frequencies for fixed lists of technical skills, qualifications, tools, and methodologies appearing in public tech job postings.

- **Live interactive version:** https://resumefitting.com/ats-resume-keyword-study
- **License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Primary data URL:** https://resumefitting.com/ats-resume-keyword-study/data.csv

## Structure & Schema

The dataset (`data.csv`) has one row per role and term, 288 rows in total:

| Column Name | Data Type | Description |
|---|---|---|
| `role` | string | Job role category (e.g., Software Engineer, DevOps / SRE / Platform Engineer, Product Manager). |
| `term` | string | Target skill, tool, or qualification term. |
| `category` | string | Grouping of the term within its role study (e.g., Practice, Certifications, Cloud & infra). Category names differ between roles. |
| `share_of_postings_percent` | float | Percentage of the role's postings that mention the term. |
| `postings_mentioning_term` | integer | Number of postings that mention the term. |
| `postings_in_sample` | integer | Number of deduplicated job postings analyzed for the role. |
| `margin_of_error_points` | float | Margin of error in percentage points. Empty for most rows. |
| `collected` | date | Date the postings for the role were collected (2026-08-29 to 2026-09-09). |

## Roles Represented

- Software Engineer: 1,360 postings across 72 companies (45 terms)
- Sales / Account Executive: 921 postings across 52 companies (43 terms)
- Product Manager: 421 postings across 62 companies (44 terms)
- Marketing: 347 postings across 62 companies (44 terms)
- Cybersecurity: 212 postings across 51 companies (40 terms)
- DevOps / SRE / Platform Engineer: 134 postings across 41 companies (42 terms)
- Accountant: 123 postings across 49 companies (30 terms)

## Limitations

- The postings are a snapshot of mostly US technology companies, not the whole profession.
- Matching is by term, so a synonym that is not in the term list counts as absent.
- The smaller samples carry margins of error of roughly 6 to 9 percentage points.

## Quickstart & Usage

```python
import pandas as pd

url = "https://resumefitting.com/ats-resume-keyword-study/data.csv"
df = pd.read_csv(url)

# Top 5 terms for DevOps
devops = df[df["role"].str.contains("DevOps", case=False)].sort_values(
    by="share_of_postings_percent", ascending=False
)
print(devops[["term", "share_of_postings_percent"]].head(5))
```

## Citation Information

If you use this dataset in your research, software applications, or articles, please cite it as follows.

### BibTeX

```bibtex
@dataset{resumefitting_2026_keywords,
  author    = {ZoeVera},
  title     = {ATS Job Posting Keyword Frequency Study (3,518 Postings)},
  year      = {2026},
  publisher = {ResumeFitting},
  url       = {https://resumefitting.com/ats-resume-keyword-study}
}
```

### APA

ZoeVera. (2026). *ATS Job Posting Keyword Frequency Study (3,518 Postings)* [Data set]. ResumeFitting. https://resumefitting.com/ats-resume-keyword-study
