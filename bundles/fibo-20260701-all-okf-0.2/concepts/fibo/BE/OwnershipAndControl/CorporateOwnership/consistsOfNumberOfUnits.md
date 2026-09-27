---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: consists of number of units
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the number of units of
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This property indicates the number of units (e.g., shares, fund units) of the asset held in a shareholding or position,
      for example.
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#decimal
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/hasAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasAmount
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/consistsOfNumberOfUnits
sources:
- id: fibo-source-4d1bc90c45
  resource: references/fibo/BE/OwnershipAndControl/CorporateOwnership.rdf
  sha256: 4d1bc90c4583cdc3c4f8228a8afb505706731dd0d76b848f6678e714ee5ac147
  title: FIBO source BE/OwnershipAndControl/CorporateOwnership.rdf
title: consists of number of units
type: Ontology Property
---

# consists of number of units

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/consistsOfNumberOfUnits>

## Definition

indicates the number of units of

## Relationships

- **Range**: [decimal](<http://www.w3.org/2001/XMLSchema#decimal>)
- **Subproperty of**: [hasAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/hasAmount.md)

## Annotations

- **label** (en): consists of number of units
- **definition** (en): indicates the number of units of
- **explanatoryNote**: This property indicates the number of units (e.g., shares, fund units) of the asset held in a shareholding or position, for example.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
