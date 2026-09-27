---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: early termination provision
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: termination of an agreement for any reason prior to its expiration date
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Early termination date refers to the date set within an agreement for the parties to exercise the option to terminate
      the contract prior to its original expiration, typically subject to predefined terms such as notice periods or specific
      conditions. Early termination may be automatically triggered by an event of default with respect to any contract obligation,
      due to corporate action, or for other reasons. An early termination date may be calculated per the terms of the agreement
      or specified explicitly at the time the termination event occurs.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Documents/hasExpirationDate
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/TerminationProvision.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/TerminationProvision
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/EarlyTerminationProvision
sources:
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: early termination provision
type: Ontology Class
---

# early termination provision

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/EarlyTerminationProvision>

## Definition

termination of an agreement for any reason prior to its expiration date

## Relationships

- **Subclass of**: [TerminationProvision](/concepts/fibo/FND/Agreements/Contracts/TerminationProvision.md)

## Constraints

- **[hasExpirationDate](/concepts/fibo/FND/Arrangements/Documents/hasExpirationDate.md)**: some values from of type [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)

## Annotations

- **label**: early termination provision
- **definition**: termination of an agreement for any reason prior to its expiration date
- **explanatoryNote**: Early termination date refers to the date set within an agreement for the parties to exercise the option to terminate the contract prior to its original expiration, typically subject to predefined terms such as notice periods or specific conditions. Early termination may be automatically triggered by an event of default with respect to any contract obligation, due to corporate action, or for other reasons. An early termination date may be calculated per the terms of the agreement or specified explicitly at the time the termination event occurs.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
