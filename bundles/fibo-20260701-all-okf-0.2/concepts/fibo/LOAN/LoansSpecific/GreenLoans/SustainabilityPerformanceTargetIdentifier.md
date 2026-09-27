---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: sustainability performance target identifier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: sequence of characters uniquely identifying a specific sustainability-related performance target
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/SustainabilityPerformanceTarget
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Identifiers/identifies
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/ContextualIdentifiers/ContextualIdentifier
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/SustainabilityPerformanceTargetIdentifier
sources:
- id: fibo-source-cff1f078be
  resource: references/fibo/LOAN/LoansSpecific/GreenLoans.rdf
  sha256: cff1f078bed4eeb9970073ab5ccbace470a24c6150ac1e18310cbe1894b9e006
  title: FIBO source LOAN/LoansSpecific/GreenLoans.rdf
title: sustainability performance target identifier
type: Ontology Class
---

# sustainability performance target identifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/SustainabilityPerformanceTargetIdentifier>

## Definition

sequence of characters uniquely identifying a specific sustainability-related performance target

## Relationships

- **Subclass of**: [ContextualIdentifier](<https://www.omg.org/spec/Commons/ContextualIdentifiers/ContextualIdentifier>)

## Constraints

- **[identifies](<https://www.omg.org/spec/Commons/Identifiers/identifies>)**: some values from of type [SustainabilityPerformanceTarget](/concepts/fibo/LOAN/LoansSpecific/GreenLoans/SustainabilityPerformanceTarget.md)

## Annotations

- **label** (en): sustainability performance target identifier
- **definition**: sequence of characters uniquely identifying a specific sustainability-related performance target

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
