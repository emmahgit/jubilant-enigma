# Annotation Quality Analysis

## Dataset Overview

The sample contains **20 annotated records** across two video clips.

The review focused on:

* Label consistency
* Confidence levels
* Review status
* Corrections required
* Potential downstream quality issues

---

## Results

| Metric                             | Result |
| ---------------------------------- | -----: |
| Total annotated records            |     20 |
| Approved records                   |     15 |
| Records requiring review           |      5 |
| Approval rate                      |    75% |
| Review rate                        |    25% |
| Low-confidence cases               |      2 |
| Label-inconsistency cases          |      3 |
| Records requiring label correction |      3 |

---

## Finding 1 — Low-Confidence Annotations

Two records were flagged because their confidence scores were below the project review threshold of **0.75**.

| Record | Initial Label | Confidence | Final Label |
| ------ | ------------- | ---------: | ----------- |
| O005   | car           |       0.72 | car         |
| O006   | motorcycle    |       0.68 | motorcycle  |

### Interpretation

The low confidence did not automatically mean the labels were wrong.

Both labels were retained after review, demonstrating that a quality-control process should distinguish between:

**uncertainty** and **actual annotation error**.

---

## Finding 2 — Label Inconsistency

Three records used labels that did not match the standardized project vocabulary.

| Record | Initial Label | Standardized Label |
| ------ | ------------- | ------------------ |
| O007   | pedestrian    | person             |
| O014   | automobile    | car                |
| O015   | pedestrian    | person             |

### Impact

The underlying objects were still identifiable, but inconsistent terminology could create unnecessary class variation in a training dataset.

The labels were standardized during review.

---

## Finding 3 — Review Rate

Five of the twenty records required review.

```text
5 ÷ 20 × 100 = 25%
```

This means **25% of the sample required additional quality review** before final acceptance.

The review workload came from:

* Low-confidence annotations
* Label inconsistencies

---

## Before vs. After

### Before Review

* 20 records
* 5 records flagged
* 3 inconsistent labels
* 2 low-confidence cases

### After Review

* 20 records reviewed
* 3 inconsistent labels standardized
* 2 low-confidence labels confirmed
* No flagged record left without a documented decision

---

## Key Quality Insight

The review process shows why annotation quality cannot be measured only by whether a record contains a label.

A useful quality process also considers:

**Consistency + Confidence + Reviewability + Standardization**

The objective is to catch problems before they affect downstream training data.

---

## Portfolio Takeaway

This project demonstrates a repeatable approach to AI data quality:

```text
Annotate
   ↓
Measure Confidence
   ↓
Identify Issues
   ↓
Review
   ↓
Standardize
   ↓
Document Decision
   ↓
Approve
```

The dataset is synthetic and created solely for portfolio demonstration.
