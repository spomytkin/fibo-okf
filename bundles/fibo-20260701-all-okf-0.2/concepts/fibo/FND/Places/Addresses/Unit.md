---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: unit
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: area in a facility, such as a medical facility or hospital that is specially staffed and equipped to provide a
      particular service or type of care
  - datatype: http://www.w3.org/2001/XMLSchema#boolean
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/requiresSecondaryUnitRange
    value: 'true'
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/preferredDesignation
    value: UNIT
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/SecondaryUnitDesignator
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/Unit
sources:
- id: fibo-source-e5a4db8fbf
  resource: references/fibo/FND/Places/Addresses.rdf
  sha256: e5a4db8fbf9370292825e1ee83afc60b2a554dbf2e9b723a527d4f3a6903178d
  title: FIBO source FND/Places/Addresses.rdf
- id: fibo-source-e1b8af13cf
  resource: references/fibo/FND/Places/NorthAmerica/USPostalServiceAddresses.rdf
  sha256: e1b8af13cfbd56c65e428ff820890c7d7d5b5057af269667e5305e15ef80b1c6
  title: FIBO source FND/Places/NorthAmerica/USPostalServiceAddresses.rdf
title: unit
type: Ontology Individual
---

# unit

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/Unit>

## Definition

area in a facility, such as a medical facility or hospital that is specially staffed and equipped to provide a particular service or type of care

## Annotations

- **label** (en): unit
- **definition**: area in a facility, such as a medical facility or hospital that is specially staffed and equipped to provide a particular service or type of care
- **requiresSecondaryUnitRange**: true
- **preferredDesignation**: UNIT

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
