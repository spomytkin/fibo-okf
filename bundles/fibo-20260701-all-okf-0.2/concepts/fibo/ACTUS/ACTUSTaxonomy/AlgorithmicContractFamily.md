---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: algorithmic contract family
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: classifier for a collection of types of contracts, such as credit agreements, financial instruments, or related
      kinds of contracts, based on their common characteristics from an ACTUS perspective
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CashFlows/CashFlowStructure
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/classifies
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Designators/isDefinedIn
    value: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/AlgorithmicContractTypesClassificationScheme
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/Documents/refersTo
    value: Nec96980d3f21446d897fa6f8b2a3e8e9
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Collections/Collection
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/AlgorithmicContractFamily
sources:
- id: fibo-source-1ffe76217e
  resource: references/fibo/ACTUS/ACTUSContractTermMapping.rdf
  sha256: 1ffe76217e0123653c8a4d03290dcfab352af9fe7a5cdb369ae0e86c55d11bbd
  title: FIBO source ACTUS/ACTUSContractTermMapping.rdf
- id: fibo-source-c715cd4f2e
  resource: references/fibo/ACTUS/ACTUSTaxonomy.rdf
  sha256: c715cd4f2e23f8986a6965786f676ee8eeea6c0496f96a0dd57306fe5907a24a
  title: FIBO source ACTUS/ACTUSTaxonomy.rdf
title: algorithmic contract family
type: Ontology Class
---

# algorithmic contract family

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/AlgorithmicContractFamily>

## Definition

classifier for a collection of types of contracts, such as credit agreements, financial instruments, or related kinds of contracts, based on their common characteristics from an ACTUS perspective

## Relationships

- **Subclass of**: [Collection](<https://www.omg.org/spec/Commons/Collections/Collection>)

## Constraints

- **[classifies](<https://www.omg.org/spec/Commons/Classifiers/classifies>)**: some values from of type [CashFlowStructure](/concepts/fibo/FND/Accounting/CashFlows/CashFlowStructure.md)
- **[isDefinedIn](<https://www.omg.org/spec/Commons/Designators/isDefinedIn>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/AlgorithmicContractTypesClassificationScheme`
- **[refersTo](<https://www.omg.org/spec/Commons/Documents/refersTo>)**: some values from value `Nec96980d3f21446d897fa6f8b2a3e8e9`

## Annotations

- **label**: algorithmic contract family
- **definition**: classifier for a collection of types of contracts, such as credit agreements, financial instruments, or related kinds of contracts, based on their common characteristics from an ACTUS perspective

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
