---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: taxpayer identification number
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identification number used by the Internal Revenue Service (IRS) in the administration of tax laws in the United
      States
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: TIN
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.irs.gov/individuals/international-taxpayers/taxpayer-identification-numbers-tin
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'A TIN must be furnished on returns, statements, and other tax related documents. For example a number must be
      furnished:

      - When filing tax returns.

      - When claiming treaty benefits.


      A TIN must be on a withholding certificate if the beneficial owner is claiming any of the following:

      - Tax treaty benefits (other than for income from marketable securities)

      - Exemption for effectively connected income

      - Exemption for certain annuities.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/TaxpayerIdentificationNumberingScheme
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/isMemberOf
  - kind: has_value
    property: https://www.omg.org/spec/Commons/ContextualDesignators/isApplicableIn
    value: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/UnitedStatesJurisdiction
  subclass_of:
  - concept: /concepts/fibo/FND/Parties/Parties/TaxIdentifier.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Parties/Parties/TaxIdentifier
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/TaxpayerIdentificationNumber
sources:
- id: fibo-source-de74203ca3
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
  sha256: de74203ca3e67fe717b4f2da9cb381abdc316f91968b3e36439872a1a684d25f
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies.rdf
title: taxpayer identification number
type: Ontology Class
---

# taxpayer identification number

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/TaxpayerIdentificationNumber>

## Definition

identification number used by the Internal Revenue Service (IRS) in the administration of tax laws in the United States

## Relationships

- **Subclass of**: [TaxIdentifier](/concepts/fibo/FND/Parties/Parties/TaxIdentifier.md)

## Constraints

- **[isMemberOf](<https://www.omg.org/spec/Commons/Collections/isMemberOf>)**: exact qualified cardinality 1 of type [TaxpayerIdentificationNumberingScheme](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USRegulatoryAgencies/TaxpayerIdentificationNumberingScheme.md)
- **[isApplicableIn](<https://www.omg.org/spec/Commons/ContextualDesignators/isApplicableIn>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/USGovernmentEntitiesAndJurisdictions/UnitedStatesJurisdiction`

## Annotations

- **label**: taxpayer identification number
- **definition**: identification number used by the Internal Revenue Service (IRS) in the administration of tax laws in the United States
- **abbreviation**: TIN
- **adaptedFrom**: https://www.irs.gov/individuals/international-taxpayers/taxpayer-identification-numbers-tin
- **explanatoryNote**: A TIN must be furnished on returns, statements, and other tax related documents. For example a number must be furnished: - When filing tax returns. - When claiming treaty benefits.  A TIN must be on a withholding certificate if the beneficial owner is claiming any of the following: - Tax treaty benefits (other than for income from marketable securities) - Exemption for effectively connected income - Exemption for certain annuities.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
