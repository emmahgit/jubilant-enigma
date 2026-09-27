# Project 01 — AI Data Annotation & Quality Control

## Overview

This project demonstrates a structured workflow for reviewing AI training-data annotations with a focus on **accuracy, consistency, confidence, and quality control**.

The dataset is synthetic and was created specifically for portfolio demonstration.

## The Problem

High-volume annotation can introduce quality problems that are easy to miss when the focus is only on completing labels.

Common issues include:

* Inconsistent terminology
* Low-confidence annotations
* Ambiguous cases
* Labels that do not follow a defined vocabulary

If these issues are not identified before submission, they can reduce the consistency and usefulness of downstream training data.

## Objective

Build a repeatable annotation-review process that can:

1. Identify potential quality issues
2. Flag uncertain records
3. Standardize inconsistent labels
4. Document review decisions
5. Produce a consistent final dataset

## Workflow

```text
Annotation
    ↓
Confidence Check
    ↓
Guideline Check
    ↓
Issue Detection
    ↓
Review
    ↓
Correction / Confirmation
    ↓
Final Approval
```

## Dataset

The sample contains:

* **20 annotation records**
* **2 video clips**
* Person and vehicle objects
* Confidence scores
* Review status
* Issue classifications
* Corrected labels

## Quality Findings

| Metric                    | Result |
| ------------------------- | -----: |
| Total records             |     20 |
| Approved records          |     15 |
| Records requiring review  |      5 |
| Approval rate             |    75% |
| Review rate               |    25% |
| Low-confidence cases      |      2 |
| Label-inconsistency cases |      3 |
| Label corrections         |      3 |

## What the Review Found

### Low Confidence

Two records had confidence scores below the project's review threshold of **0.75**.

Importantly, low confidence did not automatically mean the annotation was incorrect.

Both labels were reviewed and retained.

### Label Inconsistency

Three records used terminology that did not match the project's standardized vocabulary.

Examples included:

```text
pedestrian → person
automobile → car
```

These were standardized during review.

## Before vs. After

### Before Review

* 20 records
* 5 records flagged
* 3 inconsistent labels
* 2 low-confidence records

### After Review

* 20 records reviewed
* 3 inconsistent labels standardized
* 2 low-confidence labels confirmed
* All flagged records received a documented decision

## Why This Matters

The key lesson from the project is that annotation quality is not only about whether a label exists.

A stronger quality process also checks:

**Accuracy + Consistency + Confidence + Reviewability**

The purpose of review is to catch issues before they become downstream data-quality problems.

## Automation

The `quality_check.py` script automates several repeatable checks, including:

* Total record count
* Approval rate
* Review rate
* Low-confidence cases
* Label inconsistencies
* Label corrections

This demonstrates how manual quality-control rules can be converted into repeatable checks.

## Files

| File                       | Purpose                                    |
| -------------------------- | ------------------------------------------ |
| `annotation_sample.csv`    | Synthetic annotation dataset               |
| `annotation-guidelines.md` | Labeling rules and standardized vocabulary |
| `quality-checklist.md`     | Manual quality-control checklist           |
| `quality-analysis.md`      | Findings and before/after analysis         |
| `quality_check.py`         | Automated quality checks                   |

## Skills Demonstrated

* AI data annotation
* Data quality control
* Label consistency review
* Error identification
* Quality analysis
* Documentation
* Basic Python automation
* Structured problem solving

## Portfolio Note

This is a synthetic portfolio project based on the type of AI data annotation and quality-control work performed professionally.

It does not contain confidential client information, proprietary datasets, or internal annotation guidelines.
