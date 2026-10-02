---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: business party prefix
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: four-character (4 alphanumeric) code associated with an organization for the purposes of banking telecommunications
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 9362:2014 Banking -- Banking telecommunication messages -- Business identifier code (BIC)
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: For new BIC registration by an organization already identified with a BIC or an affiliated organization [after
      the transition period ending November 2018], SWIFT will still reserve the usage of an existing party prefix to these
      organizations. This legacy rule will be reserved to existing BIC owners. If they wish to preserve this value, no other
      organization will be allowed to use the same code
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: For new BIC registration from an organization not yet identified by a BIC, the party prefix will be allocated at
      the discretion of the RA. The code will not have a mnemonic or acronym value anymore.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: bank code
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: institution code
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/BusinessIdentifierCode
    kind: max_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/isIncludedIn
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/BusinessIdentifierCodeScheme
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/isDefinedIn
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeElement
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Organizations/OrganizationIdentifier
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/BusinessPartyPrefix
sources:
- id: fibo-source-6e6990f74b
  resource: references/fibo/FBC/FunctionalEntities/FinancialServicesEntities.rdf
  sha256: 6e6990f74b40d4b0500a945cb9492927f845764329794290952c527016de49c1
  title: FIBO source FBC/FunctionalEntities/FinancialServicesEntities.rdf
title: business party prefix
type: Ontology Class
---

# business party prefix

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/BusinessPartyPrefix>

## Definition

four-character (4 alphanumeric) code associated with an organization for the purposes of banking telecommunications

## Relationships

- **Subclass of**: [CodeElement](<https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeElement>)
- **Subclass of**: [OrganizationIdentifier](<https://www.omg.org/spec/Commons/Organizations/OrganizationIdentifier>)

## Constraints

- **[isIncludedIn](<https://www.omg.org/spec/Commons/Collections/isIncludedIn>)**: max qualified cardinality 1 of type [BusinessIdentifierCode](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/BusinessIdentifierCode.md)
- **[isDefinedIn](<https://www.omg.org/spec/Commons/Designators/isDefinedIn>)**: some values from of type [BusinessIdentifierCodeScheme](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/BusinessIdentifierCodeScheme.md)

## Annotations

- **label**: business party prefix
- **definition**: four-character (4 alphanumeric) code associated with an organization for the purposes of banking telecommunications
- **adaptedFrom**: ISO 9362:2014 Banking -- Banking telecommunication messages -- Business identifier code (BIC)
- **explanatoryNote**: For new BIC registration by an organization already identified with a BIC or an affiliated organization [after the transition period ending November 2018], SWIFT will still reserve the usage of an existing party prefix to these organizations. This legacy rule will be reserved to existing BIC owners. If they wish to preserve this value, no other organization will be allowed to use the same code
- **explanatoryNote**: For new BIC registration from an organization not yet identified by a BIC, the party prefix will be allocated at the discretion of the RA. The code will not have a mnemonic or acronym value anymore.
- **synonym**: bank code
- **synonym**: institution code

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
