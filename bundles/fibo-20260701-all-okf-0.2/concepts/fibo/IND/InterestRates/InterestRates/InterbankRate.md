---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: interbank rate
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: reference rate that is the rate of interest charged on short-term loans between banks
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Banks borrow and lend money in the interbank market in order to manage liquidity and meet the requirements placed
      on them. The interest rate charged depends on the availability of money in the market, on prevailing rates and on the
      specific terms of the contract, such as term length.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/IND/InterestRates/InterestRates/ReferenceInterestRate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/ReferenceInterestRate
resource: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/InterbankRate
sources:
- id: fibo-source-e2bedd1809
  resource: references/fibo/IND/InterestRates/InterestRates.rdf
  sha256: e2bedd18096c7346ecdd7687f4fbb370e828c7fc4e483bd84780e67e65d77fe1
  title: FIBO source IND/InterestRates/InterestRates.rdf
title: interbank rate
type: Ontology Class
---

# interbank rate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/InterbankRate>

## Definition

reference rate that is the rate of interest charged on short-term loans between banks

## Relationships

- **Subclass of**: [ReferenceInterestRate](/concepts/fibo/IND/InterestRates/InterestRates/ReferenceInterestRate.md)

## Annotations

- **label**: interbank rate
- **definition**: reference rate that is the rate of interest charged on short-term loans between banks
- **explanatoryNote**: Banks borrow and lend money in the interbank market in order to manage liquidity and meet the requirements placed on them. The interest rate charged depends on the availability of money in the market, on prevailing rates and on the specific terms of the contract, such as term length.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
