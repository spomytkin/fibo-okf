---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: overnight rate
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: reference rate that is an interest rate at which a depository institution lends funds to another depository institution
      (short-term), or the interest rate the central bank charges a financial institution to borrow money overnight
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The overnight rate is the lowest available interest rate, and as such, it is only available to the most creditworthy
      institutions. It is the underlying rate for Overnight Interest Rate Swaps (IOS).
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/hasTenor
    value: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/OneDay
  subclass_of:
  - concept: /concepts/fibo/IND/InterestRates/InterestRates/ReferenceInterestRate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/ReferenceInterestRate
resource: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/OvernightRate
sources:
- id: fibo-source-e2bedd1809
  resource: references/fibo/IND/InterestRates/InterestRates.rdf
  sha256: e2bedd18096c7346ecdd7687f4fbb370e828c7fc4e483bd84780e67e65d77fe1
  title: FIBO source IND/InterestRates/InterestRates.rdf
title: overnight rate
type: Ontology Class
---

# overnight rate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/OvernightRate>

## Definition

reference rate that is an interest rate at which a depository institution lends funds to another depository institution (short-term), or the interest rate the central bank charges a financial institution to borrow money overnight

## Relationships

- **Subclass of**: [ReferenceInterestRate](/concepts/fibo/IND/InterestRates/InterestRates/ReferenceInterestRate.md)

## Constraints

- **[hasTenor](/concepts/fibo/IND/InterestRates/InterestRates/hasTenor.md)**: has value value `https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/OneDay`

## Annotations

- **label**: overnight rate
- **definition**: reference rate that is an interest rate at which a depository institution lends funds to another depository institution (short-term), or the interest rate the central bank charges a financial institution to borrow money overnight
- **explanatoryNote**: The overnight rate is the lowest available interest rate, and as such, it is only available to the most creditworthy institutions. It is the underlying rate for Overnight Interest Rate Swaps (IOS).

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
