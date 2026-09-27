---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is guaranteed by
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates guaranty to the contract guarantor, i.e., to the legal person providing the guaranty
  defined_by:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Guaranty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/
  domain:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Guaranty/Guaranty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/Guaranty
  range:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Guaranty/Guarantor.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/Guarantor
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/isGuaranteedBy
sources:
- id: fibo-source-a6bc9592ee
  resource: references/fibo/FBC/DebtAndEquities/Guaranty.rdf
  sha256: a6bc9592eeebb061e99b2dc168751d4b3612dbcc32c86c50959e17011e4247b0
  title: FIBO source FBC/DebtAndEquities/Guaranty.rdf
title: is guaranteed by
type: Ontology Property
---

# is guaranteed by

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/isGuaranteedBy>

## Definition

relates guaranty to the contract guarantor, i.e., to the legal person providing the guaranty

## Relationships

- **Defined by**: [Guaranty](/concepts/fibo/FBC/DebtAndEquities/Guaranty.md)
- **Domain**: [Guaranty](/concepts/fibo/FBC/DebtAndEquities/Guaranty/Guaranty.md)
- **Range**: [Guarantor](/concepts/fibo/FBC/DebtAndEquities/Guaranty/Guarantor.md)

## Annotations

- **label**: is guaranteed by
- **definition**: relates guaranty to the contract guarantor, i.e., to the legal person providing the guaranty

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
