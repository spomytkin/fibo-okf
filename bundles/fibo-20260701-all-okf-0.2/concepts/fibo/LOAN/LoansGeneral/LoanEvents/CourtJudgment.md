---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: court judgment
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: decision by a court or other tribunal that resolves a controversy and determines the rights and obligations of
      the parties
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanEvents/hasJudgementAmount
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCore/CourtOfLaw
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanEvents/isDeliveredBy
  subclass_of:
  - concept: /concepts/fibo/LOAN/LoansGeneral/LoanEvents/LegalProceeding.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanEvents/LegalProceeding
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanEvents/CourtJudgment
sources:
- id: fibo-source-48fe43dc99
  resource: references/fibo/LOAN/LoansGeneral/LoanEvents.rdf
  sha256: 48fe43dc99b1d7ca56ee712ff80baad56b5ac6abd1e4cb8ac5342e7bdee88e6e
  title: FIBO source LOAN/LoansGeneral/LoanEvents.rdf
title: court judgment
type: Ontology Class
---

# court judgment

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanEvents/CourtJudgment>

## Definition

decision by a court or other tribunal that resolves a controversy and determines the rights and obligations of the parties

## Relationships

- **Subclass of**: [LegalProceeding](/concepts/fibo/LOAN/LoansGeneral/LoanEvents/LegalProceeding.md)

## Constraints

- **[hasJudgementAmount](/concepts/fibo/LOAN/LoansGeneral/LoanEvents/hasJudgementAmount.md)**: min qualified cardinality 0 of type [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- **[isDeliveredBy](/concepts/fibo/LOAN/LoansGeneral/LoanEvents/isDeliveredBy.md)**: some values from of type [CourtOfLaw](/concepts/fibo/FND/Law/LegalCore/CourtOfLaw.md)

## Annotations

- **label** (en): court judgment
- **definition** (en): decision by a court or other tribunal that resolves a controversy and determines the rights and obligations of the parties

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
