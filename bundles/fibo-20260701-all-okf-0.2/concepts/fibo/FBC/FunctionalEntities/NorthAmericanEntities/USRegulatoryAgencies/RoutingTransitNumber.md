---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: routing transit number
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: unique nine digit identifier, used primarily in the United States, to identify a banking or other financial institution
      for clearing funds, and, as it appears on a check, denotes the banking institution that holds the account from which
      funds are to be drawn
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: RTN
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Routing transit numbers are issued by Accuity on behalf of the American Bankers Association (ABA).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'The ABA RTN was originally designed to facilitate the sorting, bundling, and shipment of paper checks back to
      the drawer''s (check writer''s) account. As new payment methods were developed (ACH and Wire), the system was expanded
      to accommodate these payment methods.


      The ABA RTN is necessary for the Federal Reserve Banks to process Fedwire funds transfers, and by the Automated Clearing
      House to process direct deposits, bill payments, and other such automated transfers.'
  defined_by:
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://www.omg.org/spec/Commons/RegistrationAuthorities/hasRegistrationAuthority
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/AmericanBankersAssociationRegistrationAuthority
  - kind: has_value
    property: https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredBy
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/AmericanBankersAssociationRTNRegistrar
  - kind: has_value
    property: https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredIn
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/ABARTNRegistry
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: http://www.accuity.com/aba-registrar/
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/FinancialServiceProviderIdentifier.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/FinancialServiceProviderIdentifier
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/RegistrationAuthorities/RegisteredIdentifier
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/RoutingTransitNumber
sources:
- id: fibo-source-de74203ca3
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
  sha256: de74203ca3e67fe717b4f2da9cb381abdc316f91968b3e36439872a1a684d25f
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
title: routing transit number
type: Ontology Class
---

# routing transit number

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/RoutingTransitNumber>

## Definition

unique nine digit identifier, used primarily in the United States, to identify a banking or other financial institution for clearing funds, and, as it appears on a check, denotes the banking institution that holds the account from which funds are to be drawn

## Relationships

- **Defined by**: [USRegulatoryAgencies](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.md)
- **See also**: [aba-registrar](<http://www.accuity.com/aba-registrar/>)
- **Subclass of**: [FinancialServiceProviderIdentifier](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/FinancialServiceProviderIdentifier.md)
- **Subclass of**: [RegisteredIdentifier](<https://www.omg.org/spec/Commons/RegistrationAuthorities/RegisteredIdentifier>)

## Constraints

- **[hasRegistrationAuthority](<https://www.omg.org/spec/Commons/RegistrationAuthorities/hasRegistrationAuthority>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/AmericanBankersAssociationRegistrationAuthority`
- **[isRegisteredBy](<https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredBy>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/AmericanBankersAssociationRTNRegistrar`
- **[isRegisteredIn](<https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredIn>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/ABARTNRegistry`

## Annotations

- **label**: routing transit number
- **definition**: unique nine digit identifier, used primarily in the United States, to identify a banking or other financial institution for clearing funds, and, as it appears on a check, denotes the banking institution that holds the account from which funds are to be drawn
- **abbreviation**: RTN
- **explanatoryNote**: Routing transit numbers are issued by Accuity on behalf of the American Bankers Association (ABA).
- **explanatoryNote**: The ABA RTN was originally designed to facilitate the sorting, bundling, and shipment of paper checks back to the drawer's (check writer's) account. As new payment methods were developed (ACH and Wire), the system was expanded to accommodate these payment methods.  The ABA RTN is necessary for the Federal Reserve Banks to process Fedwire funds transfers, and by the Automated Clearing House to process direct deposits, bill payments, and other such automated transfers.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
