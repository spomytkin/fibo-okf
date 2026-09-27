---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Bank of Canada
  - language: fr
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Banque du Canada
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: central bank of Canada
  - language: en
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasLegalName
    value: Bank of Canada
  - language: fr
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasLegalName
    value: Banque du Canada
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.bankofcanada.ca/wp-content/uploads/2010/11/regulation_canadian_financial.pdf
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: "The Bank of Canada's overall goal is to promote a stable and efficient financial system in Canada. The focus on\
      \ the financial system as a whole parallels the Bank's approach to monetary policy, which focuses on the entire economy.\n\
      \ \n The Bank provides liquidity to the financial system, gives policy advice to the federal government on the design\
      \ and development of the system, oversees major clearing and settlement systems, and provides banking services to these\
      \ systems and their participants."
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: https://www.bankofcanada.ca/
  defined_by:
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies/
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/GovernmentEntities/GovernmentAgency
  related_to:
  - concept: /concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/CAGovernmentEntitiesAndJurisdictions/CanadianJurisdiction.md
    predicate: https://www.omg.org/spec/Commons/RegulatoryAgencies/hasJurisdiction
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/CAGovernmentEntitiesAndJurisdictions/CanadianJurisdiction
  - concept: /concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/CAGovernmentEntitiesAndJurisdictions/GovernmentOfCanada.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/CAGovernmentEntitiesAndJurisdictions/GovernmentOfCanada
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies/BankOfCanadaHeadOfficeAddress.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/hasHeadquartersAddress
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies/BankOfCanadaHeadOfficeAddress
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies/BankOfCanada
sources:
- id: fibo-source-3a86c5f7dd
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies.rdf
  sha256: 3a86c5f7dd7acfa3d8ca47686faffd64ac5f85eae9e50730e1337823edbfcda4
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies.rdf
title: Bank of Canada
type: Ontology Individual
---

# Bank of Canada

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies/BankOfCanada>

## Definition

central bank of Canada

## Relationships

- **Defined by**: [CARegulatoryAgencies](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies.md)
- **Related to**: [BankOfCanadaHeadOfficeAddress](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies/BankOfCanadaHeadOfficeAddress.md)
- **Related to**: [GovernmentOfCanada](/concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/CAGovernmentEntitiesAndJurisdictions/GovernmentOfCanada.md)
- **Related to**: [CanadianJurisdiction](/concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/CAGovernmentEntitiesAndJurisdictions/CanadianJurisdiction.md)

## Annotations

- **label** (en): Bank of Canada
- **label** (fr): Banque du Canada
- **definition**: central bank of Canada
- **hasLegalName** (en): Bank of Canada
- **hasLegalName** (fr): Banque du Canada
- **adaptedFrom**: https://www.bankofcanada.ca/wp-content/uploads/2010/11/regulation_canadian_financial.pdf
- **explanatoryNote**: The Bank of Canada's overall goal is to promote a stable and efficient financial system in Canada. The focus on the financial system as a whole parallels the Bank's approach to monetary policy, which focuses on the entire economy.    The Bank provides liquidity to the financial system, gives policy advice to the federal government on the design and development of the system, oversees major clearing and settlement systems, and provides banking services to these systems and their participants.
- **hasWebsite**: https://www.bankofcanada.ca/

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
