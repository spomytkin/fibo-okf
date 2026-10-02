---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has judgement amount
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: 'Undefined PoC SDM Notes: Total value of CCJs or equivalent recorded against the primary borrower that were satisfied
      / unsatsified (at time of underwriting ) is computed by selecting the satisfaction code value of interest and aggregating
      against all borrower CC Judgements &lt;/p&gt;'
  domain:
  - concept: /concepts/fibo/LOAN/LoansGeneral/LoanEvents/CourtJudgment.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanEvents/CourtJudgment
  range:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/hasMonetaryAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasMonetaryAmount
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanEvents/hasJudgementAmount
sources:
- id: fibo-source-48fe43dc99
  resource: references/fibo/LOAN/LoansGeneral/LoanEvents.rdf
  sha256: 48fe43dc99b1d7ca56ee712ff80baad56b5ac6abd1e4cb8ac5342e7bdee88e6e
  title: FIBO source LOAN/LoansGeneral/LoanEvents.rdf
title: has judgement amount
type: Ontology Property
---

# has judgement amount

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanEvents/hasJudgementAmount>

## Definition

Undefined PoC SDM Notes: Total value of CCJs or equivalent recorded against the primary borrower that were satisfied / unsatsified (at time of underwriting ) is computed by selecting the satisfaction code value of interest and aggregating against all borrower CC Judgements &lt;/p&gt;

## Relationships

- **Domain**: [CourtJudgment](/concepts/fibo/LOAN/LoansGeneral/LoanEvents/CourtJudgment.md)
- **Range**: [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- **Subproperty of**: [hasMonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/hasMonetaryAmount.md)

## Annotations

- **label** (en): has judgement amount
- **definition** (en): Undefined PoC SDM Notes: Total value of CCJs or equivalent recorded against the primary borrower that were satisfied / unsatsified (at time of underwriting ) is computed by selecting the satisfaction code value of interest and aggregating against all borrower CC Judgements &lt;/p&gt;

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
