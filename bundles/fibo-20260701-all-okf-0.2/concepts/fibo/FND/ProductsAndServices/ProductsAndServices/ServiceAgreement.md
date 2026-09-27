---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: service agreement
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: written contract between a client and service provider whereby the service provider supplies some service in the
      form of time, effort, and/or expertise in exchange for compensation
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: service contract
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/Organizations/ServiceProvider
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractParty
  - filler: https://www.omg.org/spec/Commons/Organizations/Service
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RegulatoryAgencies/governs
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/WrittenContract.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/WrittenContract
resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/ServiceAgreement
sources:
- id: fibo-source-7f330c2b6d
  resource: references/fibo/FND/ProductsAndServices/ProductsAndServices.rdf
  sha256: 7f330c2b6de4e90f2c5d728ddf32af1d75f320646040450c1da9a8c5f8740548
  title: FIBO source FND/ProductsAndServices/ProductsAndServices.rdf
title: service agreement
type: Ontology Class
---

# service agreement

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/ServiceAgreement>

## Definition

written contract between a client and service provider whereby the service provider supplies some service in the form of time, effort, and/or expertise in exchange for compensation

## Relationships

- **Subclass of**: [WrittenContract](/concepts/fibo/FND/Agreements/Contracts/WrittenContract.md)

## Constraints

- **[hasContractParty](/concepts/fibo/FND/Agreements/Contracts/hasContractParty.md)**: exact qualified cardinality 1 of type [ServiceProvider](<https://www.omg.org/spec/Commons/Organizations/ServiceProvider>)
- **[governs](<https://www.omg.org/spec/Commons/RegulatoryAgencies/governs>)**: some values from of type [Service](<https://www.omg.org/spec/Commons/Organizations/Service>)

## Annotations

- **label**: service agreement
- **definition**: written contract between a client and service provider whereby the service provider supplies some service in the form of time, effort, and/or expertise in exchange for compensation
- **synonym**: service contract

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
