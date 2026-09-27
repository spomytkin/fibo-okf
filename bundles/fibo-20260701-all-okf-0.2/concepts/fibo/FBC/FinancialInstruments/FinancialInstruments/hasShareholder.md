---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has shareholder
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates a party that holds shares in the issuer
  domain:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Issuer.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Issuer
  range:
  - concept: /concepts/fibo/BE/OwnershipAndControl/CorporateOwnership/Shareholder.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/Shareholder
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/isAffectedBy
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasShareholder
sources:
- id: fibo-source-b40f618e3f
  resource: references/fibo/FBC/FinancialInstruments/FinancialInstruments.rdf
  sha256: b40f618e3feb2ca2bdd67c28d622728874d183b83fab1c57f77493cd81da088c
  title: FIBO source FBC/FinancialInstruments/FinancialInstruments.rdf
title: has shareholder
type: Ontology Property
---

# has shareholder

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasShareholder>

## Definition

indicates a party that holds shares in the issuer

## Relationships

- **Domain**: [Issuer](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Issuer.md)
- **Range**: [Shareholder](/concepts/fibo/BE/OwnershipAndControl/CorporateOwnership/Shareholder.md)
- **Subproperty of**: [isAffectedBy](<https://www.omg.org/spec/Commons/PartiesAndSituations/isAffectedBy>)

## Annotations

- **label**: has shareholder
- **definition**: indicates a party that holds shares in the issuer

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
