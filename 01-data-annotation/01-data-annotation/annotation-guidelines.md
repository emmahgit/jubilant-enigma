# Annotation Guidelines

## Purpose

These guidelines define how objects in the sample dataset should be labeled consistently.

The objective is to reduce inconsistent labels, identify uncertain cases, and ensure that reviewed data uses a standardized vocabulary.

## 1. Person

Use `person` when the object is a visible human.

Do not use alternative labels such as:

* pedestrian
* individual
* human

For this project, all visible humans are standardized to:

```text
person
```

### Example

Initial label:

```text
pedestrian
```

Standardized label:

```text
person
```

---

## 2. Vehicle

Vehicle labels should describe the most appropriate standardized vehicle class.

Use:

```text
car
motorcycle
van
truck
```

Avoid interchangeable labels when a standardized class already exists.

### Example

Initial label:

```text
automobile
```

Standardized label:

```text
car
```

---

## 3. Confidence Score

Confidence represents how certain the annotator is about the assigned label.

### High confidence

```text
0.90 – 1.00
```

Normally eligible for approval when no other issue is present.

### Medium confidence

```text
0.75 – 0.89
```

Review when the object or label could reasonably be interpreted differently.

### Low confidence

```text
Below 0.75
```

Flag for review.

A low-confidence record does not automatically mean the assigned label is wrong.

---

## 4. Label Consistency

A label should follow the same terminology throughout the dataset.

For example:

```text
automobile
car
```

should not be treated as two different classes when the project vocabulary defines both as `car`.

Likewise:

```text
pedestrian
person
```

should use the standardized `person` label.

---

## 5. Review Status

Use:

### Approved

The annotation follows the project guidelines and does not require additional review.

### Review

The annotation contains an issue requiring additional inspection.

Typical reasons include:

* Low confidence
* Label inconsistency
* Ambiguous classification
* Possible guideline violation

---

## 6. Quality-Control Process

Each annotation should pass through the following sequence:

```text
Identify Object
      ↓
Assign Label
      ↓
Record Confidence
      ↓
Check Against Guidelines
      ↓
Flag Issues
      ↓
Correct Where Necessary
      ↓
Approve
```

## Quality Principle

The goal is not to change labels unnecessarily.

The goal is to ensure that the final dataset is:

* Consistent
* Accurate
* Reviewable
* Easy to interpret
* Suitable for downstream AI training workflows

## Portfolio Note

This document is a synthetic portfolio example based on the type of annotation and quality-control workflows used in professional AI data work.

It does not reproduce any confidential client guidelines or proprietary annotation instructions.
