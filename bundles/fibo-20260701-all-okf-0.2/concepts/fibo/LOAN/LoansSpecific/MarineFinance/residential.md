---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: residential
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Whether the boat is intended to be used and is legally able to be used as a place of residence.
  domain:
  - concept: /concepts/fibo/LOAN/LoansSpecific/MarineFinance/MarineFinancing.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/MarineFinance/MarineFinancing
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/MarineFinance/residential
sources:
- id: fibo-source-ab59d0379b
  resource: references/fibo/LOAN/LoansSpecific/MarineFinance.rdf
  sha256: ab59d0379b2ad3a710669ccbb048f639d29436b20df95d91770694bf7f22c84e
  title: FIBO source LOAN/LoansSpecific/MarineFinance.rdf
title: residential
type: Ontology Property
---

# residential

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/MarineFinance/residential>

## Definition

Whether the boat is intended to be used and is legally able to be used as a place of residence.

## Relationships

- **Domain**: [MarineFinancing](/concepts/fibo/LOAN/LoansSpecific/MarineFinance/MarineFinancing.md)
- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label** (en): residential
- **definition** (en): Whether the boat is intended to be used and is legally able to be used as a place of residence.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
