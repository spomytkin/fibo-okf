---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has fractional interest
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: has proportionate, non-exclusive entitlement to
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Fractional interest may be expressed as a percentage, ratio, or unit count, and typically arises in contexts where
      multiple parties share contractual claims to income, usage, ownership, or participation. It does not imply full control
      or sole ownership, and may be subject to limitations specified in the underlying legal framework.
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#decimal
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasNumericValue
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/hasFractionalInterest
sources:
- id: fibo-source-544b6eb4c7
  resource: references/fibo/FND/Law/LegalCapacity.rdf
  sha256: 544b6eb4c7d0acd6efdeb794a9af17ec89bec5145b178192396defaa50bbef22
  title: FIBO source FND/Law/LegalCapacity.rdf
title: has fractional interest
type: Ontology Property
---

# has fractional interest

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/hasFractionalInterest>

## Definition

has proportionate, non-exclusive entitlement to

## Relationships

- **Range**: [decimal](<http://www.w3.org/2001/XMLSchema#decimal>)
- **Subproperty of**: [hasNumericValue](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasNumericValue>)

## Annotations

- **label**: has fractional interest
- **definition**: has proportionate, non-exclusive entitlement to
- **explanatoryNote**: Fractional interest may be expressed as a percentage, ratio, or unit count, and typically arises in contexts where multiple parties share contractual claims to income, usage, ownership, or participation. It does not imply full control or sole ownership, and may be subject to limitations specified in the underlying legal framework.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
