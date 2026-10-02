---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: base rate
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: basic rate of interest on which the actual rate a bank charges on loans to its customers is calculated
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: BBR
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Typically, the bank base rate is a reference rate set by a central bank. Banks that are regulated by a given central
      bank cannot lend below the base rate to their customers. The bank base rate is determined on an ongoing basis and represents
      the central bank's judgement of the price of short-term funds on their interbank market.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: bank base rate
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/IND/InterestRates/InterestRates/ReferenceInterestRate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/ReferenceInterestRate
resource: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/BaseRate
sources:
- id: fibo-source-e2bedd1809
  resource: references/fibo/IND/InterestRates/InterestRates.rdf
  sha256: e2bedd18096c7346ecdd7687f4fbb370e828c7fc4e483bd84780e67e65d77fe1
  title: FIBO source IND/InterestRates/InterestRates.rdf
title: base rate
type: Ontology Class
---

# base rate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/BaseRate>

## Definition

basic rate of interest on which the actual rate a bank charges on loans to its customers is calculated

## Relationships

- **Subclass of**: [ReferenceInterestRate](/concepts/fibo/IND/InterestRates/InterestRates/ReferenceInterestRate.md)

## Annotations

- **label**: base rate
- **definition**: basic rate of interest on which the actual rate a bank charges on loans to its customers is calculated
- **abbreviation**: BBR
- **explanatoryNote**: Typically, the bank base rate is a reference rate set by a central bank. Banks that are regulated by a given central bank cannot lend below the base rate to their customers. The bank base rate is determined on an ongoing basis and represents the central bank's judgement of the price of short-term funds on their interbank market.
- **synonym**: bank base rate

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
