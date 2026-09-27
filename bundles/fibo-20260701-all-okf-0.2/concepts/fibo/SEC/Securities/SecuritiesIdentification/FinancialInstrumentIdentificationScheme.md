---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: financial instrument identification scheme
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: formal definition of the structure and application of a particular set of financial instrument identifiers
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrumentIdentifier
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Identifiers/IdentificationScheme
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/FinancialInstrumentIdentificationScheme
sources:
- id: fibo-source-966091c50a
  resource: references/fibo/SEC/Securities/SecuritiesIdentification.rdf
  sha256: 966091c50a68aae0becec1ae82b25a9fa7129356c4caa9b25ba1ed33b8fdd2cf
  title: FIBO source SEC/Securities/SecuritiesIdentification.rdf
title: financial instrument identification scheme
type: Ontology Class
---

# financial instrument identification scheme

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/FinancialInstrumentIdentificationScheme>

## Definition

formal definition of the structure and application of a particular set of financial instrument identifiers

## Relationships

- **Subclass of**: [IdentificationScheme](<https://www.omg.org/spec/Commons/Identifiers/IdentificationScheme>)

## Constraints

- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from of type [FinancialInstrumentIdentifier](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrumentIdentifier.md)

## Annotations

- **label**: financial instrument identification scheme
- **definition**: formal definition of the structure and application of a particular set of financial instrument identifiers

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
