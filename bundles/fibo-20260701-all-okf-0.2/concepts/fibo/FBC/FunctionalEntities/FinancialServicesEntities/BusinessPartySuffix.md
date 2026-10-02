---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: business party suffix
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: two-character (2 alphanumeric) code associated with the organization for the purposes of banking telecommunications
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 9362:2014 Banking -- Banking telecommunication messages -- Business identifier code (BIC)
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In the prior version of the standard, position 7 of the BIC determined the location of the BIC in a particular
      country. In a country spanning over multiple time zones, each character may have been used to define a different time
      zone. If an organization moved location to a different time zone within the same country, the existing BIC would normally
      have been deleted and replaced by a new BIC with the appropriate location code.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: With the revision of the standard [and transition period ending November 2018], the location code has been re-defined
      as a 'party suffix' without any specific meaning. A new reference data attribute has been introduced in the SWIFTRef
      directories to indicate where the institution is located and to which time zone it refers.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/BusinessIdentifierCode
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/isIncludedIn
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/BusinessIdentifierCodeScheme
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/isDefinedIn
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeElement
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/BusinessPartySuffix
sources:
- id: fibo-source-6e6990f74b
  resource: references/fibo/FBC/FunctionalEntities/FinancialServicesEntities.rdf
  sha256: 6e6990f74b40d4b0500a945cb9492927f845764329794290952c527016de49c1
  title: FIBO source FBC/FunctionalEntities/FinancialServicesEntities.rdf
title: business party suffix
type: Ontology Class
---

# business party suffix

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/BusinessPartySuffix>

## Definition

two-character (2 alphanumeric) code associated with the organization for the purposes of banking telecommunications

## Relationships

- **Subclass of**: [CodeElement](<https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeElement>)

## Constraints

- **[isIncludedIn](<https://www.omg.org/spec/Commons/Collections/isIncludedIn>)**: some values from of type [BusinessIdentifierCode](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/BusinessIdentifierCode.md)
- **[isDefinedIn](<https://www.omg.org/spec/Commons/Designators/isDefinedIn>)**: some values from of type [BusinessIdentifierCodeScheme](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/BusinessIdentifierCodeScheme.md)

## Annotations

- **label**: business party suffix
- **definition**: two-character (2 alphanumeric) code associated with the organization for the purposes of banking telecommunications
- **adaptedFrom**: ISO 9362:2014 Banking -- Banking telecommunication messages -- Business identifier code (BIC)
- **explanatoryNote**: In the prior version of the standard, position 7 of the BIC determined the location of the BIC in a particular country. In a country spanning over multiple time zones, each character may have been used to define a different time zone. If an organization moved location to a different time zone within the same country, the existing BIC would normally have been deleted and replaced by a new BIC with the appropriate location code.
- **explanatoryNote**: With the revision of the standard [and transition period ending November 2018], the location code has been re-defined as a 'party suffix' without any specific meaning. A new reference data attribute has been introduced in the SWIFTRef directories to indicate where the institution is located and to which time zone it refers.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
