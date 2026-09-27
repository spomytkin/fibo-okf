---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: denomination
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The currency amount in which the Note is denominated, for example $500 notes. This term added by symmettry with
      MBS Tranche Note. needs to be reviewed and validated.
  domain:
  - concept: /concepts/fibo/SEC/Debt/MortgageBackedSecurities/PassThroughMBSInstrumentNote.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/PassThroughMBSInstrumentNote
  range:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/denomination.1
sources:
- id: fibo-source-025d7e8955
  resource: references/fibo/SEC/Debt/MortgageBackedSecurities.rdf
  sha256: 025d7e89558a319cbd2b60f6a11ca228190a5137c59ed5b5bf34878c5f976f60
  title: FIBO source SEC/Debt/MortgageBackedSecurities.rdf
title: denomination
type: Ontology Property
---

# denomination

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/denomination.1>

## Definition

The currency amount in which the Note is denominated, for example $500 notes. This term added by symmettry with MBS Tranche Note. needs to be reviewed and validated.

## Relationships

- **Domain**: [PassThroughMBSInstrumentNote](/concepts/fibo/SEC/Debt/MortgageBackedSecurities/PassThroughMBSInstrumentNote.md)
- **Range**: [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)

## Annotations

- **label** (en): denomination
- **definition** (en): The currency amount in which the Note is denominated, for example $500 notes. This term added by symmettry with MBS Tranche Note. needs to be reviewed and validated.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
