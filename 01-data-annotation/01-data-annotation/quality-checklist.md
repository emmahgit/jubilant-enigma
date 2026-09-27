# Annotation Quality-Control Checklist

## Purpose

This checklist is used to review annotated records before they are accepted as final training data.

The objective is to identify labeling errors, inconsistencies, and uncertain cases before they move downstream.

---

## 1. Object Identification

* [ ] Is the object clearly identified?
* [ ] Is the object type appropriate?
* [ ] Has the object been recorded only once where appropriate?

---

## 2. Label Accuracy

* [ ] Does the assigned label match the object?
* [ ] Does the label follow the project vocabulary?
* [ ] Are alternative labels being used unnecessarily?

Example:

```text
Incorrect / inconsistent:
automobile

Standardized:
car
```

---

## 3. Confidence Review

* [ ] Is the confidence score reasonable?
* [ ] Are records below the review threshold flagged?
* [ ] Does a low-confidence record receive additional inspection?

**Review threshold:**

```text
Confidence < 0.75 → Review
```

---

## 4. Consistency Review

Check whether the same type of object has been labeled consistently across records.

Examples requiring review:

```text
person / pedestrian
car / automobile
```

Where the project vocabulary defines a single standard label, the standardized label should be used.

---

## 5. Issue Classification

If a record requires review, identify the reason.

Possible issue types:

* Low confidence
* Label inconsistency
* Ambiguous classification
* Guideline violation

The reason should be documented rather than simply marking the record as incorrect.

---

## 6. Correction

When an issue is confirmed:

1. Review the original annotation.
2. Compare it against the annotation guidelines.
3. Apply the standardized label where required.
4. Record the corrected label.
5. Recheck the final record.

---

## 7. Final Approval

Before a record is marked `Approved`:

* [ ] Label is valid
* [ ] Label follows the standard vocabulary
* [ ] Confidence has been considered
* [ ] No unresolved issue remains
* [ ] Corrected label is recorded where applicable

---

## Quality-Control Principle

A record should not be changed simply because it was flagged.

The purpose of review is to determine whether an actual problem exists and document the decision consistently.

The final dataset should be:

**Accurate + Consistent + Reviewable + Reproducible**

---

## Portfolio Note

This is a synthetic quality-control framework created for portfolio demonstration. It does not reproduce proprietary client workflows or confidential annotation guidelines.
