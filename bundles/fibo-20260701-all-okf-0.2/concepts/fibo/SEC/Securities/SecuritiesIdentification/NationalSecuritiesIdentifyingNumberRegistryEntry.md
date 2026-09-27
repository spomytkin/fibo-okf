---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: national numbering agency registry entry
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: entry in a National Securities Identifying Number registry
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/NationalSecuritiesIdentifyingNumber
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIdentification/SecurityRegistryEntry.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/SecurityRegistryEntry
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/NationalSecuritiesIdentifyingNumberRegistryEntry
sources:
- id: fibo-source-966091c50a
  resource: references/fibo/SEC/Securities/SecuritiesIdentification.rdf
  sha256: 966091c50a68aae0becec1ae82b25a9fa7129356c4caa9b25ba1ed33b8fdd2cf
  title: FIBO source SEC/Securities/SecuritiesIdentification.rdf
title: national numbering agency registry entry
type: Ontology Class
---

# national numbering agency registry entry

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/NationalSecuritiesIdentifyingNumberRegistryEntry>

## Definition

entry in a National Securities Identifying Number registry

## Relationships

- **Subclass of**: [SecurityRegistryEntry](/concepts/fibo/SEC/Securities/SecuritiesIdentification/SecurityRegistryEntry.md)

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [NationalSecuritiesIdentifyingNumber](/concepts/fibo/SEC/Securities/SecuritiesIdentification/NationalSecuritiesIdentifyingNumber.md)

## Annotations

- **label**: national numbering agency registry entry
- **definition**: entry in a National Securities Identifying Number registry

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
