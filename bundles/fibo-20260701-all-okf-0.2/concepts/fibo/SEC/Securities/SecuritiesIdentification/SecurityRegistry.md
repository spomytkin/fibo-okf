---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: security registry
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: registry used to manage security identifiers and related information
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Securities registries may be managed by an exchange, clearing house, custodian, bank, or other financial services
      provider.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/SecurityIdentificationScheme
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Classifiers/isCharacterizedBy
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/SecurityRegistryEntry
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - filler: https://www.omg.org/spec/Commons/RegistrationAuthorities/RegistrationAuthority
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Organizations/isManagedBy
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/RegistrationAuthorities/Registry
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/SecurityRegistry
sources:
- id: fibo-source-966091c50a
  resource: references/fibo/SEC/Securities/SecuritiesIdentification.rdf
  sha256: 966091c50a68aae0becec1ae82b25a9fa7129356c4caa9b25ba1ed33b8fdd2cf
  title: FIBO source SEC/Securities/SecuritiesIdentification.rdf
title: security registry
type: Ontology Class
---

# security registry

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/SecurityRegistry>

## Definition

registry used to manage security identifiers and related information

## Relationships

- **Subclass of**: [Registry](<https://www.omg.org/spec/Commons/RegistrationAuthorities/Registry>)

## Constraints

- **[isCharacterizedBy](<https://www.omg.org/spec/Commons/Classifiers/isCharacterizedBy>)**: exact qualified cardinality 1 of type [SecurityIdentificationScheme](/concepts/fibo/SEC/Securities/SecuritiesIdentification/SecurityIdentificationScheme.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [SecurityRegistryEntry](/concepts/fibo/SEC/Securities/SecuritiesIdentification/SecurityRegistryEntry.md)
- **[isManagedBy](<https://www.omg.org/spec/Commons/Organizations/isManagedBy>)**: some values from of type [RegistrationAuthority](<https://www.omg.org/spec/Commons/RegistrationAuthorities/RegistrationAuthority>)

## Annotations

- **label**: security registry
- **definition**: registry used to manage security identifiers and related information
- **explanatoryNote**: Securities registries may be managed by an exchange, clearing house, custodian, bank, or other financial services provider.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
