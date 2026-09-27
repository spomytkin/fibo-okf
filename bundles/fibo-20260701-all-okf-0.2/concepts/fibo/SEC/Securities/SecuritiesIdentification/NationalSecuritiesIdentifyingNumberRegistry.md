---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: National Securities Identifying Number registry
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: registry used by a national numbering agency to manage the financial instrument identifiers and related information
      that it registers
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: NSIN registry
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/NationalSecurityIdentificationScheme
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Classifiers/isCharacterizedBy
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/NationalSecuritiesIdentifyingNumberRegistryEntry
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/NationalNumberingAgency
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Organizations/isManagedBy
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIdentification/SecurityRegistry.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/SecurityRegistry
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/NationalSecuritiesIdentifyingNumberRegistry
sources:
- id: fibo-source-966091c50a
  resource: references/fibo/SEC/Securities/SecuritiesIdentification.rdf
  sha256: 966091c50a68aae0becec1ae82b25a9fa7129356c4caa9b25ba1ed33b8fdd2cf
  title: FIBO source SEC/Securities/SecuritiesIdentification.rdf
title: National Securities Identifying Number registry
type: Ontology Class
---

# National Securities Identifying Number registry

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/NationalSecuritiesIdentifyingNumberRegistry>

## Definition

registry used by a national numbering agency to manage the financial instrument identifiers and related information that it registers

## Relationships

- **Subclass of**: [SecurityRegistry](/concepts/fibo/SEC/Securities/SecuritiesIdentification/SecurityRegistry.md)

## Constraints

- **[isCharacterizedBy](<https://www.omg.org/spec/Commons/Classifiers/isCharacterizedBy>)**: exact qualified cardinality 1 of type [NationalSecurityIdentificationScheme](/concepts/fibo/SEC/Securities/SecuritiesIdentification/NationalSecurityIdentificationScheme.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [NationalSecuritiesIdentifyingNumberRegistryEntry](/concepts/fibo/SEC/Securities/SecuritiesIdentification/NationalSecuritiesIdentifyingNumberRegistryEntry.md)
- **[isManagedBy](<https://www.omg.org/spec/Commons/Organizations/isManagedBy>)**: some values from of type [NationalNumberingAgency](/concepts/fibo/SEC/Securities/SecuritiesIdentification/NationalNumberingAgency.md)

## Annotations

- **label**: National Securities Identifying Number registry
- **definition**: registry used by a national numbering agency to manage the financial instrument identifiers and related information that it registers
- **abbreviation**: NSIN registry

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
