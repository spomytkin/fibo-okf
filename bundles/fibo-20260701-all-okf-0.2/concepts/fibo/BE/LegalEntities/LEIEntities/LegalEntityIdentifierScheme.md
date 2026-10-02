---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: legal entity identifier scheme
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: a scheme that specifies the elements of an unambiguous legal entity identifier (LEI) scheme to identify the legal
      entities relevant to any financial transaction
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.gleif.org/en/about-lei/common-data-file-format/lei-cdf-format/lei-cdf-format-version-2-1
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.iso.org/standard/59771.html
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/LegalEntityIdentifier
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/defines
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Organizations/OrganizationIdentificationScheme
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/LegalEntityIdentifierScheme
sources:
- id: fibo-source-535adad55c
  resource: references/fibo/BE/LegalEntities/LEIEntities.rdf
  sha256: 535adad55c4f6fe3ad7131256c4a1602e8c4727fbef1a89c338de8d9559a4cca
  title: FIBO source BE/LegalEntities/LEIEntities.rdf
title: legal entity identifier scheme
type: Ontology Class
---

# legal entity identifier scheme

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/LegalEntityIdentifierScheme>

## Definition

a scheme that specifies the elements of an unambiguous legal entity identifier (LEI) scheme to identify the legal entities relevant to any financial transaction

## Relationships

- **Subclass of**: [OrganizationIdentificationScheme](<https://www.omg.org/spec/Commons/Organizations/OrganizationIdentificationScheme>)

## Constraints

- **[defines](<https://www.omg.org/spec/Commons/Designators/defines>)**: some values from of type [LegalEntityIdentifier](/concepts/fibo/BE/LegalEntities/LEIEntities/LegalEntityIdentifier.md)

## Annotations

- **label**: legal entity identifier scheme
- **definition**: a scheme that specifies the elements of an unambiguous legal entity identifier (LEI) scheme to identify the legal entities relevant to any financial transaction
- **adaptedFrom**: https://www.gleif.org/en/about-lei/common-data-file-format/lei-cdf-format/lei-cdf-format-version-2-1
- **adaptedFrom**: https://www.iso.org/standard/59771.html

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
