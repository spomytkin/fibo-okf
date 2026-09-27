---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Alphabet Inc. class C capital stock
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: common share class that represents class C series shares in Alphabet Inc.
  - datatype: http://www.w3.org/2001/XMLSchema#boolean
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/isNegotiable
    value: 'true'
  - datatype: http://www.w3.org/2001/XMLSchema#boolean
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/isAssignable
    value: 'false'
  - predicate: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/hasShareClass
    value: C
  - predicate: https://www.omg.org/spec/Commons/RegistrationAuthorities/hasRegistrationDate
    value: '2015-10-02'
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityCFIClassificationIndividuals/CommonNonVotingUnrestrictedFullyPaidRegisteredShare
  - https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/ListedShare
  related_to:
  - concept: /concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/StateOfDelawareJurisdiction.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/isLegallyRecordedIn
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/StateOfDelawareJurisdiction
  - concept: /concepts/fibo/EXMP/Securities/EquitiesExamples/AlphabetIncEquityIssuer.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasPrincipalParty
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/EquitiesExamples/AlphabetIncEquityIssuer
  - concept: /concepts/fibo/EXMP/Securities/EquitiesExamples/AlphabetIncEquityIssuer.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isIssuedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/EquitiesExamples/AlphabetIncEquityIssuer
  - concept: /concepts/fibo/EXMP/Securities/EquitiesExamples/XNASListedAlphabetIncClassCCapitalStock.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/isListedVia
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/EquitiesExamples/XNASListedAlphabetIncClassCCapitalStock
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XNAS.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/hasHomeExchange
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XNAS
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XNAS.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/hasOriginalPlaceOfListing
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XNAS
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/SecuritiesAndExchangeRegulator.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/isRegisteredWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/SecuritiesAndExchangeRegulator
  - concept: /concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/USDollar.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/isDenominatedIn
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/USDollar
  - concept: /concepts/fibo/SEC/Equities/EquityCFIClassificationIndividuals/ESNUFR.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityCFIClassificationIndividuals/ESNUFR
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIssuance/BookEntryForm.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/isIssuedInForm
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/BookEntryForm
resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/EquitiesExamples/AlphabetIncClassCCapitalStock
sources:
- id: fibo-source-67472951ed
  resource: references/fibo/EXMP/Securities/EquitiesExamples.rdf
  sha256: 67472951eda4ab333ca860aff880574f4629454478bbf8d10154cde935dfb619
  title: FIBO source EXMP/Securities/EquitiesExamples.rdf
title: Alphabet Inc. class C capital stock
type: Ontology Individual
---

# Alphabet Inc. class C capital stock

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/EquitiesExamples/AlphabetIncClassCCapitalStock>

## Definition

common share class that represents class C series shares in Alphabet Inc.

## Relationships

- **Related to**: [USDollar](/concepts/fibo/FND/Accounting/ISO4217-CurrencyCodes/USDollar.md)
- **Related to**: [StateOfDelawareJurisdiction](/concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/StateOfDelawareJurisdiction.md)
- **Related to**: [AlphabetIncEquityIssuer](/concepts/fibo/EXMP/Securities/EquitiesExamples/AlphabetIncEquityIssuer.md)
- **Related to**: [AlphabetIncEquityIssuer](/concepts/fibo/EXMP/Securities/EquitiesExamples/AlphabetIncEquityIssuer.md)
- **Related to**: [BookEntryForm](/concepts/fibo/SEC/Securities/SecuritiesIssuance/BookEntryForm.md)
- **Related to**: [SecuritiesAndExchangeRegulator](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/SecuritiesAndExchangeRegulator.md)
- **Related to**: [Facility-XNAS](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XNAS.md)
- **Related to**: [Facility-XNAS](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XNAS.md)
- **Related to**: [XNASListedAlphabetIncClassCCapitalStock](/concepts/fibo/EXMP/Securities/EquitiesExamples/XNASListedAlphabetIncClassCCapitalStock.md)
- **Related to**: [ESNUFR](/concepts/fibo/SEC/Equities/EquityCFIClassificationIndividuals/ESNUFR.md)

## Annotations

- **label**: Alphabet Inc. class C capital stock
- **definition**: common share class that represents class C series shares in Alphabet Inc.
- **isNegotiable**: true
- **isAssignable**: false
- **hasShareClass**: C
- **hasRegistrationDate**: 2015-10-02

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
