---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: request
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: event in which some party asks another party for something at some point in time
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/hasRequestDate
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/DateTime
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/hasRequestDateTime
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/Requester
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/isRequestedBy
  - filler: https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/isRequestedOf
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/RequestActivity
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/exemplifies
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/Occurrences/Occurrence.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/Occurrence
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/Request
sources:
- id: fibo-source-a52060e8b1
  resource: references/fibo/FND/Arrangements/Reporting.rdf
  sha256: a52060e8b187a3f08302027cf7c7be15c9b644d9a3a7105f69a6415913db5143
  title: FIBO source FND/Arrangements/Reporting.rdf
title: request
type: Ontology Class
---

# request

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/Request>

## Definition

event in which some party asks another party for something at some point in time

## Relationships

- **Subclass of**: [Occurrence](/concepts/fibo/FND/DatesAndTimes/Occurrences/Occurrence.md)

## Constraints

- **[hasRequestDate](/concepts/fibo/FND/Arrangements/Reporting/hasRequestDate.md)**: min qualified cardinality 0 of type [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)
- **[hasRequestDateTime](/concepts/fibo/FND/Arrangements/Reporting/hasRequestDateTime.md)**: min qualified cardinality 0 of type [DateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/DateTime>)
- **[isRequestedBy](/concepts/fibo/FND/Arrangements/Reporting/isRequestedBy.md)**: some values from of type [Requester](/concepts/fibo/FND/Arrangements/Reporting/Requester.md)
- **[isRequestedOf](/concepts/fibo/FND/Arrangements/Reporting/isRequestedOf.md)**: some values from of type [PartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole>)
- **[exemplifies](/concepts/fibo/FND/Relations/Relations/exemplifies.md)**: some values from of type [RequestActivity](/concepts/fibo/FND/Arrangements/Reporting/RequestActivity.md)

## Annotations

- **label**: request
- **definition**: event in which some party asks another party for something at some point in time

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
