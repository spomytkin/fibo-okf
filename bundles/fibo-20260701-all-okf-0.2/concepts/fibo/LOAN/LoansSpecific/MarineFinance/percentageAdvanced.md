---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: percentage advanced
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The percentage of the purchase price advanced as the loan.
  domain:
  - concept: /concepts/fibo/LOAN/LoansSpecific/MarineFinance/MarineFinancing.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/MarineFinance/MarineFinancing
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/Percentage
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/MarineFinance/percentageAdvanced
sources:
- id: fibo-source-ab59d0379b
  resource: references/fibo/LOAN/LoansSpecific/MarineFinance.rdf
  sha256: ab59d0379b2ad3a710669ccbb048f639d29436b20df95d91770694bf7f22c84e
  title: FIBO source LOAN/LoansSpecific/MarineFinance.rdf
title: percentage advanced
type: Ontology Property
---

# percentage advanced

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/MarineFinance/percentageAdvanced>

## Definition

The percentage of the purchase price advanced as the loan.

## Relationships

- **Domain**: [MarineFinancing](/concepts/fibo/LOAN/LoansSpecific/MarineFinance/MarineFinancing.md)
- **Range**: [Percentage](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/Percentage>)

## Annotations

- **label** (en): percentage advanced
- **definition** (en): The percentage of the purchase price advanced as the loan.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
