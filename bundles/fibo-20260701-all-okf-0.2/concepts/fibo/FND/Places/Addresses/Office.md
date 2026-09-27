---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: office
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: place where a particular kind of business is transacted or a service is supplied
  - datatype: http://www.w3.org/2001/XMLSchema#boolean
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/requiresSecondaryUnitRange
    value: 'false'
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/preferredDesignation
    value: OFC
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/SecondaryUnitDesignator
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/Office
sources:
- id: fibo-source-e5a4db8fbf
  resource: references/fibo/FND/Places/Addresses.rdf
  sha256: e5a4db8fbf9370292825e1ee83afc60b2a554dbf2e9b723a527d4f3a6903178d
  title: FIBO source FND/Places/Addresses.rdf
- id: fibo-source-e1b8af13cf
  resource: references/fibo/FND/Places/NorthAmerica/USPostalServiceAddresses.rdf
  sha256: e1b8af13cfbd56c65e428ff820890c7d7d5b5057af269667e5305e15ef80b1c6
  title: FIBO source FND/Places/NorthAmerica/USPostalServiceAddresses.rdf
title: office
type: Ontology Individual
---

# office

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/Office>

## Definition

place where a particular kind of business is transacted or a service is supplied

## Annotations

- **label** (en): office
- **definition**: place where a particular kind of business is transacted or a service is supplied
- **requiresSecondaryUnitRange**: false
- **preferredDesignation**: OFC

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
