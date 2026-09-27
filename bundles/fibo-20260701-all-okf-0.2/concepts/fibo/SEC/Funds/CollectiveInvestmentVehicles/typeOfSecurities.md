---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: type of securities
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The type of securities or other holdings that may be invested in.
  domain:
  - concept: /concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/InvestmentRestriction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/InvestmentRestriction
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#string
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/typeOfSecurities
sources:
- id: fibo-source-ee709790f7
  resource: references/fibo/SEC/Funds/CollectiveInvestmentVehicles.rdf
  sha256: ee709790f7157eacba64b78b55ac3e69da45c99673be17ca2df35d4f0ed3230c
  title: FIBO source SEC/Funds/CollectiveInvestmentVehicles.rdf
title: type of securities
type: Ontology Property
---

# type of securities

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/CollectiveInvestmentVehicles/typeOfSecurities>

## Definition

The type of securities or other holdings that may be invested in.

## Relationships

- **Domain**: [InvestmentRestriction](/concepts/fibo/SEC/Funds/CollectiveInvestmentVehicles/InvestmentRestriction.md)
- **Range**: [string](<http://www.w3.org/2001/XMLSchema#string>)

## Annotations

- **label** (en): type of securities
- **definition** (en): The type of securities or other holdings that may be invested in.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
