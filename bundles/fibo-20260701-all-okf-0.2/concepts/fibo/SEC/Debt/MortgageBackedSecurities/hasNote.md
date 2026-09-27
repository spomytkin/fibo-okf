---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has note
  domain:
  - concept: /concepts/fibo/SEC/Debt/MortgageBackedSecurities/MortgageBackedSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/MortgageBackedSecurity
  range:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/PromissoryNote.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/PromissoryNote
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Collections/hasPart
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/hasNote
sources:
- id: fibo-source-025d7e8955
  resource: references/fibo/SEC/Debt/MortgageBackedSecurities.rdf
  sha256: 025d7e89558a319cbd2b60f6a11ca228190a5137c59ed5b5bf34878c5f976f60
  title: FIBO source SEC/Debt/MortgageBackedSecurities.rdf
title: has note
type: Ontology Property
---

# has note

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/hasNote>

## Relationships

- **Domain**: [MortgageBackedSecurity](/concepts/fibo/SEC/Debt/MortgageBackedSecurities/MortgageBackedSecurity.md)
- **Range**: [PromissoryNote](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/PromissoryNote.md)
- **Subproperty of**: [hasPart](<https://www.omg.org/spec/Commons/Collections/hasPart>)

## Annotations

- **label** (en): has note

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
