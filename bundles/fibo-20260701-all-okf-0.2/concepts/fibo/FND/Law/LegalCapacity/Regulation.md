---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: regulation
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: a rule used to carry out a law
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Many government agencies issue regulations to administer laws.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCore/Law
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isConferredBy
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/RegulatoryAgencies/RegulatoryAgency
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isIssuedBy
  - filler: https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/isApplicableIn
  subclass_of:
  - concept: /concepts/fibo/FND/Law/LegalCapacity/LegalConstruct.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/LegalConstruct
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/Regulation
sources:
- id: fibo-source-ef717d20cc
  resource: references/fibo/FBC/FunctionalEntities/RegulatoryAgencies.rdf
  sha256: ef717d20cc3804b8cc9643a625bf716211db11cc374a524b54dd5ce7e70bf1db
  title: FIBO source FBC/FunctionalEntities/RegulatoryAgencies.rdf
- id: fibo-source-544b6eb4c7
  resource: references/fibo/FND/Law/LegalCapacity.rdf
  sha256: 544b6eb4c7d0acd6efdeb794a9af17ec89bec5145b178192396defaa50bbef22
  title: FIBO source FND/Law/LegalCapacity.rdf
title: regulation
type: Ontology Class
---

# regulation

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/Regulation>

## Definition

a rule used to carry out a law

## Relationships

- **Subclass of**: [LegalConstruct](/concepts/fibo/FND/Law/LegalCapacity/LegalConstruct.md)

## Constraints

- **[isConferredBy](/concepts/fibo/FND/Relations/Relations/isConferredBy.md)**: some values from of type [Law](/concepts/fibo/FND/Law/LegalCore/Law.md)
- **[isIssuedBy](/concepts/fibo/FND/Relations/Relations/isIssuedBy.md)**: exact qualified cardinality 1 of type [RegulatoryAgency](<https://www.omg.org/spec/Commons/RegulatoryAgencies/RegulatoryAgency>)
- **[isApplicableIn](<https://www.omg.org/spec/Commons/ContextualDesignators/isApplicableIn>)**: some values from of type [Jurisdiction](<https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction>)

## Annotations

- **label**: regulation
- **definition**: a rule used to carry out a law
- **explanatoryNote**: Many government agencies issue regulations to administer laws.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
