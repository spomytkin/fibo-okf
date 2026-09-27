---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: non-negotiable security
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: security that is not transferable to another party
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Certain securities that can be redeemed by the issuer may not be 'negotiable', such as savings bonds and certificates
      of deposit.
  disjoint_with:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/NegotiableSecurity.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/NegotiableSecurity
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Security.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Security
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/NonNegotiableSecurity
sources:
- id: fibo-source-b40f618e3f
  resource: references/fibo/FBC/FinancialInstruments/FinancialInstruments.rdf
  sha256: b40f618e3feb2ca2bdd67c28d622728874d183b83fab1c57f77493cd81da088c
  title: FIBO source FBC/FinancialInstruments/FinancialInstruments.rdf
title: non-negotiable security
type: Ontology Class
---

# non-negotiable security

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/NonNegotiableSecurity>

## Definition

security that is not transferable to another party

## Relationships

- **Subclass of**: [Security](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Security.md)

## Constraints

- **Disjoint with**: [NegotiableSecurity](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/NegotiableSecurity.md)

## Annotations

- **label**: non-negotiable security
- **definition**: security that is not transferable to another party
- **explanatoryNote**: Certain securities that can be redeemed by the issuer may not be 'negotiable', such as savings bonds and certificates of deposit.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
