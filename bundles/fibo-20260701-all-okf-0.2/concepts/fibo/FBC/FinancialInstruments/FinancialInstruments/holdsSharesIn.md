---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: holds shares in
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specifies the issuer in which a shareholder holds an equity position
  domain:
  - concept: /concepts/fibo/BE/OwnershipAndControl/CorporateOwnership/Shareholder.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/Shareholder
  inverse_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/hasShareholder.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/hasShareholder
  range:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Issuer.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Issuer
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/actsOn
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/holdsSharesIn
sources:
- id: fibo-source-b40f618e3f
  resource: references/fibo/FBC/FinancialInstruments/FinancialInstruments.rdf
  sha256: b40f618e3feb2ca2bdd67c28d622728874d183b83fab1c57f77493cd81da088c
  title: FIBO source FBC/FinancialInstruments/FinancialInstruments.rdf
title: holds shares in
type: Ontology Property
---

# holds shares in

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/holdsSharesIn>

## Definition

specifies the issuer in which a shareholder holds an equity position

## Relationships

- **Domain**: [Shareholder](/concepts/fibo/BE/OwnershipAndControl/CorporateOwnership/Shareholder.md)
- **Inverse of**: [hasShareholder](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/hasShareholder.md)
- **Range**: [Issuer](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Issuer.md)
- **Subproperty of**: [actsOn](<https://www.omg.org/spec/Commons/PartiesAndSituations/actsOn>)

## Annotations

- **label**: holds shares in
- **definition**: specifies the issuer in which a shareholder holds an equity position

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
