---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: employer identification number
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: unique nine-digit number assigned by the Internal Revenue Service (IRS) to business entities operating in the United
      States for the purposes of identification
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: EIN
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: FEIN
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.irs.gov/businesses/small-businesses-self-employed/employer-id-numbers
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Note that despite the name, the business may not necessarily employ anyone.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: Federal Employer Identification Number
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: Federal Tax Identification Number
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/EmployerIdentificationNumberingScheme
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/isMemberOf
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/TaxpayerIdentificationNumber.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/TaxpayerIdentificationNumber
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Organizations/OrganizationIdentifier
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/EmployerIdentificationNumber
sources:
- id: fibo-source-de74203ca3
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
  sha256: de74203ca3e67fe717b4f2da9cb381abdc316f91968b3e36439872a1a684d25f
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
title: employer identification number
type: Ontology Class
---

# employer identification number

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/EmployerIdentificationNumber>

## Definition

unique nine-digit number assigned by the Internal Revenue Service (IRS) to business entities operating in the United States for the purposes of identification

## Relationships

- **Subclass of**: [TaxpayerIdentificationNumber](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/TaxpayerIdentificationNumber.md)
- **Subclass of**: [OrganizationIdentifier](<https://www.omg.org/spec/Commons/Organizations/OrganizationIdentifier>)

## Constraints

- **[isMemberOf](<https://www.omg.org/spec/Commons/Collections/isMemberOf>)**: exact qualified cardinality 1 of type [EmployerIdentificationNumberingScheme](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/EmployerIdentificationNumberingScheme.md)

## Annotations

- **label**: employer identification number
- **definition**: unique nine-digit number assigned by the Internal Revenue Service (IRS) to business entities operating in the United States for the purposes of identification
- **abbreviation**: EIN
- **abbreviation**: FEIN
- **adaptedFrom**: https://www.irs.gov/businesses/small-businesses-self-employed/employer-id-numbers
- **explanatoryNote**: Note that despite the name, the business may not necessarily employ anyone.
- **synonym**: Federal Employer Identification Number
- **synonym**: Federal Tax Identification Number

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
