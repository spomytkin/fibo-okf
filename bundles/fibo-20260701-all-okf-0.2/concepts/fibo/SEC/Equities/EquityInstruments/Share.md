---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: share
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: financial instrument that signifies a unit of equity ownership in a corporation, or a unit of ownership in a mutual
      fund, or interest in a general or limited partnership, or a unit of ownership in a structured product, such as a real
      estate investment trust
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: http://www.w3.org/2001/XMLSchema#nonNegativeInteger
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/hasSharesAuthorized
  - filler: http://www.w3.org/2001/XMLSchema#decimal
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/confersNumberOfVotesPerShare
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/ShareholdersEquity
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/confersOwnershipOf
  - cardinality: 0
    filler: http://www.w3.org/2001/XMLSchema#nonNegativeInteger
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasAvailableShares
  - cardinality: 0
    filler: http://www.w3.org/2001/XMLSchema#nonNegativeInteger
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasFloatingStock
  - cardinality: 0
    filler: http://www.w3.org/2001/XMLSchema#string
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasShareClass
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/SharePaymentStatus
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasSharePaymentStatus
  - cardinality: 0
    filler: http://www.w3.org/2001/XMLSchema#nonNegativeInteger
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasSharesIssued
  - cardinality: 0
    filler: http://www.w3.org/2001/XMLSchema#nonNegativeInteger
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasSharesOutstanding
  - cardinality: 0
    filler: http://www.w3.org/2001/XMLSchema#nonNegativeInteger
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasTreasuryShares
  - cardinality: 0
    filler: http://www.w3.org/2001/XMLSchema#string
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasVotingRestriction
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/EquityInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/EquityInstrument
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/Share
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: share
type: Ontology Class
---

# share

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/Share>

## Definition

financial instrument that signifies a unit of equity ownership in a corporation, or a unit of ownership in a mutual fund, or interest in a general or limited partnership, or a unit of ownership in a structured product, such as a real estate investment trust

## Relationships

- **Subclass of**: [EquityInstrument](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/EquityInstrument.md)

## Constraints

- **[hasSharesAuthorized](/concepts/fibo/BE/LegalEntities/CorporateBodies/hasSharesAuthorized.md)**: some values from of type [nonNegativeInteger](<http://www.w3.org/2001/XMLSchema#nonNegativeInteger>)
- **[confersNumberOfVotesPerShare](/concepts/fibo/SEC/Equities/EquityInstruments/confersNumberOfVotesPerShare.md)**: some values from of type [decimal](<http://www.w3.org/2001/XMLSchema#decimal>)
- **[confersOwnershipOf](/concepts/fibo/SEC/Equities/EquityInstruments/confersOwnershipOf.md)**: some values from of type [ShareholdersEquity](/concepts/fibo/FND/OwnershipAndControl/Ownership/ShareholdersEquity.md)
- **[hasAvailableShares](/concepts/fibo/SEC/Equities/EquityInstruments/hasAvailableShares.md)**: min qualified cardinality 0 of type [nonNegativeInteger](<http://www.w3.org/2001/XMLSchema#nonNegativeInteger>)
- **[hasFloatingStock](/concepts/fibo/SEC/Equities/EquityInstruments/hasFloatingStock.md)**: min qualified cardinality 0 of type [nonNegativeInteger](<http://www.w3.org/2001/XMLSchema#nonNegativeInteger>)
- **[hasShareClass](/concepts/fibo/SEC/Equities/EquityInstruments/hasShareClass.md)**: min qualified cardinality 0 of type [string](<http://www.w3.org/2001/XMLSchema#string>)
- **[hasSharePaymentStatus](/concepts/fibo/SEC/Equities/EquityInstruments/hasSharePaymentStatus.md)**: some values from of type [SharePaymentStatus](/concepts/fibo/SEC/Equities/EquityInstruments/SharePaymentStatus.md)
- **[hasSharesIssued](/concepts/fibo/SEC/Equities/EquityInstruments/hasSharesIssued.md)**: min qualified cardinality 0 of type [nonNegativeInteger](<http://www.w3.org/2001/XMLSchema#nonNegativeInteger>)
- **[hasSharesOutstanding](/concepts/fibo/SEC/Equities/EquityInstruments/hasSharesOutstanding.md)**: min qualified cardinality 0 of type [nonNegativeInteger](<http://www.w3.org/2001/XMLSchema#nonNegativeInteger>)
- **[hasTreasuryShares](/concepts/fibo/SEC/Equities/EquityInstruments/hasTreasuryShares.md)**: min qualified cardinality 0 of type [nonNegativeInteger](<http://www.w3.org/2001/XMLSchema#nonNegativeInteger>)
- **[hasVotingRestriction](/concepts/fibo/SEC/Equities/EquityInstruments/hasVotingRestriction.md)**: min qualified cardinality 0 of type [string](<http://www.w3.org/2001/XMLSchema#string>)

## Annotations

- **label** (en): share
- **definition** (en): financial instrument that signifies a unit of equity ownership in a corporation, or a unit of ownership in a mutual fund, or interest in a general or limited partnership, or a unit of ownership in a structured product, such as a real estate investment trust

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
