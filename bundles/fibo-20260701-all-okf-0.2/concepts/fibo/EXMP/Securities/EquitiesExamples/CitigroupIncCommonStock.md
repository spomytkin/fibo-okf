---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Citigroup Inc. common stock
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: common share class representing shares in Citigroup Inc.
  - datatype: http://www.w3.org/2001/XMLSchema#boolean
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/isNegotiable
    value: 'true'
  - datatype: http://www.w3.org/2001/XMLSchema#boolean
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/isAssignable
    value: 'false'
  - predicate: https://www.omg.org/spec/Commons/RegistrationAuthorities/hasRegistrationDate
    value: '1998-09-29'
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityCFIClassificationIndividuals/CommonVotingUnrestrictedFullyPaidRegisteredShare
  - https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/ListedShare
  related_to:
  - concept: /concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/StateOfDelawareJurisdiction.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/isLegallyRecordedIn
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/StateOfDelawareJurisdiction
  - concept: /concepts/fibo/EXMP/Securities/EquitiesExamples/CitigroupIncEquityIssuer.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasPrincipalParty
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/EquitiesExamples/CitigroupIncEquityIssuer
  - concept: /concepts/fibo/EXMP/Securities/EquitiesExamples/CitigroupIncEquityIssuer.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isIssuedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/EquitiesExamples/CitigroupIncEquityIssuer
  - concept: /concepts/fibo/EXMP/Securities/EquitiesExamples/XNYSListedCitigroupIncCommonStock.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/isListedVia
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/EquitiesExamples/XNYSListedCitigroupIncCommonStock
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XNYS.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/hasHomeExchange
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XNYS
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XNYS.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/hasOriginalPlaceOfListing
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XNYS
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/SecuritiesAndExchangeRegulator.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/isRegisteredWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/SecuritiesAndExchangeRegulator
  - concept: /concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/USDollar.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/isDenominatedIn
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/USDollar
  - concept: /concepts/fibo/SEC/Equities/EquityCFIClassificationIndividuals/ESVUFR.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityCFIClassificationIndividuals/ESVUFR
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIssuance/BearerAndRegisteredForm.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/isIssuedInForm
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/BearerAndRegisteredForm
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIssuance/BookEntryForm.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/isIssuedInForm
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/BookEntryForm
resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/EquitiesExamples/CitigroupIncCommonStock
sources:
- id: fibo-source-67472951ed
  resource: references/fibo/EXMP/Securities/EquitiesExamples.rdf
  sha256: 67472951eda4ab333ca860aff880574f4629454478bbf8d10154cde935dfb619
  title: FIBO source EXMP/Securities/EquitiesExamples.rdf
title: Citigroup Inc. common stock
type: Ontology Individual
---

# Citigroup Inc. common stock

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/EquitiesExamples/CitigroupIncCommonStock>

## Definition

common share class representing shares in Citigroup Inc.

## Relationships

- **Related to**: [USDollar](/concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/USDollar.md)
- **Related to**: [StateOfDelawareJurisdiction](/concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/StateOfDelawareJurisdiction.md)
- **Related to**: [CitigroupIncEquityIssuer](/concepts/fibo/EXMP/Securities/EquitiesExamples/CitigroupIncEquityIssuer.md)
- **Related to**: [CitigroupIncEquityIssuer](/concepts/fibo/EXMP/Securities/EquitiesExamples/CitigroupIncEquityIssuer.md)
- **Related to**: [BearerAndRegisteredForm](/concepts/fibo/SEC/Securities/SecuritiesIssuance/BearerAndRegisteredForm.md)
- **Related to**: [BookEntryForm](/concepts/fibo/SEC/Securities/SecuritiesIssuance/BookEntryForm.md)
- **Related to**: [SecuritiesAndExchangeRegulator](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/SecuritiesAndExchangeRegulator.md)
- **Related to**: [Facility-XNYS](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XNYS.md)
- **Related to**: [Facility-XNYS](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XNYS.md)
- **Related to**: [XNYSListedCitigroupIncCommonStock](/concepts/fibo/EXMP/Securities/EquitiesExamples/XNYSListedCitigroupIncCommonStock.md)
- **Related to**: [ESVUFR](/concepts/fibo/SEC/Equities/EquityCFIClassificationIndividuals/ESVUFR.md)

## Annotations

- **label**: Citigroup Inc. common stock
- **definition**: common share class representing shares in Citigroup Inc.
- **isNegotiable**: true
- **isAssignable**: false
- **hasRegistrationDate**: 1998-09-29

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
