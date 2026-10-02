---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: security identification scheme
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: formal definition of the structure and application of a particular set of securities identifiers
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/SecurityIdentifier
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/defines
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIdentification/FinancialInstrumentIdentificationScheme.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/FinancialInstrumentIdentificationScheme
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/RegistrationAuthorities/RegistrationScheme
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/SecurityIdentificationScheme
sources:
- id: fibo-source-966091c50a
  resource: references/fibo/SEC/Securities/SecuritiesIdentification.rdf
  sha256: 966091c50a68aae0becec1ae82b25a9fa7129356c4caa9b25ba1ed33b8fdd2cf
  title: FIBO source SEC/Securities/SecuritiesIdentification.rdf
title: security identification scheme
type: Ontology Class
---

# security identification scheme

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/SecurityIdentificationScheme>

## Definition

formal definition of the structure and application of a particular set of securities identifiers

## Relationships

- **Subclass of**: [FinancialInstrumentIdentificationScheme](/concepts/fibo/SEC/Securities/SecuritiesIdentification/FinancialInstrumentIdentificationScheme.md)
- **Subclass of**: [RegistrationScheme](<https://www.omg.org/spec/Commons/RegistrationAuthorities/RegistrationScheme>)

## Constraints

- **[defines](<https://www.omg.org/spec/Commons/Designators/defines>)**: some values from of type [SecurityIdentifier](/concepts/fibo/SEC/Securities/SecuritiesIdentification/SecurityIdentifier.md)

## Annotations

- **label**: security identification scheme
- **definition**: formal definition of the structure and application of a particular set of securities identifiers

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
