---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: bankruptcy
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: credit event involving a change in state or condition in which a party becomes insolvent
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Barron's Dictionary of Banking Terms, Sixth Edition, 2012
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://thelawdictionary.org/bankruptcy/
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/CreditEvents/EntitySpecificCreditEvent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/EntitySpecificCreditEvent
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/Bankruptcy
sources:
- id: fibo-source-bc069e913f
  resource: references/fibo/FBC/DebtAndEquities/CreditEvents.rdf
  sha256: bc069e913f78f120d461cf77899be0452acda5d5786c9cd342e37931a2b141c6
  title: FIBO source FBC/DebtAndEquities/CreditEvents.rdf
title: bankruptcy
type: Ontology Class
---

# bankruptcy

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/Bankruptcy>

## Definition

credit event involving a change in state or condition in which a party becomes insolvent

## Relationships

- **Subclass of**: [EntitySpecificCreditEvent](/concepts/fibo/FBC/DebtAndEquities/CreditEvents/EntitySpecificCreditEvent.md)

## Annotations

- **label** (en): bankruptcy
- **definition** (en): credit event involving a change in state or condition in which a party becomes insolvent
- **adaptedFrom**: Barron's Dictionary of Banking Terms, Sixth Edition, 2012
- **adaptedFrom**: https://thelawdictionary.org/bankruptcy/

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
