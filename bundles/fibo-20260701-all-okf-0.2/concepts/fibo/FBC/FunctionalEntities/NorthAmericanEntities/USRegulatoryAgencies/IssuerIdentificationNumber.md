---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: issuer identification number
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: a numbering system that allows a credit, debit, or other card to be identified as having been issued by a particular
      financial institution
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: IIN
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: IINs are issued directly by the American Banker's Association (ABA) in the US. The ABA is the Registration Authority
      (RA) for ISO/IEC 7812, which defines the IIN, in other words.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The issuer identification number (IIN) is a six digit number that is unique to a single card issuer. The number
      is only used to identify the card issuer, and is not used to identify a particular product, service, or region associated
      with the card issuer.
  defined_by:
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/identifies
  - kind: has_value
    property: https://www.omg.org/spec/Commons/RegistrationAuthorities/hasRegistrationAuthority
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/AmericanBankersAssociationRegistrationAuthority
  - kind: has_value
    property: https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredBy
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/AmericanBankersAssociationRegistrationAuthority
  - kind: has_value
    property: https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredIn
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/ABAIINRegistry
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://en.wikipedia.org/wiki/ISO/IEC_7812
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/FinancialServiceProviderIdentifier.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/FinancialServiceProviderIdentifier
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/RegistrationAuthorities/RegisteredIdentifier
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/IssuerIdentificationNumber
sources:
- id: fibo-source-de74203ca3
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
  sha256: de74203ca3e67fe717b4f2da9cb381abdc316f91968b3e36439872a1a684d25f
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
title: issuer identification number
type: Ontology Class
---

# issuer identification number

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/IssuerIdentificationNumber>

## Definition

a numbering system that allows a credit, debit, or other card to be identified as having been issued by a particular financial institution

## Relationships

- **Defined by**: [USRegulatoryAgencies](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.md)
- **See also**: [IEC_7812](<https://en.wikipedia.org/wiki/ISO/IEC_7812>)
- **Subclass of**: [FinancialServiceProviderIdentifier](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/FinancialServiceProviderIdentifier.md)
- **Subclass of**: [RegisteredIdentifier](<https://www.omg.org/spec/Commons/RegistrationAuthorities/RegisteredIdentifier>)

## Constraints

- **[identifies](<https://www.omg.org/spec/Commons/Identifiers/identifies>)**: exact qualified cardinality 1 of type [FinancialInstitution](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md)
- **[hasRegistrationAuthority](<https://www.omg.org/spec/Commons/RegistrationAuthorities/hasRegistrationAuthority>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/AmericanBankersAssociationRegistrationAuthority`
- **[isRegisteredBy](<https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredBy>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/AmericanBankersAssociationRegistrationAuthority`
- **[isRegisteredIn](<https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredIn>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/ABAIINRegistry`

## Annotations

- **label**: issuer identification number
- **definition**: a numbering system that allows a credit, debit, or other card to be identified as having been issued by a particular financial institution
- **abbreviation**: IIN
- **explanatoryNote**: IINs are issued directly by the American Banker's Association (ABA) in the US. The ABA is the Registration Authority (RA) for ISO/IEC 7812, which defines the IIN, in other words.
- **explanatoryNote**: The issuer identification number (IIN) is a six digit number that is unique to a single card issuer. The number is only used to identify the card issuer, and is not used to identify a particular product, service, or region associated with the card issuer.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
