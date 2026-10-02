---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: business identifier code
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: international identifier for financial and non-financial institutions used to facilitate automated processing of
      information for financial services
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: BIC
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 9362:2014 Banking -- Banking telecommunication messages -- Business identifier code (BIC)
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The BIC is used for addressing messages, routing business transactions and identifying business parties. Note that
      the use of OrganizationSubUnitIdentifier in FIBO corresponds to the Branch Code in the SWIFT scheme.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: SWIFT ID
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: SWIFT code
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: SWIFT-BIC
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: bank identifier code
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: business entity identifier
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/BusinessPartyPrefix
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/BusinessPartySuffix
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - cardinality: 1
    filler: https://www.omg.org/spec/LCC/Countries/CountryRepresentation/Alpha2Code
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/Organizations/OrganizationSubUnitIdentifier
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/BusinessIdentifierCodeScheme
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/isMemberOf
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/Organizations/FormalOrganization
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Designators/denotes
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeElement
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/ContextualIdentifiers/StructuredIdentifier
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Organizations/OrganizationIdentifier
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/BusinessIdentifierCode
sources:
- id: fibo-source-6e6990f74b
  resource: references/fibo/FBC/FunctionalEntities/FinancialServicesEntities.rdf
  sha256: 6e6990f74b40d4b0500a945cb9492927f845764329794290952c527016de49c1
  title: FIBO source FBC/FunctionalEntities/FinancialServicesEntities.rdf
title: business identifier code
type: Ontology Class
---

# business identifier code

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/BusinessIdentifierCode>

## Definition

international identifier for financial and non-financial institutions used to facilitate automated processing of information for financial services

## Relationships

- **Subclass of**: [CodeElement](<https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeElement>)
- **Subclass of**: [StructuredIdentifier](<https://www.omg.org/spec/Commons/ContextualIdentifiers/StructuredIdentifier>)
- **Subclass of**: [OrganizationIdentifier](<https://www.omg.org/spec/Commons/Organizations/OrganizationIdentifier>)

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: exact qualified cardinality 1 of type [BusinessPartyPrefix](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/BusinessPartyPrefix.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: exact qualified cardinality 1 of type [BusinessPartySuffix](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/BusinessPartySuffix.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: exact qualified cardinality 1 of type [Alpha2Code](<https://www.omg.org/spec/LCC/Countries/CountryRepresentation/Alpha2Code>)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: min qualified cardinality 0 of type [OrganizationSubUnitIdentifier](<https://www.omg.org/spec/Commons/Organizations/OrganizationSubUnitIdentifier>)
- **[isMemberOf](<https://www.omg.org/spec/Commons/Collections/isMemberOf>)**: some values from of type [BusinessIdentifierCodeScheme](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/BusinessIdentifierCodeScheme.md)
- **[denotes](<https://www.omg.org/spec/Commons/Designators/denotes>)**: exact qualified cardinality 1 of type [FormalOrganization](<https://www.omg.org/spec/Commons/Organizations/FormalOrganization>)

## Annotations

- **label**: business identifier code
- **definition**: international identifier for financial and non-financial institutions used to facilitate automated processing of information for financial services
- **abbreviation**: BIC
- **adaptedFrom**: ISO 9362:2014 Banking -- Banking telecommunication messages -- Business identifier code (BIC)
- **explanatoryNote**: The BIC is used for addressing messages, routing business transactions and identifying business parties. Note that the use of OrganizationSubUnitIdentifier in FIBO corresponds to the Branch Code in the SWIFT scheme.
- **synonym**: SWIFT ID
- **synonym**: SWIFT code
- **synonym**: SWIFT-BIC
- **synonym**: bank identifier code
- **synonym**: business entity identifier

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
