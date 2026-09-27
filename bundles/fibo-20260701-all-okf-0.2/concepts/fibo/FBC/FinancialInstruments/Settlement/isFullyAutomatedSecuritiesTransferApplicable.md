---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is fully automated securities transfer applicable
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates whether the security is to be held at the transfer agent as part of the FAST (Fully Automated Securities
      Transfer) program
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: is FAST applicable
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The Fast Automated Securities Transfer Program (FAST) is a contract between DTC (and its subsidiaries) and transfer
      agents whereby FAST agents act as custodians for DTC.
  domain:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/SettlementTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/SettlementTerms
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/Settlement/isFullyAutomatedSecuritiesTransferApplicable
sources:
- id: fibo-source-89377f435c
  resource: references/fibo/FBC/FinancialInstruments/Settlement.rdf
  sha256: 89377f435ce3f9d5ae76a4c2bf85b0591df9c10d237d0a2ca9700d9da0c4da5c
  title: FIBO source FBC/FinancialInstruments/Settlement.rdf
title: is fully automated securities transfer applicable
type: Ontology Property
---

# is fully automated securities transfer applicable

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/Settlement/isFullyAutomatedSecuritiesTransferApplicable>

## Definition

indicates whether the security is to be held at the transfer agent as part of the FAST (Fully Automated Securities Transfer) program

## Relationships

- **Domain**: [SettlementTerms](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/SettlementTerms.md)
- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label**: is fully automated securities transfer applicable
- **definition**: indicates whether the security is to be held at the transfer agent as part of the FAST (Fully Automated Securities Transfer) program
- **abbreviation**: is FAST applicable
- **explanatoryNote**: The Fast Automated Securities Transfer Program (FAST) is a contract between DTC (and its subsidiaries) and transfer agents whereby FAST agents act as custodians for DTC.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
