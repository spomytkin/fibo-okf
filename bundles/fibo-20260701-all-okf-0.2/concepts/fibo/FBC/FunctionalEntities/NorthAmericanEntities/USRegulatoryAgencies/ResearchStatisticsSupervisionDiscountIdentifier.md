---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Research, Statistics, Supervision and Regulation, and Discount and Credit identifier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: unique identifier assigned by the Federal Reserve to financial institutions for regulatory and oversight purposes
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: RSSD ID
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://cdr.ffiec.gov/CDR/Public/CDRHelp/FAQs1205.htm#FAQ16
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: ID_RSSD
  defined_by:
  - predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://www.federalreserve.gov/reportforms/mdrm/pdf/RSSD.PDF
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredBy
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FederalReserveRegulatoryAgencyAndCentralBank
  - kind: has_value
    property: https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredIn
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/NationalInformationCenterRepository
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/FinancialServiceProviderIdentifier.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/FinancialServiceProviderIdentifier
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/RegistrationAuthorities/RegisteredIdentifier
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/ResearchStatisticsSupervisionDiscountIdentifier
sources:
- id: fibo-source-de74203ca3
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
  sha256: de74203ca3e67fe717b4f2da9cb381abdc316f91968b3e36439872a1a684d25f
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
title: Research, Statistics, Supervision and Regulation, and Discount and Credit identifier
type: Ontology Class
---

# Research, Statistics, Supervision and Regulation, and Discount and Credit identifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/ResearchStatisticsSupervisionDiscountIdentifier>

## Definition

unique identifier assigned by the Federal Reserve to financial institutions for regulatory and oversight purposes

## Relationships

- **Defined by**: [RSSD.PDF](<https://www.federalreserve.gov/reportforms/mdrm/pdf/RSSD.PDF>)
- **Subclass of**: [FinancialServiceProviderIdentifier](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/FinancialServiceProviderIdentifier.md)
- **Subclass of**: [RegisteredIdentifier](<https://www.omg.org/spec/Commons/RegistrationAuthorities/RegisteredIdentifier>)

## Constraints

- **[isRegisteredBy](<https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredBy>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/FederalReserveRegulatoryAgencyAndCentralBank`
- **[isRegisteredIn](<https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredIn>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/NationalInformationCenterRepository`

## Annotations

- **label**: Research, Statistics, Supervision and Regulation, and Discount and Credit identifier
- **definition**: unique identifier assigned by the Federal Reserve to financial institutions for regulatory and oversight purposes
- **abbreviation**: RSSD ID
- **adaptedFrom**: https://cdr.ffiec.gov/CDR/Public/CDRHelp/FAQs1205.htm#FAQ16
- **synonym**: ID_RSSD

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
