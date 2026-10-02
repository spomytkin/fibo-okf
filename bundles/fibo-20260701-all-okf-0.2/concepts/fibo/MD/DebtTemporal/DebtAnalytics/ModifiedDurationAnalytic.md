---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: modified duration analytic
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The percentage price change of a security for a given change in yield. The higher the modified duration of a security,
      the higher its risk. Ad/ModDuration = [duration / {1 + (IRR/M)}]; where IRR is the internal rate of return and M is
      the number of compounding periods per year.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The higher the MD the greater the change in price for a given change in yield.
  disjoint_with:
  - concept: /concepts/fibo/MD/DebtTemporal/DebtAnalytics/MacCaulaysDurationAnalytic.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/MacCaulaysDurationAnalytic
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/MacCaulaysDurationAnalytic
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Documents/refersTo
  subclass_of:
  - concept: /concepts/fibo/MD/DebtTemporal/DebtAnalytics/DurationAnalytic.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/DurationAnalytic
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/ModifiedDurationAnalytic
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
title: modified duration analytic
type: Ontology Class
---

# modified duration analytic

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/ModifiedDurationAnalytic>

## Definition

The percentage price change of a security for a given change in yield. The higher the modified duration of a security, the higher its risk. Ad/ModDuration = [duration / {1 + (IRR/M)}]; where IRR is the internal rate of return and M is the number of compounding periods per year.

## Relationships

- **Subclass of**: [DurationAnalytic](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/DurationAnalytic.md)

## Constraints

- **Disjoint with**: [MacCaulaysDurationAnalytic](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/MacCaulaysDurationAnalytic.md)
- **[refersTo](<https://www.omg.org/spec/Commons/Documents/refersTo>)**: some values from of type [MacCaulaysDurationAnalytic](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/MacCaulaysDurationAnalytic.md)

## Annotations

- **label** (en): modified duration analytic
- **definition** (en): The percentage price change of a security for a given change in yield. The higher the modified duration of a security, the higher its risk. Ad/ModDuration = [duration / {1 + (IRR/M)}]; where IRR is the internal rate of return and M is the number of compounding periods per year.
- **explanatoryNote** (en): The higher the MD the greater the change in price for a given change in yield.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
