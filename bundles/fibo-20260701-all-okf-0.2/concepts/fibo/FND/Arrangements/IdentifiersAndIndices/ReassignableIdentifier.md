---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: reassignable identifier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identifier that uniquely identifies something for a given time period, and that may be reused to identify something
      else at a different point in time
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: ticker symbol, vehicle license number, such as a vanity plate that can be reassigned and moved from one car to
      another
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: If no assignment termination date is provided, the identifier is considered to be assigned and valid. If there
      is no initial assignment date, then the identifier is assumed to be assigned up until the termination date, if any.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime
    kind: max_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/IdentifiersAndIndices/hasAssignmentTerminationDate
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime
    kind: max_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/IdentifiersAndIndices/hasInitialAssignmentDate
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Identifiers/Identifier
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/IdentifiersAndIndices/ReassignableIdentifier
sources:
- id: fibo-source-2943e244c9
  resource: references/fibo/FND/Arrangements/IdentifiersAndIndices.rdf
  sha256: 2943e244c9f1e05582f4cd0ce73c69f5f8a148d740aa66d458c621a1ad24f51c
  title: FIBO source FND/Arrangements/IdentifiersAndIndices.rdf
title: reassignable identifier
type: Ontology Class
---

# reassignable identifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/IdentifiersAndIndices/ReassignableIdentifier>

## Definition

identifier that uniquely identifies something for a given time period, and that may be reused to identify something else at a different point in time

## Relationships

- **Subclass of**: [Identifier](<https://www.omg.org/spec/Commons/Identifiers/Identifier>)

## Constraints

- **[hasAssignmentTerminationDate](/concepts/fibo/FND/Arrangements/IdentifiersAndIndices/hasAssignmentTerminationDate.md)**: max qualified cardinality 1 of type [CombinedDateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime>)
- **[hasInitialAssignmentDate](/concepts/fibo/FND/Arrangements/IdentifiersAndIndices/hasInitialAssignmentDate.md)**: max qualified cardinality 1 of type [CombinedDateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime>)

## Annotations

- **label**: reassignable identifier
- **definition**: identifier that uniquely identifies something for a given time period, and that may be reused to identify something else at a different point in time
- **example**: ticker symbol, vehicle license number, such as a vanity plate that can be reassigned and moved from one car to another
- **explanatoryNote**: If no assignment termination date is provided, the identifier is considered to be assigned and valid. If there is no initial assignment date, then the identifier is assumed to be assigned up until the termination date, if any.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
