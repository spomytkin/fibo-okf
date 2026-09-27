---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: boat held as chattel
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Whether the vessel is to be held in ownership as a form of chattel by the lender during the period of the loan.
  domain:
  - concept: /concepts/fibo/LOAN/LoansSpecific/MarineFinance/MarineFinancing.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/MarineFinance/MarineFinancing
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/MarineFinance/boatHeldAsChattel
sources:
- id: fibo-source-ab59d0379b
  resource: references/fibo/LOAN/LoansSpecific/MarineFinance.rdf
  sha256: ab59d0379b2ad3a710669ccbb048f639d29436b20df95d91770694bf7f22c84e
  title: FIBO source LOAN/LoansSpecific/MarineFinance.rdf
title: boat held as chattel
type: Ontology Property
---

# boat held as chattel

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/MarineFinance/boatHeldAsChattel>

## Definition

Whether the vessel is to be held in ownership as a form of chattel by the lender during the period of the loan.

## Relationships

- **Domain**: [MarineFinancing](/concepts/fibo/LOAN/LoansSpecific/MarineFinance/MarineFinancing.md)
- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label** (en): boat held as chattel
- **definition** (en): Whether the vessel is to be held in ownership as a form of chattel by the lender during the period of the loan.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
