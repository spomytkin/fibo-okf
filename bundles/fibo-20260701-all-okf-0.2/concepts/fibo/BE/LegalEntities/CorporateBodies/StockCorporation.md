---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: stock corporation
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: corporation that has shareholders, each of whom receives a portion of the ownership of the corporation through
      shares of stock
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.oecd.org/corporate/OECD-Corporate-Governance-Factbook.pdf
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The shares in a stock corporation may receive a return on their investment in the form of dividends. Shares are
      used for voting on matters of corporate policy or to elect directors, at the corporation's annual meeting and at other
      meetings of the corporation.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/hasDateOfIncorporation
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/hasDateOfRegistration
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/hasIssuedCapital
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/BoardAgreement
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RegulatoryAgencies/isGovernedBy
  subclass_of:
  - concept: /concepts/fibo/BE/LegalEntities/CorporateBodies/Corporation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/Corporation
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/StockCorporation
sources:
- id: fibo-source-6fa4a51dba
  resource: references/fibo/BE/LegalEntities/CorporateBodies.rdf
  sha256: 6fa4a51dba5b2409b4becae9f17299d91b3fd0da0b7a4439f6c3888b6f1dd363
  title: FIBO source BE/LegalEntities/CorporateBodies.rdf
title: stock corporation
type: Ontology Class
---

# stock corporation

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/StockCorporation>

## Definition

corporation that has shareholders, each of whom receives a portion of the ownership of the corporation through shares of stock

## Relationships

- **Subclass of**: [Corporation](/concepts/fibo/BE/LegalEntities/CorporateBodies/Corporation.md)

## Constraints

- **[hasDateOfIncorporation](/concepts/fibo/BE/LegalEntities/CorporateBodies/hasDateOfIncorporation.md)**: exact qualified cardinality 1 of type [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)
- **[hasDateOfRegistration](/concepts/fibo/BE/LegalEntities/CorporateBodies/hasDateOfRegistration.md)**: min qualified cardinality 0 of type [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)
- **[hasIssuedCapital](/concepts/fibo/BE/LegalEntities/CorporateBodies/hasIssuedCapital.md)**: exact qualified cardinality 1 of type [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- **[isGovernedBy](<https://www.omg.org/spec/Commons/RegulatoryAgencies/isGovernedBy>)**: some values from of type [BoardAgreement](/concepts/fibo/BE/LegalEntities/CorporateBodies/BoardAgreement.md)

## Annotations

- **label** (en): stock corporation
- **definition**: corporation that has shareholders, each of whom receives a portion of the ownership of the corporation through shares of stock
- **adaptedFrom**: https://www.oecd.org/corporate/OECD-Corporate-Governance-Factbook.pdf
- **explanatoryNote**: The shares in a stock corporation may receive a return on their investment in the form of dividends. Shares are used for voting on matters of corporate policy or to elect directors, at the corporation's annual meeting and at other meetings of the corporation.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
