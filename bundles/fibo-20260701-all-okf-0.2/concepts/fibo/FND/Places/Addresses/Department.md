---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: department
  - language: es
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: departamento
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: division of a large organization such as a government, university, business, or shop, dealing with a specific subject,
      commodity, or area of activity
  - datatype: http://www.w3.org/2001/XMLSchema#boolean
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/requiresSecondaryUnitRange
    value: 'true'
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/preferredDesignation
    value: DEPT
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/SecondaryUnitDesignator
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/Department
sources:
- id: fibo-source-e5a4db8fbf
  resource: references/fibo/FND/Places/Addresses.rdf
  sha256: e5a4db8fbf9370292825e1ee83afc60b2a554dbf2e9b723a527d4f3a6903178d
  title: FIBO source FND/Places/Addresses.rdf
- id: fibo-source-e1b8af13cf
  resource: references/fibo/FND/Places/NorthAmerica/USPostalServiceAddresses.rdf
  sha256: e1b8af13cfbd56c65e428ff820890c7d7d5b5057af269667e5305e15ef80b1c6
  title: FIBO source FND/Places/NorthAmerica/USPostalServiceAddresses.rdf
title: department
type: Ontology Individual
---

# department

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/Department>

## Definition

division of a large organization such as a government, university, business, or shop, dealing with a specific subject, commodity, or area of activity

## Annotations

- **label** (en): department
- **label** (es): departamento
- **definition**: division of a large organization such as a government, university, business, or shop, dealing with a specific subject, commodity, or area of activity
- **requiresSecondaryUnitRange**: true
- **preferredDesignation**: DEPT

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
