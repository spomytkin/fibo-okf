---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is slice of
  domain:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/PromissoryNote.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/PromissoryNote
  inverse_of:
  - concept: /concepts/fibo/SEC/Debt/MortgageBackedSecurities/hasNote.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/hasNote
  range:
  - concept: /concepts/fibo/SEC/Debt/MortgageBackedSecurities/MortgageBackedSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/MortgageBackedSecurity
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Collections/isPartOf
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/isSliceOf
sources:
- id: fibo-source-025d7e8955
  resource: references/fibo/SEC/Debt/MortgageBackedSecurities.rdf
  sha256: 025d7e89558a319cbd2b60f6a11ca228190a5137c59ed5b5bf34878c5f976f60
  title: FIBO source SEC/Debt/MortgageBackedSecurities.rdf
title: is slice of
type: Ontology Property
---

# is slice of

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/isSliceOf>

## Relationships

- **Domain**: [PromissoryNote](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/PromissoryNote.md)
- **Inverse of**: [hasNote](/concepts/fibo/SEC/Debt/MortgageBackedSecurities/hasNote.md)
- **Range**: [MortgageBackedSecurity](/concepts/fibo/SEC/Debt/MortgageBackedSecurities/MortgageBackedSecurity.md)
- **Subproperty of**: [isPartOf](<https://www.omg.org/spec/Commons/Collections/isPartOf>)

## Annotations

- **label** (en): is slice of

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
