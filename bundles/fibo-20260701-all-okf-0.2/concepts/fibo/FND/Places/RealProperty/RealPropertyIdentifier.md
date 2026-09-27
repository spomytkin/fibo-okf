---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: real property identifier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: unique identifier given to identify a specific real property in some jurisidiction
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/ContextualDesignators/isApplicableIn
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Places/RealProperty/RealProperty
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/identifies
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/ContextualIdentifiers/ContextualIdentifier
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/RealProperty/RealPropertyIdentifier
sources:
- id: fibo-source-f0e5ecd06c
  resource: references/fibo/FND/Places/RealProperty.rdf
  sha256: f0e5ecd06c164d1e5fff0c1236869b2014bcba3d7008365dcc2c7363064202bd
  title: FIBO source FND/Places/RealProperty.rdf
title: real property identifier
type: Ontology Class
---

# real property identifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/RealProperty/RealPropertyIdentifier>

## Definition

unique identifier given to identify a specific real property in some jurisidiction

## Relationships

- **Subclass of**: [ContextualIdentifier](<https://www.omg.org/spec/Commons/ContextualIdentifiers/ContextualIdentifier>)

## Constraints

- **[isApplicableIn](<https://www.omg.org/spec/Commons/ContextualDesignators/isApplicableIn>)**: min qualified cardinality 0 of type [Jurisdiction](<https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction>)
- **[identifies](<https://www.omg.org/spec/Commons/Identifiers/identifies>)**: exact qualified cardinality 1 of type [RealProperty](/concepts/fibo/FND/Places/RealProperty/RealProperty.md)

## Annotations

- **label**: real property identifier
- **definition**: unique identifier given to identify a specific real property in some jurisidiction

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
